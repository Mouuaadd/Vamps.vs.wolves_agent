import math


def proba_small_attacker(e1: int, e2: int):
    return e1/(2 * e2)


def proba_large_attacker(e1: int, e2: int):
    return e1/e2 - 0.5


def approx_nb_winning_attacker(e1: int, e2: int, proba: float):
    return math.floor((e1 + e2) * proba)


def approx_nb_surviving_attacked(e2: int, proba: float):
    return math.floor(e2 * (1 - proba))


def battle_humans(nb_units, nb_humans):
    # Assumption: we're never going on a battle with humans we can't beat
    # Its explicitly filtered in possible moved even though it exists here
    if nb_units >= nb_humans:
        proba = 1
    else: # random battle
        proba = nb_units / (2 * nb_humans)

    return approx_nb_winning_attacker(nb_units, nb_humans, proba)


def battle_enemy(nb_units, nb_enemy):
    # Assumption: we're never going on a battle with enemy we can't beat
    # Its explicitly filtered in possible moved even though it exists here
    if nb_units >  nb_enemy:
        proba = 1
    elif nb_units <= nb_enemy:
        proba = 0

    return proba, approx_nb_winning_attacker(nb_units, nb_enemy, proba)
