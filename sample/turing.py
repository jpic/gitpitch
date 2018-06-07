import sys

def main(etat, ruban, position):
    action = None
    try:
        tete = ruban[position]
    except IndexError:
        tete = 0

    for a in actions:
        if a[0] == etat and a[1] == tete:
            action = a
            break

    if not action or action[2] == 'stop':
        return False, ruban, position

    # écrire symbole
    if position > len(ruban) - 1:
        ruban.append(action[2])
    else:
        ruban[position] = action[2]

    # déplacer tête
    if action[3] == 'gauche':
        position -= 1
    elif action[3] == 'droite':
        position += 1

    return action[4], ruban, position

position = 0
ruban = [1, 1]
etat = 'a'  # initial
actions = [
    ('a', 0, 'stop'),
    ('a', 1, 0, 'droite', 'b'),
    ('b', 1, 1, 'droite', 'b'),
    ('b', 0, 0, 'droite', 'c'),
    ('c', 1, 1, 'droite', 'c'),
    ('c', 0, 1, 'gauche', 'd'),
    ('d', 1, 1, 'gauche', 'd'),
    ('d', 0, 0, 'gauche', 'e'),
    ('e', 1, 1, 'gauche', 'e'),
    ('e', 0, 1, 'droite', 'a'),
]

print('etat', etat, 'position', position, 'symbole', ruban[position], 'ruban', ruban)
while etat != False:
    (etat, ruban, position) = main(etat, ruban, position)
    print('etat', etat, 'position', position, 'ruban', ruban)
