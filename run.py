#! /usr/bin/python3

import os, sys

try:
        file_name = sys.argv[1]
        program, file_type = map(str, file_name.split('.'))
        path = os.getcwd()
        inputf = 'inputf.in'
        outputf = 'outputf.out'
        if file_type == 'cpp':
                cpp = f"g++ -std=c++20 {file_name} -o {program} && timeout 4s ./{program}<{path}/{inputf}>{path}/{outputf}"
                try:
                        os.system(cpp)
                        print("CPP worked!")
                except:
                        print("CPP failed!")
        else:
                py = f"timeout 4s python3 {file_name} <{path}/{inputf}>{path}/{outputf}"
                try:
                        os.system(py)
                        print("Python worked!")
                except:
                        print("Python failed!")
except:
        print("Wrong file type!")
