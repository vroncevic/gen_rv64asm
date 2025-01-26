#!/bin/bash
#
# @brief   gen_rv64asm
# @version v1.0.0
# @date    Sat Jan 25 19:48:16 AM CEST 2025
# @company None, free software to use 2025
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

rm -rf htmlcov gen_rv64asm_coverage.xml gen_rv64asm_coverage.json .coverage
rm -rf new_simple_test/ full_simple/ latest/ empty_simple_test/
ats_coverage_run.py -n gen_rv64asm -p ../README.md
rm -rf new_simple_test/ full_simple/ latest/ empty_simple_test/
python3 -m coverage run -m --source=../gen_rv64asm unittest discover -s ./ -p '*_test.py' -vvv
python3 -m coverage html -d htmlcov
python3 -m coverage xml -o gen_rv64asm_coverage.xml 
python3 -m coverage json -o gen_rv64asm_coverage.json
python3 -m coverage report --format=markdown -m
