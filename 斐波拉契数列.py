class Fib_array:
    def __init__(self,last=0,curr=1):
        self.last=last
        self.curr=curr

    def __iter__(self):
        return self

    def next(self):
        if self.curr>10:
            raise Stop
        value=self.curr
        self.curr+=self.last+self.curr
        self.last=value
        return value

