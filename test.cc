#include "cpp_utils/includes.hh"
#include "cpp_utils/read_data.hh"
#include "cpp_utils/write_output.hh"

int main(int argc, char** argv) {
    if (argc != 2) {
        cout << "Usage:   ./test <input_file_name>" << endl;
        cout << "Example: ./test a" << endl;
        return 1;
    }

    string name = argv[1];
    string input_path = "inputs/" + name;
    read_data(input_path);
    // TODO
}