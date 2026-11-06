class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        adj = [[] for i in range(n+1)]
        for u, v, w in times:
            # value, cost
            adj[u].append((v, w))

        print(adj)

        dists = {}
        heap = []
        ans = -1

        first_node = (0, k)
        heapq.heappush(heap, first_node)

        while heap:
            dist, curr = heapq.heappop(heap)
            if curr not in dists:
                dists[curr] = dist
                ans = max(ans, dist)
                #print("Shortest path to", curr, "is", dist)
                #print(heap)

                #print("Is", curr, "in adj?", curr in adj)
                
                for child, cost in adj[curr]:
                    #print("cost is", cost, "child is", child)
                    if child not in dists:
                        #print(child, ": adding", cost, "to", dist)
                        heapq.heappush(heap, (cost + dist, child))

        #print(dists)

        if len(dists) != n:
            return -1

        return -1 if ans == 0 else ans