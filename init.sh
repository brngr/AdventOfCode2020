#!/bin/bash
touch "solution.py"
for i in {1..24}
do
   mkdir "Day$i"
   cp "./Day0/solution.py" "./Day$i/"
done