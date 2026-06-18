from collections import deque

def astar(start, goal):

    queue = deque()

    queue.append((start, [start]))

    visited = set()

    while queue:

        current, path = queue.popleft()

        if current == goal:

            return path

        if current in visited:

            continue

        visited.add(current)

        x, y = current

        neighbors = [

            (x + 1, y),
            (x - 1, y),
            (x, y + 1),
            (x, y - 1)

        ]

        for nx, ny in neighbors:

            if 0 <= nx < 10 and 0 <= ny < 10:

                queue.append(
                    ((nx, ny), path + [(nx, ny)])
                )

    return []