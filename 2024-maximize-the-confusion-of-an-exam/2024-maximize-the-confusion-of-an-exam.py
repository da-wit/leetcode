class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        l=0
        d=defaultdict(int)
        m=0
        res=0
        for r in range(len(answerKey)):
            d[answerKey[r]]+=1
            m=max(m,d[answerKey[r]])
            if r -l +1 -m > k:
                d[answerKey[l]]-=1
                l+=1
            res=max(res,r-l+1)
        return res
            