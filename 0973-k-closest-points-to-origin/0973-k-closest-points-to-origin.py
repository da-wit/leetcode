class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def lala(num):
            y = num[0]**2 + num[1]**2
            return y
        
        m = {}
        for i in range(len(points)):
            m[i] = lala(points[i])
        print(m)

        x = sorted(m.items(), key=lambda x:x[1])
        print(x)
        z = []
        for key ,val in x:
            if len(z)<k:
                z.append(points[key])
        return z


        