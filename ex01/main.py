from math import sqrt
import turtle

from sys import argv



def pythagoras_tree(t: turtle.Turtle, length: int, level: int):
    if level == 0:
        return

    t.forward(length)

    t.left(45)
    pythagoras_tree(t, length * sqrt(2) / 2, level - 1)
    t.right(90)
    pythagoras_tree(t, length * sqrt(2) / 2, level - 1)
    t.left(45)

    t.forward(-length)


def main():
    if len(argv) != 2:
        print("Incorect arguments\n"
              "Usage: python3 main.py <level>"
        )
        exit(1)

    try:
        level: int = int(argv[1])
    except ValueError:
        print("Level must be a number")
        exit(1)

    if level <= 0:
        print("Level must be a positive number and greater than zero")
        exit(1)

    if level > 8:
        print("WARNING: Levels bigger than 8 may take a while to draw")

    screen = turtle.Screen()
    screen.title(f"Pythagoras tree level {level}")
    screen.bgcolor("black")
    screen.setup(width=1600, height=900)

    t = turtle.Turtle()
    t.speed(0)  # Max speed
    t.color("blue")
    t.pensize(2)

    STEP = 150
    t.left(90)
    pythagoras_tree(t, STEP, level)

    print("Drawing complete")

    t.hideturtle()
    screen.mainloop()


if __name__ == "__main__":
    main()
