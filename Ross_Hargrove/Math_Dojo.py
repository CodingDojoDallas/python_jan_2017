class MathDojo(object):
    def __init__(self):
        self.result = 0
    def add(self, *x):
        for value in x:
            if type(value) is list:
                for number in value:
                    self.result+=number
            else:
                self.result+=value
        return self
    def subtract(self, *y):
        for value in y:
            if type(value) is list:
                for number in value:
                    self.result-=number
            else:
                self.result-=value
        return self

md = MathDojo().add(2).add(2, 5).subtract(3, 2).result
md2 = MathDojo().add([1],3,4).add([3,5,7,8],[2,4.3,1.25]).subtract(2,[2,3],[1.1,2.3]).result

print md
print md2