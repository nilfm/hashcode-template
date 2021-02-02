def compute_score(file_path):
    """
    TODO
    This function should return a numeric value which is
    the score of the output file at file_path
    """
    with open(file_path, "r") as f:
        nums = [int(x) for x in f.read().split()]
        return sum(nums)
