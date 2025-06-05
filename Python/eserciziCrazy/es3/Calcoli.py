
class Calcoli:
    #constructor
    def __init__(self, first, second):
        self.first = first
        self.second = second

    #methods
    def add(self):
        result = self.first + self.second
        return result;
    
    def sub(self):
        result = self.first - self.second
        return result;
    
    def molt(self):
        result = self.first * self.second
        return result;

    def div(self):
        result = self.first / self.second
        return result;