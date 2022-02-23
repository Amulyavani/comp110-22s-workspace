"""Describe your scene program."""

__author__ = "730407531"

from turtle import Turtle, colormode, done


def main() -> None:
    """The entrypoint of my scene."""
    turtle_buddy: Turtle = Turtle()
    scene = turtle_buddy.getscreen()
    colormode(255)
    scene.bgcolor(147, 199, 209)
    turtle_buddy.speed(50)
    draw_house(turtle_buddy, 50.0, 20.0, 150.0)
    draw_roof(turtle_buddy, 50.0, 20.0, 150.0)
    draw_sun(turtle_buddy, 250.0, 150.0, 80.0)
    draw_sunrays(turtle_buddy, 250.0, 140.0, 90.0)
    draw_sunrays(turtle_buddy, 250.0, 130.0, 100.0)
    draw_sunrays(turtle_buddy, 250.0, 120.0, 110.0)
    draw_sunrays(turtle_buddy, 250.0, 110.0, 120.0)
    draw_door(turtle_buddy, 100.0, -55.0, 50.0, 75.0)
    draw_ground(turtle_buddy, -390.0, -320.0, 780.0, -190.0)
    draw_window(turtle_buddy, 150.0, 2.0, 35.0)
    draw_window(turtle_buddy, 167.5, -15.0, 17.5)
    draw_window(turtle_buddy, 167.5, 2.0, 17.5)
    draw_window(turtle_buddy, 150.0, -15.0, 17.5)
    draw_window(turtle_buddy, 150.0, 2.0, 17.5)
    draw_window(turtle_buddy, 65.0, 2.0, 35.0)
    draw_window(turtle_buddy, 82.5, 2.0, 17.5)
    draw_window(turtle_buddy, 82.5, -15.0, 17.5)
    draw_window(turtle_buddy, 65.0, 2.0, 17.5)
    draw_window(turtle_buddy, 65.0, -15.0, 17.5)
    done()


def draw_house(a: Turtle, x: float, y: float, width: float) -> None:
    """Draw a square of the given width whose top-left corner is located at x, y."""
    a.pencolor(101, 59, 30)
    a.fillcolor(240, 240, 212)
    
    a.penup()
    a.goto(x, y)
    a.pendown()
    
    a.begin_fill()
    
    a.speed(50)
    
    i: int = 0
    while i < 4:
        a.forward(width)
        a.right(90)
        i = i + 1

    a.end_fill()


def draw_roof(b: Turtle, x: float, y: float, side_length: float) -> None:
    """Draw a triangle of the given side length whose bottom-left corner is located at x, y."""
    b.pencolor(118, 21, 21)
    b.fillcolor(190, 83, 52)

    b.penup()
    b.goto(x, y)
    b.pendown()

    b.begin_fill()

    b.speed(50)

    i: int = 0
    while i < 3:
        b.forward(side_length)
        b.left(120)
        i = i + 1
    
    b.end_fill()


def draw_sun(c: Turtle, x: float, y: float, radius: float) -> None:
    """Draw a circle of the given radius whose starting point is located at x, y."""
    c.pencolor(251, 143, 67)
    c.fillcolor(249, 239, 35) 

    c.penup()
    c.goto(x, y)
    c.pendown()

    c.begin_fill()

    c.speed(50)

    c.circle(radius)

    c.end_fill()


def draw_door(d: Turtle, x: float, y: float, width: float, height: float) -> None:
    """Draw a rectangle of the given width and height whose starting point is located at x, y."""
    d.pencolor(114, 73, 53)
    d.fillcolor(139, 108, 64)

    d.penup()
    d.goto(x, y)
    d.pendown()

    d.begin_fill()

    d.speed(50)

    i: int = 0
    while i < 2:
        d.forward(width)
        d.right(90)
        d.forward(height)
        d.right(90)
        i = i + 1
    
    d.end_fill()


def draw_ground(e: Turtle, x: float, y: float, width: float, height: float) -> None:
    """Draw a rectangle of the given width and height whose starting point is located at x, y."""
    e.pencolor(50, 118, 21)
    e.fillcolor(160, 198, 143)

    e.penup()
    e.goto(x, y)
    e.pendown()

    e.begin_fill()

    e.speed(50)

    i: int = 0
    while i < 2:
        e.forward(width)
        e.right(90)
        e.forward(height)
        e.right(90)
        i = i + 1
    
    e.end_fill()


def draw_window(f: Turtle, x: float, y: float, width: float) -> None:
    """Draw a square of the given width whose starting point is located at x, y."""
    f.pencolor(101, 59, 30)
    f.fillcolor(197, 225, 241)

    f.penup()
    f.goto(x, y)
    f.pendown()

    f.begin_fill()

    f.speed(50)

    i: int = 0
    while i < 4:
        f.forward(width)
        f.right(90)
        i = i + 1
    
    f.end_fill()


def draw_sunrays(g: Turtle, x: float, y: float, radius: float) -> None:
    """Draw a circle of the given radius whose starting point is located at x, y."""
    g.pencolor(251, 143, 67)

    g.penup()
    g.goto(x, y)
    g.pendown()

    g.begin_fill()

    g.speed(50)

    g.circle(radius)


if __name__ == "__main__":
    main()