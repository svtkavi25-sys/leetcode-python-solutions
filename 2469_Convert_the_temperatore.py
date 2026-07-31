class Solution(object):
    def convertTemperature(self, celsius):
        new=[]
        new.append(celsius+273.15)
        new.append(celsius*1.80+32.00)
        return new
        