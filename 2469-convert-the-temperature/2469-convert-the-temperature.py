class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        # new = []
        # new.append(celsius+ 273.15)
        # new.append(celsius * 1.80 + 32.00)
        # return new     
        return [celsius+ 273.15,celsius * 1.80 + 32.00]   