from turtle import *


def spirale():
    for i in range(10):
        for j in range(2):
            forward(10 * i)
            left(90)


def rosace():
    for i in range(36):
        circle(80)
        left(10)


def creneau(l):
    def tleft():
        left(90)

    def tright():
        right(90)

    for i in range(4):
        for j in range(10):
            forward(l)
            tleft()
            forward(l)
            tright()
            forward(l)
            tright()
            forward(l)
            tleft()
        forward(l * 2)
        for j in range(3):
            tleft()
            forward(l)


speed(0)
spirale()
done()
