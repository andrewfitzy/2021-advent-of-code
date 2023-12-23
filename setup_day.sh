#!/bin/bash

# Ask for the day
read -p 'Challenge Day: ' day

echo Initialising solution and test folder for day $day

# Copy the two directories and rename to contain the day
cp -R ./src/Dayxx ./src/Day$day
cp -R ./tests/Dayxx ./tests/Day$day

# Then we'll replace xx in the test files with the day number
sed -i '' "s/xx/$day/g" ./tests/Day$day/test_Task01.py
sed -i '' "s/xx/$day/g" ./tests/Day$day/test_Task02.py