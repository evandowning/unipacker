#!/bin/bash

# OUTPUTs samples that don't exist in binaries/ folder

if [[ $# -ne 2 ]]; then
    echo "usage: ./check_exit.sh samples.txt binaries/"
    exit 2
fi

fn="$1"
folder="$2"

while read LINE; do
    h=$(echo "$LINE" | rev | cut -d '/' -f 1 | rev)

    rv=`find $folder -type f -name $h`

    if [[ ! $rv ]]; then
        echo "NOT found: $LINE"
    fi

done < "$fn"
