class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        """
4: {2}
1: {2, 3}
2: {1}

x=2
n=3
find all b/t [3-2, 3] -> 1 and 3 inclusive

1: {2, 3}
2: {1}
3: {}

Set: {1, 2, 3}
len(set) == 3
n - len(set) = 3 - 3 = 0
answered 


[3, 1] -> 1
[5, 1] -> 1
[6, 2] -> 2

Between [5, 6] how many servers received requests? 2
(2 - 1) + 1 

[1, 2] i
[1, 3] 
[2, 1] j
[4, 2]

Between [1, 3]? Ans: 3
        """
        ans = {}
        times = [(time, server_id) for server_id, time in logs]
        times.sort()
        sorted_q = sorted(queries)

        #print(times)

        active = defaultdict(int)
        i = 0
        j = 0
        k = 0 # goal: match sorted_q[k]
        while k < len(sorted_q):
            #print("looking for", sorted_q[k] - x, sorted_q[k])

            while j < len(times) and times[j][0] <= sorted_q[k]:
                active[times[j][1]] += 1
                j += 1
                #print("j is now", j)

            #print(active)
            
            while i <= j and i < len(times) and times[i][0] < sorted_q[k] - x:
                #print("removing", i)
                active[times[i][1]] -= 1
                if active[times[i][1]] <= 0:
                    del active[times[i][1]]

                i += 1

            #print("i j are", i, j)
            #print("active", active)
            ans[sorted_q[k]] = n - len(active)

            k += 1
        
        #print(ans)
        ans_arr = []
        for i in range(len(queries)):
            ans_arr.append(ans[queries[i]])

        return ans_arr