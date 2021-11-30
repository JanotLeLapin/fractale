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


def creneau():
    l = 10

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


def iteration1(l: int):
    for j in range(1, 4, 2):
        motif(l / 2)
        left(60)
        motif(l / 2)
        right(120 * j)


def iteration2(l: int):
    for j in range(1, 4, 2):
        iteration1(l / 2)
        left(60)
        iteration1(l / 2)
        right(120 * j)


def motif(l: int):
    forward(l)
    left(60)
    forward(l)
    right(120)
    forward(l)
    left(60)
    forward(l)


def flocon(l: int):
    for i in range(3):
        motif(l)
        right(120)


def iterationN(l: int, n: int):
    print('Code Joseph !')


def floconN(l: int, n: int):
    print('Code Joseph !')
