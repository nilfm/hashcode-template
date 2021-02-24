#ifndef __READ_DATA__
#define __READ_DATA__

#include "includes.hh"

// TODO: Declare variables to hold the input data
vector<int> nums;

// TODO: Function to read input and store in the previous variables
void read_data(const string& path) {
    ifstream infile(path);
    int sz;
    infile >> sz;
    nums = vector<int>(sz);
    for (int& x : nums) infile >> x;
}

#endif