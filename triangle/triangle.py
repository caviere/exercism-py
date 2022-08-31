def equilateral(sides):
    a, b, c = sides[0], sides[1], sides[2]
    return triangle(sides) and a == b == c 


def isosceles(sides):
    a, b, c = sides[0], sides[1], sides[2]
    return triangle(sides) and (a == b or a == c or b == c)


def scalene(sides):
    a, b, c = sides[0], sides[1], sides[2]
    return triangle(sides) and a != b and b != c and a !=c

def degenerate(sides):
    a, b, c = sides[0], sides[1], sides[2]
    return triangle(sides) and a + b == c or a + c == b or b + c == a
 
def triangle(sides):
    a, b, c = sides[0], sides[1], sides[2]
    return a > 0 and b>0 and c>0 and a + b >= 0 and a + c >= 0 and b + c >=0