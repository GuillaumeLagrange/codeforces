import math
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


def main():
    n = inp()
    shortcuts = inlt()

    # print(n)
    # print(shortcuts)

    paths = [0]
    # Neighbor[i] = nodes that can reach i with a cost of 1
    graph = [[1]]

    for i in range(n-2):
        paths.append(math.inf)
        graph.append([i, i + 2])

    paths.append(math.inf)
    graph.append([n-2])

    for i in range(n):
        if i not in graph[shortcuts[i] - 1]:
            graph[shortcuts[i] - 1].append(i)

    for i in range(n):
        newPath = paths[i]

        # print('node', i)
        for neighbor in graph[i]:
            # print('neighbor', neighbor)
            # print(paths[neighbor])
            newPath = min(newPath, paths[neighbor] + 1)

        paths[i] = newPath

    # print(graph)
    # print(paths)
    print(' '.join(str(path) for path in paths))


main()
