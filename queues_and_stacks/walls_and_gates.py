from collections import deque


class Solution:
    def wallsAndGates(self, rooms):

        if rooms and len(rooms) > 0:
            row_count = len(rooms)
            col_count = len(rooms[0])

            def add_distance(r, c, queue, distance):
                if r >= 0 and c >= 0 and r < row_count and c < col_count and rooms[r][c] > distance:
                    queue.append((r, c, distance))
                    rooms[r][c] = distance

            queue = deque()

            for rIdx in range(row_count):
                for cIdx in range(col_count):
                    if rooms[rIdx][cIdx] == 0:
                        queue.append((rIdx, cIdx, 0))

            while queue:
                r, c, distance = queue.popleft()
                distance += 1
                add_distance(r, c + 1, queue, distance)
                add_distance(r, c - 1, queue, distance)
                add_distance(r + 1, c, queue, distance)
                add_distance(r - 1, c, queue, distance)
