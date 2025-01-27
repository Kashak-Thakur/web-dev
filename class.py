class A:
    def __init__(self) -> None:
        pass
    def Solve(self):
        print("hello")

class B(A):
    def __init__(self) -> None:
        super().__init__()

    def Solve(self):
        print("olleh")

var = B()
var.Solve()
#Inheritance 