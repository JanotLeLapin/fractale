from algo import *
import inquirer

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
