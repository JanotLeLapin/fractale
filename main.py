from turtle import *
import inquirer


# Algorithmes
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


# User input
algo = inquirer.prompt([
    inquirer.List(
        'algo',
        'Quel algorithme voulez vous exécuter ?',
        [
            'Dessin A',
            'Dessin B',
            'Dessin C',
            'Motif',
            'Itération 1',
            'Itération 2'
        ]
    )
])['algo']

options = {
    'Dessin A': spirale,
    'Dessin B': rosace,
    'Dessin C': creneau,
}

segment_options = {
    'Motif': motif,
    'Itération 1': iteration1,
    'Itération 2': iteration2,
}

if algo in options:
    speed(0)
    options[algo]()
    done()
elif algo in segment_options:
    try:
        segment = int(inquirer.prompt([
            inquirer.Text(
                'segment', 'Quelle longueur de segment voulez vous utiliser ?', '50')
        ])['segment'])

        speed(0)
        segment_options[algo](segment)
        done()
    except ValueError:
        print('Mauvais segment.')
