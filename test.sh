#!/bin/sh

TP2="./bin/tp2"
TIMEOUT="30.1m"
TESTS="tests"

echo "solver,testcase,expected,answer,time,memory"

for solver in "greedy" "fptas 0.2" "fptas 0.1" "fptas 0.05" "bnb"; do
  for input in "$TESTS/"*.in; do
    testcase=$(basename "$input" .in)
    expected=$(cat "$TESTS/$testcase.out")
    output=$(timeout "$TIMEOUT" "$TP2" $solver < "$input") || output=",,"

    echo "$solver,$testcase,$expected,$output"
  done
done
