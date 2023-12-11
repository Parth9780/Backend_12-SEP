# Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle

class Circle:
    def area(self, r):
        area = 3.14*r*r
        print(area)
    
    def perimeter(self,r):
        pi = 3.14
        area = pi * pi *r
        print(area)

ci = Circle()

redius = int(input("Enter the redius :"))

ci.area(redius)
ci.perimeter(redius)
