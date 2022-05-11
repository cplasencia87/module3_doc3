def square_footage():
    legnth = int(input('Legnth? '))
    width = int(input('Width? '))
    area = legnth * width
    return f' area is {area}'




def circumference():
    from math import pi
    rad = int(input('What is the radius? '))
    circ = 2*pi*rad
    return f'The circumference is {circ}'

