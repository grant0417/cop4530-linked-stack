#!/bin/sh

INPUT_FILE="example_test_file"
OUTPUT_FILE="example_output_file"

FILE_DIFF=$(./main.py $INPUT_FILE | diff $OUTPUT_FILE -)

if [[ $FILE_DIFF ]]; then
  echo "Test failed"
else 
  echo "Test succeded"
fi

