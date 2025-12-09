class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n  
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  
        return self.parent[x]
    
    def union(self,x,y):
        dadx = self.find(x)
        dady = self.find(y)

        if dadx == dady:
            return
        
        if self.rank[dadx] > self.rank[dady]:
            self.parent[dady] = dadx 
        elif self.rank[dadx] < self.rank[dady]:
            self.parent[dadx] = dady
        else:
            self.parent[dady] = dadx
            self.rank[dadx] += 1 
        return True
    
def numIslands2(m: int, n: int, positions: list[list[int]]) -> list[int]:
    uf = UnionFind( m * n )
    active = [False] * ( m * n )
    results = []
    regions = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for r, c in positions:
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
                if uf.union(idx, n_index):
                    regions -= 1

        results.append(regions)
    
    return results

m = 3
n = 3
activations = [(0, 0), (0, 1), (1, 2), (2, 1), (1, 1)]  # Example activations

print(numIslands2(m, n, activations))

