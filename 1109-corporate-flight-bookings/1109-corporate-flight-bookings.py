class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        d =[0]*(n+2)
        for i in range(len(bookings)):
            d[bookings[i][0]]+=bookings[i][-1]
            d[bookings[i][1]+1]-=bookings[i][-1]
        pre = [0]*(n+1)
        # print(d)
        for i in range(1,len(pre)):
            pre[i] = d[i]+pre[i-1]
        # print(pre)
        return pre[1:]

            
