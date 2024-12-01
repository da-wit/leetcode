class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse = True)
        m =0
        for i in range(len(processorTime)):
            m =max(m,processorTime[i] + max(tasks[i*4:i*4+4]))
        return m