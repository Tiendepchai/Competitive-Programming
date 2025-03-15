#! /bin/bash
#! /bin/python3
# Usage: ./run.sh filename.cpp or ./run.sh filename.py

file_name="$1"
program="${file_name%.*}"
file_type="${file_name##*.}"
inputf="inputf.in"
outputf="outputf.out"
path=$(pwd)

if [ "$file_type" == "cpp" ]; then
    g++ -std=c++20 "$file_name" -o "$program"
    if [ $? -eq 0 ]; then
        echo "CPP compiled successfully!"
        timeout 4s "./$program" < "$path/$inputf" > "$path/$outputf"
        echo "CPP executed!"
    else
        echo "CPP compilation failed!"
    fi
elif [ "$file_type" == "py" ]; then
    timeout 4s python3 "$file_name" < "$path/$inputf" > "$path/$outputf"
    if [ $? -eq 0 ]; then
        echo "Python executed!"
    else
        echo "Python execution failed!"
    fi
else
    echo "Wrong file type!"
fi
