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
            rar a -v"${SIZE}m" "${rarname}" && break
            rarname="$rarname$((part++))"
        done
        cd $base_addr
    done
    
}

compress_data
