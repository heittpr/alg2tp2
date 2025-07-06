#!/bin/sh

TP2="./bin/tp2"
TIMEOUT="30.1m"
TESTS="data/tests"

echo "solver,testcase,answer,time,memory"

for solver in "greedy" "fptas 0.2" "fptas 0.1" "fptas 0.05" "bnb"; do
  for input in "$TESTS/"*; do
    testcase=$(basename "$input")
    output=$(timeout "$TIMEOUT" "$TP2" $solver < "$input") || output=",,"
    echo "$solver,$testcase,$output"
  done
done
