class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return False
        if self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        elif self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1
        return True

def num_regions(n, activations):
    dsu = DSU(n * n) 
    active = [False] * (n * n)
    regions = 0
    results = []
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for r, c in activations:
        idx = r * n + c
        if active[idx]:
            results.append(regions)
            continue
        active[idx] = True
        regions += 1

        for drow, dcol in directions:
            nr, nc = r + drow, c + dcol
            n_index = nr * n + nc
            if 0 <= nr < n and 0 <= nc < n and active[n_index]:
                if dsu.union(idx, n_index):
                    regions -= 1

        results.append(regions)
    
    return results

# Grid of size 3x3
grid_size = 3
activations = [(0, 0), (0, 1), (1, 2), (2, 1), (1, 1)]  # Example activations

print(num_regions(grid_size, activations))
