import sys
input = sys.stdin.readline


def inp():
    """For taking integer inputs."""
    return (int(input()))


def inlt():
    """For taking List inputs."""
    return (list(map(int, input().split())))


def insr():
    """ For taking string inputs. (list of characters)"""
    s = input()
    return (list(s[:len(s) - 1]))


def invr():
    """For taking space seperated integer variable inputs"""
    return (map(int, input().split()))

# 0 1 1 1 1 1 1 1 0
# 1 1 1 1 1 1 1 0 0
# 1 1 1 1 1 1 0 0 1
# 1 1 1 1 1 0 0 1 1
# 1 1 1 1 0 0 1 1 1
# 1 1 1 0 0 1 1 1 1
# 1 1 0 0 1 1 1 1 1
# 1 0 0 1 1 1 1 1 1
# 0 0 1 1 1 1 1 1 1


def main():
    lines = inp()
    print(lines)


main()
