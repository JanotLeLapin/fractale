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

iter_options = {
    'Itération N': iterationN,
    'Flocon N': floconN,
}


algo = inquirer.prompt([
    inquirer.List(
        'algo',
        'Quel algorithme voulez vous exécuter ?',
        [list(d.keys()) for d in [options | segment_options | iter_options]][0]
    )
])['algo']

if algo in options:
    speed(0)
    options[algo]()
    done()
elif algo in segment_options or algo in iter_options:
    try:
        segment = int(inquirer.prompt([
            inquirer.Text(
                'segment', 'Quelle longueur de segment voulez vous utiliser ?', '50')
        ])['segment'])

        if algo in iter_options:
            it = int(inquirer.prompt([
                inquirer.Text(
                    'iter', "Combien d'itérations voulez vous effectuer ?", '5'
                )
            ])['iter'])

            speed(0)
            iter_options[algo](segment, it)
            done()
        else:
            speed(0)
            segment_options[algo](segment)
            done()
    except ValueError:
        print('Mauvais segment.')
