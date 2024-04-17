#!/bin/bash

# Directory containing the folders to compress
ROOT_DIR="data/"

# Size of each part in MB
SIZE=100

# Folder structure
STRUCTURE="*/*/"

# Function to compress a directory into RAR parts
compress_data() {
    for container in "$ROOT_DIR"*/*/; do
        local folder="$1"
        #local rarname="${folder##*/}.part"
        local part=1
        local rarname="$(basename "$container").part"
        local base_addr=$(pwd)

        cd $container
        echo "Packaging data $rarname"
        while true; do
            rar a -v"${SIZE}m" "${rarname}.rar" && break
            rarname="$rarname$((part++))"
        done
        cd $base_addr
    done
    
}

exctract_data () {
    for container in "$ROOT_DIR"*/*/; do
        local folder="$1"
        #local rarname="${folder##*/}.part"
        local part=1
        local rarname="$(basename "$container").part"
        local base_addr=$(pwd)

        cd $container
        echo "Packaging data $rarname"
        while true; do
            unrar x $rarname && break
            rarname="$rarname$((part++))"
        done
        cd $base_addr
    done
    
}

if [ "$1" == "compress" ]; then
    compress_data
elif [ "$1" == "extract" ]; then
    exctract_data
else
    echo "Usage: $0 [compress|extract]"
    exit 1
fi