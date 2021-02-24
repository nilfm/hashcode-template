#include "cpp_utils/includes.hh"
#include "cpp_utils/read_params.hh"
#include "cpp_utils/read_data.hh"
#include "cpp_utils/write_output.hh"

int main(int argc, char** argv) {
    map<string, double> p = read_params(argc, argv);
    read_data(argv[1]);

    // TODO: Modify this section
    vector<int> chosen;
    for (int x : nums) {
        if (x >= p["threshold"]) {
            chosen.push_back(x);
        }
    }

    // TODO: Modify the parameters to write_output as desired
    write_output(chosen);
}