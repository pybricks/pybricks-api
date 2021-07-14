from micropython import const, opt_level, mem_info, qstr_info, stack_use

# Get stack at start.
stack_start = stack_use()

# Print REPL compiler optimization level.
print("level", opt_level())

# Print memory usage.
mem_info()

# Print memory usage and a memory map.
mem_info(True)

# Print interned string information.
qstr_info()

# Print interned string information and their names.
APPLES = const(123)
_ORANGES = const(456)
qstr_info(True)


def test_stack():
    return stack_use()


# Check the stack.
print("Stack diff: ", test_stack() - stack_start)
