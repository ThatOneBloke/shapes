import pgzrun
def draw():
    screen.clear()
    screen.fill("white")
    screen.draw.circle((200, 400), 50, "yellow")
    screen.draw.filled_circle((100, 200), 50, "yellow")
    rectangle1 = Rect((100, 50), (50, 100))
    screen.draw.rect(rectangle1, "green")
    rectangle2 = Rect((50, 100), (100, 50))
    screen.draw.filled_rect(rectangle2, "green")
    screen.draw.line((20, 20), (50, 50), "black")
    screen.draw.text(("hello"), (400, 50), color = "blue", background = "yellow")

pgzrun.go()