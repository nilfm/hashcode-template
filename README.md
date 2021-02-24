# hashcode-template

This repository is meant to serve as a framework to write Google Hashcode solutions in. It offers automated optimization of the solution with respect to the chosen parameters.

## What is Google Hashcode?

Google Hashcode is a contest in which a team is given a problem statement and 6 data sets and they have to generate the best possible output for each of them. The contestant's score is the sum of their scores in all data sets. The problems are hard enough that there isn't usually an optimal solution that runs in a feasible time.

## Why is this useful?

Since the problem can't be solved optimally, a common way to get a good score is to use a greedy algorithm and randomize parts of it. The advantage of randomization is that the program can be re-run multiple times and keep the best score. Because of this, once the randomized parameters have been chosen, it becomes an optimization problem. 

This framework enables the user to choose which parameters to randomize and easily integrates into their C++ code. Then, it offers automatic optimization of a given score function with respect to these parameters. The user can choose between a random strategy and a simulated annealing algorithm.

## How do I work with it?

In order to work with this template, the user will need to make some changes to the original repo (which is just a trivial example problem):

* Implement `compute_score` inside `optimizer/get_score.py`. This function should read the files at the given paths and output a number, which will be the score of that file.
* Decide the parameters that you want to randomize and implement `params.json`. This file contains two lists, one for `float` variables and one for `int` variables. Each variable is a dictionary with the fields `name`, `lower` and `upper` (the bounds of the parameter).
* Implement `cpp_utils/read_data.hh`. This file will contain the necessary data structures to hold the input data (they will be global and accessible from `main.cc` if declared here), as well as the function `read_data`, which initializes these structures.
* Implement `main.cc`. In this file, you should use the data structures from the previous step to reach a solution. You should also use the parameters you chose in `params.json` via the map `p`. Example: `p["threshold"]`.
* Implement `cpp_utils/write_output.hh`. This file will write to `out_temp.txt`, which is a temporary file. All solutions that are good enough will be copied to the `outputs` directory automatically. Pass the desired arguments from `main.cc` to the `write_output` function in order to write the solution to this file.

Once this is done, you can execute `main_random.py` and `main_sim_ann.py` to optimize the score function. The following sections explain how these algorithms work and which parameters can be passed to them via command line arguments.

The `check_score.py` file is a simple script that prints the score of an output file given its path. It uses the previously defined `compute_score` function.

### Random strategy

This strategy is simple: at each iteration, for each parameter, choose a random value between its lower bound and its upper bound. Whenever the current iteration improves the current high score, copy it to the `outputs` directory.

### Simulated annealing strategy

This strategy is a local search algorithm: once it has a solution, it will explore nearby solutions to try to improve the current score. Neigbours are defined as solutions within a radius of 5% of the total domain of each parameter. For each neighbour, it will decide whether to move to the new solution based on the following:

* If the new solution has a better score than the best solution so far, it will always move.
* If the new solution has a worse score than the best solution so far, it will move with probability `exp(-lambda*(best_score - new_score)/temperature)`, where `temperature` is a positive function which decreases with iterations, and `lambda` is a parameter which controls the "risk-adversity" of the algorithm (explained in the following section).

When a solution is found that improves the current high score, it is copied to the `outputs` directory.

### Command-line arguments

This framework offers some customization of the algorithms via command-line arguments, which are listed here:

* `-p`/`--params`: Required argument. Path to the JSON file which defines the parameters.
* `-d`/`--data`: Required argument. Path to the input file **relative to the `inputs` directory**.
* `-s`/`--steps`: Optional argument. Specifies the number of iterations that the algorithm will perform at most. Default: 1000.
* `-x`/`--executable`: Optional argument. Allows the user to specify the executable that solves the problem. `make` will be run on this executable. Default: `main`.
* `-n`/`--neigbours`: Optional argument, only used in simulated annealing. Allows the user to specify how many neighbours should be tried unsuccessfully before ending the execution of the algorithm. Default: 25.
* `-l`/`--lambda_exp`: Optional argument, only used in simulated annealing. Used as the `lambda` in the simulated annealing algorithm. A larger `lambda` means more stability, and a smaller `lambda` means more volatility (more likely to jump to a lower score). 
* `-g`/`--graph`: Optional argument, boolean. If provided, the program will show plots to visualize its execution. The random algorithm will produce a box plot representing the scores obtained. The simulated annealing algorithm will produce line plots showing the evolution of the score and each one of its parameters over the iterations.

## What is the example problem?

The example problem that was chosen to test this framework was the following:

```
The input file contains an integer number n, followed by n integer numbers x_1, ..., x_n. 
We want to generate a file with a subset of the input file maximizing the sum of its elements.
```

This problem is trivially solved by taking only the positive numbers. We took a different approach in order to test the algorithms: we defined a parameter `threshold`, which takes values in [-1500, 1500], and took the values greater than `threshold`. The optimal value for this parameter should be 0 or close to 0, so it will be easy to see if the algorithms reach the correct result. 

## Tips

* Name the input files `a`, `b`, `c`, `d`, `e`, `f` and place them in the `inputs` directory.
* Make sure that the `compute_score` function is implemented properly (test it against the judge system). A poorly implemented `compute_score` function will make the optimization meaningless.
* Simulated annealing will not work better than random if the score is not a continuous function of the parameters. An example of this would be to use one of the parameters as a random seed for the `C++` code. Since small changes to the parameter will result in completely different results, local search is not applicable. 
* In simulated annealing, if the program gets stuck in local minima easily, try using smaller `lambda` values. If it oscillates too much, try using larger `lambda` values.