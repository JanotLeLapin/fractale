from algo import *
import inquirer

options = {
    'Dessin A': spirale,
    'Dessin B': rosace,
    'Dessin C': creneau,
}

segment_options = {
    'Motif': motif,
    'Itération 1': iteration1,
    'Itération 2': iteration2,
    'Flocon': flocon
}

algo = inquirer.prompt([
    inquirer.List(
        'algo',
        'Quel algorithme voulez vous exécuter ?',
        [list(d.keys()) for d in [options | segment_options]][0]
    )
])['algo']

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
