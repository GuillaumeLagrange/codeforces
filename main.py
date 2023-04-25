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
    # reachableFrom[i] = nodes that can reach i with a cost of 1
    nodesFrom = [[1]]
    nodesTo = [[1]]

    for i in range(n-2):
        paths.append(math.inf)
        nodesFrom.append([i, i + 2])
        nodesTo.append([i, i + 2])

    paths.append(math.inf)
    nodesFrom.append([n - 2])
    nodesTo.append([n - 2])

    for i in range(n):
        nodeFrom = i
        nodeTo = shortcuts[i] - 1

        if nodeFrom not in nodesFrom[nodeTo]:
            nodesFrom[nodeTo].append(nodeFrom)

        if nodeTo not in nodesTo[nodeFrom]:
            nodesTo[nodeFrom].append(nodeTo)

    toVisit = nodesTo[0].copy()

    while len(toVisit) != 0:
        node = toVisit.pop()

        oldPath = paths[node]

        for neighbor in nodesFrom[node]:
            paths[node] = min(paths[node], paths[neighbor] + 1)

        if oldPath != paths[node]:
            for nextNode in nodesTo[node]:
                if paths[nextNode] > paths[node] + 1:
                    toVisit.append(nextNode)

    answer = ' '.join(str(path) for path in paths)
    print(answer)
    # print(answer == EXPECTED_4)


main()
