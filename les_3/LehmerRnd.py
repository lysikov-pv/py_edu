import datetime

class LehmerRnd:
    a = 16807
    m = 2147483647
    q = 127773
    r = 2836
    seed = int(str(datetime.datetime.now().timestamp())[-5:])

    # def __init__(self, seed):
    #     self.seed = int(str(datetime.datetime.now().timestamp())[-5:])

    def Next(self, leftBound, rightBound):
        hi = int(self.seed / self.q)
        lo = int(self.seed % self.q)
        self.seed = int((self.a * lo) - (self.r * hi))
        if (self.seed <= 0):
            self.seed = self.seed + self.m
        x = (self.seed * 1.0) / self.m
        return (int)((rightBound - leftBound) * x + leftBound)