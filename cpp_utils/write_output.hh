#ifndef __WRITE_OUTPUT__
#define __WRITE_OUTPUT__

#include "includes.hh"

// TODO: Modify the parameters to this function as desired and write to "out_temp.txt"
void write_output(vector<int>& chosen) {
    ofstream file("out_temp.txt");
    bool first = true;
    for (int x : chosen) {
        if (first) first = false;
        else file << " ";
        file << x;
    }
    file << endl;
}

#endif