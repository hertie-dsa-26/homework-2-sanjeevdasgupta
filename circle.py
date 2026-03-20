class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def perimeter(self) -> float:
        return 2 * 3.14159 * self.radius
    
    def area(self) -> float:
        return 3.14159 * (self.radius**2)