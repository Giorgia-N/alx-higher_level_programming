#!/usr/bin/python3
if __name__ == "__main__":
    """Print the result of the addition of all arguments."""
    import system

    total = 0
    for i in range(len(system.argv) - 1):
        total += int(system.argv[i + 1])
    print("{}".format(total))
