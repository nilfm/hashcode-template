def compute_score(input_path, output_path):
    """
    TODO
    This function should return a numeric value which is
    the score of the output file at file_path
    """
    with open(output_path, "r") as f:
        nums = [int(x) for x in f.read().split()]
        return sum(nums)
