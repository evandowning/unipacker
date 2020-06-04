#!/bin/bash

if [ $# -ne 2 ]; then
    echo "usage: ./write_commands.sh samples.txt output/"
    exit 2
fi

sampleFN=$1
output=$2

# Read in file
while read line;
do
    sha=$(echo "$line" | rev | cut -d '/' -f 1 | rev)

    echo "python single.py ${line} > ${output}/${sha}_stdout.txt 2> ${output}/${sha}_stderr.txt"

done < "$sampleFN"
