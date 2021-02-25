main: main.cc cpp_utils/*
	g++ main.cc -o main -O2

main_debug: main.cc cpp_utils/*
	g++ main.cc -o main -O0 -g

test: test.cc cpp_utils/*
	g++ test.cc -o test

zip: main.cc *.py optimizer/* cpp_utils/* 
	zip code.zip -r main.cc *.py optimizer cpp_utils

clean:
	rm -f main
	rm -f main_debug
	rm -f test

ultraclean:
	rm -f main
	rm -f main_debug
	rm -f outputs/*
	rm -f out_temp.txt
	rm -f code.zip
	rm -f test