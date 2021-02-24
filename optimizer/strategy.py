import os
import math
import random
import matplotlib.pyplot as plt
from abc import abstractmethod

from optimizer.utils import run_cpp
from optimizer.get_score import compute_score

TEMP_OUT_PATH = "out_temp.txt"


class Strategy:
    def __init__(self, params, steps, graph):
        self.params = params
        self.steps = steps
        self.graph = graph

    @abstractmethod
    def execute(self, executable, data_path):
        pass


class SimulatedAnnealingStrategy(Strategy):
    def __init__(self, params, steps, num_neighbours, lambda_exp, graph):
        super().__init__(params, steps, graph)
        self.num_neighbours = num_neighbours
        self.lambda_exp = lambda_exp

    def change_state(self, score, best, step):
        if score > best:
            return True

        # Temperature is positive and decreasing with each iteration
        temperature = self.steps - step
        difference = best - score
        threshold = math.exp(-self.lambda_exp*difference/temperature)
        return random.uniform(0, 1) < threshold

    def execute(self, executable, data_path):
        input_path = f"inputs/{data_path}"
        best_out_path = f"outputs/{data_path}_output.txt"

        best_file_score = -1
        if os.path.exists(best_out_path):
            best_file_score = compute_score(input_path, best_out_path)
            print(f"INITIAL BEST SCORE: {best_file_score}")

        scores = []
        param_values = [[] for _ in self.params]

        for step in range(self.steps):
            # If it's the first iteration, do the same as the random strategy would
            if step == 0:
                values = []
                params = []
                for param in self.params:
                    value = param.generate_random()
                    values.append(value)
                    params.append(param.name)
                    params.append(str(value))
                run_cpp(params, executable, data_path)
                best = compute_score(input_path, TEMP_OUT_PATH)
                scores.append(best)
                previous_values = values
                if best > best_file_score:
                    os.rename(TEMP_OUT_PATH, best_out_path)
                    best_file_score = best

                print(f"Iteration {step} - Score: {best}")
            else:
                # Add previous_values to param_values
                for i, val in enumerate(previous_values):
                    param_values[i].append(val)

                moved = False
                # Try as many times as num_neighbours
                for _ in range(self.num_neighbours):
                    # Generate a neighbour close to the previous guess
                    values = []
                    params = []
                    for param, prev in zip(self.params, previous_values):
                        value = param.generate_nearby(prev)
                        values.append(value)
                        params.append(param.name)
                        params.append(str(value))
                    run_cpp(params, executable, data_path)
                    score = compute_score(input_path, TEMP_OUT_PATH)

                    # If we choose to move to this state, change state
                    if self.change_state(score, best, step):
                        if score <= best_file_score:
                            print(
                                f"Iteration {step} - Score {score}"
                            )
                        scores.append(score)
                        previous_values = values
                        moved = True
                    # If this state is better than any other in this execution, update best
                    if score > best:
                        best = score
                    # If this state is better than any other, copy the solution to the "best" file
                    if score > best_file_score:
                        print(
                            f"Iteration {step} - Score: {score} (NEW BEST SCORE)")
                        os.rename(TEMP_OUT_PATH, best_out_path)
                        best_file_score = score
                    # If we changed state, break the loop
                    if moved:
                        break
                # If we weren't able to find a move, end execution
                if not moved:
                    print("Couldn't find a neighbour to move to. Ending execution")
                    break

        print(f"FINAL BEST SCORE: {best_file_score}")
        print(f"Solution at: {best_out_path}")

        if self.graph:
            plt.figure("Score")
            plt.title("Score over time")
            plt.xlabel("Iterations")
            plt.ylabel("Score")
            plt.grid(True)
            plt.plot(list(range(len(scores))), scores)

            for param, vals in zip(self.params, param_values):
                plt.figure(f"Parameter {param.name}")
                plt.title(f"Parameter {param.name} over time")
                plt.xlabel("Iterations")
                plt.ylabel("Value")
                plt.ylim(param.lower, param.upper)
                plt.grid(True)
                plt.plot(list(range(len(vals))), vals)
                plt.show()


class RandomStrategy(Strategy):
    def __init__(self, params, steps, graph):
        super().__init__(params, steps, graph)

    def generate_params(self):
        res = []
        for param in self.params:
            res.append(param.name)
            res.append(str(param.generate_random()))
        return res

    def execute(self, executable, data_path):
        input_path = f"inputs/{data_path}"
        best_out_path = f"outputs/{data_path}_output.txt"

        best_file_score = -1
        if os.path.exists(best_out_path):
            best_file_score = compute_score(input_path, best_out_path)
            print(f"INITIAL BEST SCORE: {best_file_score}")

        scores = []

        for step in range(self.steps):
            params = self.generate_params()
            run_cpp(params, executable, data_path)
            score = compute_score(input_path, TEMP_OUT_PATH)
            scores.append(score)
            if score > best_file_score:
                print(f"Iteration {step} - Score: {score} (NEW BEST SCORE)")
                os.rename(TEMP_OUT_PATH, best_out_path)
                best_file_score = score
            else:
                print(f"Iteration {step} - Score: {score}")

        print(f"FINAL BEST SCORE: {best_file_score}")
        print(f"Solution at: {best_out_path}")

        if self.graph:
            plt.title("Score boxplot")
            plt.ylabel("Score")
            plt.boxplot(scores)
            plt.show()
