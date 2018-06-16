def deplacer_disque(source, destination):
    print('Deplacer disque de {} a {}'.format(
        source, destination))


def deplacer_tour(hauteur, tour_source,
        tour_destination, tour_intermediaire):

    if hauteur >= 1:
        deplacer_tour(
            hauteur - 1,
            tour_source,
            tour_intermediaire,
            tour_destination
        )
        deplacer_disque(
            tour_source,
            tour_destination
        )
        deplacer_tour(
            hauteur - 1,
            tour_intermediaire,
            tour_destination,
            tour_source
        )


deplacer_tour(3, 'A', 'B', 'C')
