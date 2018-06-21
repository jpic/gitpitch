'''
        23958233
  ×         5830
  ———————————————
        00000000 ( =      23,958,233 ×     0)
       71874699  ( =      23,958,233 ×    30)
     191665864   ( =      23,958,233 ×   800)
  + 119791165    ( =      23,958,233 × 5,000)
  ———————————————
    139676498390 ( = 139,676,498,390        )
'''

def multiplier(a, b):
    resultat = 0

    import ipdb
    ipdb.set_trace()
    for a_index, a_value in enumerate(a[::-1]):
        for b_index, b_value in enumerate(b[::-1]):
            multiplicateur = '1' + ('0' * b_index)
            resultat += int(b_value) * int(a_value) * int(multiplicateur)
            print('resultat', resultat)

print(multiplier('10', '11'))
