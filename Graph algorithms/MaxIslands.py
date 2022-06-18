class Graph:
    def __init__(self, rows, col, graph):
        self.row = rows
        self.col = col
        self.g = graph
        self.count = 1

    def isFree(self, i, j, visited):
        return (i >= 0 and i < self.row and j >= 0 and j < self.col and visited[i][j] == False and self.g[i][j])

    def DFS(self, i, j, visited):

        rowNeighbours = [-1, -1, -1, 0, 0, 1, 1, 1]
        colNeighbours = [-1, 0, 1, -1, 1, -1, 0, 1]

        visited[i][j] = True
        for ind in range(8):
            if self.isFree(i+rowNeighbours[ind], j+colNeighbours[ind], visited):
                self.count += 1
                self.DFS(i+rowNeighbours[ind], j +
                         colNeighbours[ind], visited)

    # def countIslands(self):
    #     count = 0
    #     visited = [[False for j in range(self.col)] for i in range(self.row)]
    #     for i in range(self.row):
    #         for j in range(self.col):
    #             if visited[i][j] == False and self.g[i][j] == 1:
    #                 self.DFS(i, j, visited)
    #                 count += 1
    #     return count

    def maxIslands(self):
        output = 0
        visited = [[False for j in range(self.col)] for i in range(self.row)]
        for i in range(self.row):
            for j in range(self.col):
                if visited[i][j] == False and self.g[i][j] == 1:
                    self.DFS(i, j, visited)
                    output = max(output, self.count)
        return output


row = int(input())
g = []
for i in range(row):
    rows = list(map(int, input().split()))
    g.append(rows)
col = len(rows)
g = Graph(row, col, g)
print(g.maxIslands())
