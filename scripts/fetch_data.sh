#!/bin/bash

# Define the URL to download the titanic dataset
URL="https://www.openml.org/data/get_csv/16826755/phpMYEkMl.csv"

# Define the destination folder to download the dataset
DEST_FOLDER="./model/datasets"

# Remove old files if they exist
if [ -f "$DEST_FOLDER/train.csv" ]; then
    rm "$DEST_FOLDER/train.csv"
fi
if [ -f "$DEST_FOLDER/test.csv" ]; then
    rm "$DEST_FOLDER/test.csv"
fi

# Download the CSV file
wget "$URL" -O "$DEST_FOLDER/titanic.csv"

# Relative path to the original CSV and output CSVs
ORIGINAL_CSV="$DEST_FOLDER/titanic.csv"
TRAIN_CSV="$DEST_FOLDER/train.csv"
TEST_CSV="$DEST_FOLDER/test.csv"

# Length of dataset
TOTAL_LINES=$(wc -l < "$ORIGINAL_CSV")
TRAIN_LINES=$((TOTAL_LINES * 80 / 100))

# Shuffle the dataset lines randomly
awk 'BEGIN {srand()} {print rand(), $0}' "$ORIGINAL_CSV" | sort -n | cut -d ' ' -f 2- > shuffled.csv

# Use awk to split the shuffled CSV file into two files
awk -v train_lines="$TRAIN_LINES" 'NR <= train_lines { print > "'"$TRAIN_CSV"'" } NR > train_lines { print > "'"$TEST_CSV"'" }' shuffled.csv
rm shuffled.csv
