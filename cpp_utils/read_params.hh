#ifndef __READ_PARAMS__
#define __READ_PARAMS__

#include <bits/stdc++.h>
using namespace std;

map<string, double> read_params(int argc, char** argv) {
    map<string, double> res;
    // Start from 2 because args start with executable and data path
    for (int i = 2; i < argc; i += 2) {
        // Debug information 
        // cout << argv[i] << " -> " << argv[i+1] << endl;
        string key = argv[i];
        double val = stod(argv[i+1]);
        res[key] = val;
    }
    return res;
}

#endif