#!/bin/bash

if [[ $# -ne 3 ]]; then
    echo "usage: ./cp_verified_exist.sh check_exist_output.txt new/"
    exit 2
fi

fn="$1"
old="$2"
new="$3"

while read LINE; do
    oldpath="$LINE"
    h=$(echo "$oldpath" | rev | cut -d '/' -f 1 | rev)
    f=$(echo "$oldpath" | rev | cut -d '/' -f 2 | rev)
    newpath="$new/$f"

    echo "$oldpath -> $newpath/$h"

    mkdir -p $newpath
    cp $oldpath $newpath/$h
done < "$fn"
