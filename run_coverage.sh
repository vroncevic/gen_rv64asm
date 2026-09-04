#!/bin/bash
#
# @brief   gen_rv64asm
# @version 2.0.0
# @date    Fri Sep 04 07:35:10 2026
# @company None, free software to use 2026
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

python3 coverage/ats_coverage.py gen_rv64asm
pylint gen_rv64asm > gen_rv64asm.report
echo "Done"
