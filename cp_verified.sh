#!/bin/bash

if [[ $# -ne 3 ]]; then
    echo "usage: ./cp_verified.sh verified_unipacker.txt old/ new/"
    exit 2
fi

fn="$1"
old="$2"
new="$3"

while read LINE; do
    oldpath=`find $old -type f -name $LINE`
    f=$(echo "$oldpath" | rev | cut -d '/' -f 2 | rev)
    newpath="$new/$f"

    echo "$oldpath -> $newpath/$LINE"

    mkdir -p $newpath
#   cp $oldpath $newpath/$LINE
    break
done < "$fn"
