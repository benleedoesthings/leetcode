class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        ans = {}
        times = [(time, server_id) for server_id, time in logs]
        times.sort()
        sorted_q = sorted(queries)

        active = defaultdict(int)
        i = 0
        j = 0
        k = 0 # goal: match sorted_q[k]
        while k < len(sorted_q):
            while j < len(times) and times[j][0] <= sorted_q[k]:
                active[times[j][1]] += 1
                j += 1
            
            while i <= j and i < len(times) and times[i][0] < sorted_q[k] - x:
                active[times[i][1]] -= 1
                if active[times[i][1]] <= 0:
                    del active[times[i][1]]

                i += 1

            ans[sorted_q[k]] = n - len(active)

            k += 1
        
        ans_arr = []
        for i in range(len(queries)):
            ans_arr.append(ans[queries[i]])

        return ans_arr