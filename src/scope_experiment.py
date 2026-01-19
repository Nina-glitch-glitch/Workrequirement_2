# ============================================
# Exercise 3: Scoped Variables Experiment
# ============================================
# This script demonstrates how variable scope works in Python
# by comparing a global variable with a local variable inside
# a function and a loop.
# Based on my own testing after watching the Qybele video
# in Chapter 3.4 (Scopes).

# Global variable
foo = 100
print("Global foo at start:", foo)


def bar():
    # Local variable (inside function)
    foo = 50
    print("Local foo at start of function:", foo)

    # Loop inside the function
    for i in range(2):
        foo = foo + 1
        print("Local foo inside loop:", foo)

    # After the loop
    print("Local foo after loop:", foo)


# Call the function
bar()

# Back in global scope
print("Global foo after function:", foo)
