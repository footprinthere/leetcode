# https://www.acmicpc.net/problem/5214

from sys import stdin
from collections import defaultdict, deque


def main():
    n_stations, _, n_tubes = (int(t) for t in stdin.readline().split())
    graph = Graph(n_stations=n_stations, n_tubes=n_tubes)
    for i in range(1, n_tubes + 1):
        graph.add_connection(i, [int(t) for t in stdin.readline().split()])

    print(graph.bfs(start=1, end=n_stations))


class Graph:
    def __init__(self, n_stations: int, n_tubes: int):
        self.n_stations = n_stations
        self.n_tubes = n_tubes

        self.stations: defaultdict[int, list[int]] = defaultdict(list)
        self.tubes: list[list[int]] = [[]]  # padding for 1-indexing

    def add_connection(self, idx: int, connection: list[int]):
        # station -> tube
        for v in connection:
            self.stations[v].append(idx)
        # tube -> station
        self.tubes.append(connection)

    def bfs(self, start: int, end: int) -> int:
        # Special case
        if start == end:
            return 1

        stations_queue = deque([(start, 1)])
        stations_visited = [False] * (self.n_stations + 1)
        stations_visited[start] = True
        tubes_visited = [False] * (self.n_tubes + 1)

        while stations_queue:
            u, d = stations_queue.popleft()

            for t in self.stations[u]:
                if tubes_visited[t]:
                    continue
                tubes_visited[t] = True

                for v in self.tubes[t]:
                    if v == end:
                        return d + 1
                    if stations_visited[v]:
                        continue

                    stations_visited[v] = True
                    stations_queue.append((v, d + 1))

        return -1  # not reachable


if __name__ == "__main__":
    main()
