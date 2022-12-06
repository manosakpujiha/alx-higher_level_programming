#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        uno = int(argv[1])
        dos = int(argv[3])
        if argv[2] == '+':
            print("{:d} + {:d} = {:d}".format(uno, dos, add(uno, dos)))
        elif argv[2] == '-':
            print("{:d} - {:d} = {:d}".format(uno, dos, sub(uno, dos)))
        elif argv[2] == '*':
            print("{:d} * {:d} = {:d}".format(uno, dos, mul(uno, dos)))
        elif argv[2] == '/':
            print("{:d} / {:d} = {:d}".format(uno, dos, div(uno, dos)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
