main: main.cc cpp_utils/*
	g++ main.cc -o main -O2

main_debug: main.cc cpp_utils/*
	g++ main.cc -o main -O0 -g

clean:
	rm -f main
	rm -f main_debug

ultraclean:
	rm -f main
	rm -f main_debug
	rm -f outputs/*
	rm -f code.zip