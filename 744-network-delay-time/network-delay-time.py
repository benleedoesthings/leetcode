class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        adj = [[] for i in range(n+1)]
        for u, v, w in times:
            # value, cost
            adj[u].append((v, w))

        dists = {}
        heap = []
        ans = -1

        first_node = (0, k)
        heapq.heappush(heap, first_node)

        while heap and len(dists) < n:
            dist, curr = heapq.heappop(heap)
            if curr not in dists:
                dists[curr] = dist
                ans = max(ans, dist)
                
                for child, cost in adj[curr]:
                    if child not in dists:
                        heapq.heappush(heap, (cost + dist, child))

        if len(dists) != n:
            return -1

        return -1 if ans == 0 else ans