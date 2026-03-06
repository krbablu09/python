import math

def circle_stats(radius):
    area = math.pi * radius ** 2 # use pi value in math.pi
    circumference = 2 * math.pi * radius
    return area, circumference
    print("hii") # return ke baad print nhi hota hai

a, c = circle_stats(3)

print("Area: ", a ,"\n" "Circumfarence: ", c  )