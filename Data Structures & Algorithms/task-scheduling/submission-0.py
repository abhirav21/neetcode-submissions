class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        count= Counter(tasks)
        maxHeap = [-count[cnt] for cnt in count]
        
        heapq.heapify(maxHeap)
        q= deque()
        time =0
        while q or maxHeap:
            time +=1
            if maxHeap:
                node = 1+ heapq.heappop(maxHeap)
                if node:
                    q.append([node, time+n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time
        
                


                





       
        