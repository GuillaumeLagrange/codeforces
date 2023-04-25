import math
import sys
input = sys.stdin.readline


EXPECTED_4 = "0 1 2 3 4 5 6 7 8 8 7 6 5 4 3 2 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 4 4 5 6 5 6 7 8"


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

    while True:
        newIteration = paths.copy()

        for i in range(n):
            newPath = newIteration[i]

            for neighbor in graph[i]:
                newPath = min(newPath, newIteration[neighbor] + 1)

            newIteration[i] = newPath

        if newIteration == paths:
            break

        paths = newIteration

    # wrong = 10
    # print(graph[wrong])
    # print(paths[wrong])
    answer = ' '.join(str(path) for path in paths)
    # print('#######')
    print(answer)
    # print(answer == EXPECTED_4)


main()
