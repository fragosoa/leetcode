print("hello world")

class A:
    def __init__(self, x):
        self.x = x

    def __str__(self):
        return f"A({self.x})"

    def __repr__(self):
        return f"A({self.x})"
    
    def __add__(self, other):
        if isinstance(other, A):
            return A(self.x + other.x)
        return NotImplemented
    
class B(A):
    def __init__(self, x):
        super().__init__(x)

    def __str__(self):
        return f"B({self.x})"

    def __repr__(self):
        return f"B({self.x})"
    

    
def test_addition():
    a1 = A(5)
    a2 = A(10)
    result = a1 + a2
    assert result.x == 15, f"Expected 15, got {result.x}"
    print("Test passed!")
if __name__ == "__main__":
    test_addition()
    print("All tests passed!")
    print(A(5) + A(10))  # Should print A(15)
    print(A(5))          # Should print A(5)
    print(repr(A(5)))    # Should print A(5)
    print(str(A(5)))     # Should print A(5)
    print("End of script")
    b1 = B(3)
    b2 = B(7)
    print(b1 + b2)  # Should print A(10) since B inherits from A
    print(b1)       # Should print B(3)
    print(repr(b1))  # Should print B(3)
    print(str(b1))   # Should print B(3)
    print("End of main")



