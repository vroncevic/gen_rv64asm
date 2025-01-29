#
# @brief   full_simple
# @version 1.0.0
# @date    2025-01-29
# @company None, free software to use 2025
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

.global _start

.section .data
message:
    .asciz "Hello, RISC-V without glibc!\n"
    len = . - message

.section .text
_start:
    # Syscall: write(int fd, const void *buf, size_t count)
    li a7, 64          # Load the syscall number for write (64) into a7
    li a0, 1           # File descriptor 1 (stdout)
    la a1, message     # Load address of the message into a1
    li a2, len         # Load the length of the message into a2
    ecall              # Invoke the syscall

    # Syscall: exit(int status)
    li a7, 93          # Load the syscall number for exit (93) into a7
    li a0, 0           # Exit status 0 (success)
    ecall              # Invoke the syscall
