class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = {}

        for task in tasks:
            counts[task] = counts.get(task, 0) + 1

        q = deque()
        heap = []
        time = 0

        for count in counts:
            heap.append(-counts[count])

        heapq.heapify(heap)

        while heap or q:
            time += 1

            if heap:
                cur = heapq.heappop(heap) + 1

                if cur != 0:
                    q.append((cur, time + n))

            if q:
                if q[0][1] == time:
                    cur = q.popleft()
                    heapq.heappush(heap, cur[0])

        return time


        