#classe com um número e sua incerteza
class uNum:
    def __init__(self, value, error=0) -> None:
        self.value = value
        if(error < 0):
            raise ValueError("Error can't be less than 0")
        self.error = abs(error)

    def __str__(self) -> str:
        return f"{self.value} ± {self.error}"
    
    def __add__(self, other):
        newUnum=0
        if type(other) == int or type(other) == float:
            newUnum = uNum(self.value + other, self.error)
            
        else:
            newUnum = uNum(self.value + other.value, self.error + other.error)
        return newUnum
    def __sub__(self, other):
        newUnum=0
        if type(other) == int or type(other) == float:
            newUnum = uNum(self.value - other, self.error)
            
        else:
            newUnum = uNum(self.value - other.value, self.error + other.error)
        return newUnum
    
    def __mul__(self, other):
        newUnum=0
        if type(other) == int or type(other) == float:
            newUnum = uNum(self.value * other, self.error * abs(other))
            
        else:
            newUnum = uNum(self.value * other.value, abs(self.error*other.value) + abs(self.value* other.error))
        return newUnum
    
    def __truediv__(self, other):
        newUnum=0
        if type(other) == int or type(other) == float:
            newUnum = uNum(self.value / other, self.error / abs(other))
            
        else:
            newUnum = uNum(self.value / other.value, (abs(self.error*other.value) + abs(self.value* other.error))/abs(other.value**2))
        return newUnum
    
    def __pow__(self, other):
        newUnum = uNum(self.value**other, abs(other*self.value**(other-1)*self.error))
        return newUnum

