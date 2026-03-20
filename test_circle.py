from circle import Circle

# perimeter unit test
assert round(Circle(radius=10).perimeter(),2) == 62.83
assert round(Circle(radius=5).perimeter(),2) == 31.42
assert round(Circle(radius=1).perimeter(),2) == 6.28
print("All perimeter tests passed!")

# area unit test
assert round(Circle(radius=10).area(),2) == 314.16
assert round(Circle(radius=5).area(),2) == 78.54
assert round(Circle(radius=1).area(),2) == 3.14
print("All area tests passed!")