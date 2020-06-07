def calculate_vat(amount):
    total = amount*1.2
    return total

print(calculate_vat(100))
import turtle
turtle.speed('slowest')
length = 200
angle = 90
angle_one = 240
glass_side = 45
door_distance = 75
def colour():
    turtle.color('brown', 'gold')
    turtle.begin_fill()
    turtle.end_fill()

for house in range(4):
    colour()
    turtle.forward(length)
    turtle.right(angle)

for triangle in range(3):

    turtle.forward(length)
    turtle.right(angle_one)

def window():
    for glass in range(4):
        turtle.forward(glass_side)
        turtle.right(angle)
    print(glass)


window()
turtle.forward(length-glass_side)
window()
turtle.forward(glass_side)
turtle.right(angle)
turtle.forward(length)
turtle.right(angle)
turtle.forward(door_distance)
window()

turtle.done()

