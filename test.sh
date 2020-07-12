#!/bin/sh

TEST_FILE="example_test_file"
OUTPUT_FILE="example_output_file"

PROGRAM_OUTPUT=$(./main.py $TEST_FILE)
PROGRAM_SUCCESS=$?

FILE_DIFF=$(echo "$PROGRAM_OUTPUT" | diff - $OUTPUT_FILE)

if [ "$FILE_DIFF" ] || [ $PROGRAM_SUCCESS != 0 ]; then
  echo "Test failed"
  echo "$FILE_DIFF"
  exit 1
else 
  echo "Test succeeded"
fi

