#!/usr/bin/env python3
# coding: utf-8
"""
Dictionnaire des noms d'indiens :

Usage:
======
    python nsi_dict_indien.py 

    argument1: 
    argument2: 

__authors__ = ("Pascal LUCAS", "Professeur NSI")
__contact__ = ("pascal.lucas@ac-lille.fr")
__version__ = "1.0.0"
__copyright__ = "copyleft"
__date__ = "202101002"

"""

DICT_1 = { 'A' : 'Aigle', 
           'B' : 'Buse',
           'C' : 'Chacal',
           'D' : 'Doryphore',
           'E' : 'Ecureuil',
           'F' : 'Fleuve',
           'G' : 'Grenouille',
           'H' : 'Horizon',
           'I' : 'Iris',
           'J' : 'Jaguar',
           'K' : 'Kangourou',
           'L' : 'Loutre',
           'M' : 'Mésange',
           'N' : 'Neige',
           'O' : 'Ours',
           'P' : 'Pluie',
           'Q' : 'Quetzal',
           'R' : 'Renard',
           'S' : 'Sauterelle',
           'T' : 'Tourterelle',
           'U' : 'Ululement',
           'V' : 'Vent',
           'W' : 'Weigélia',
           'X' : 'Xérus',
           'Y' : 'Yak',
           'Z' : 'Zibeline'}

DICT_2 = { 'A' : ' agile',
           'B' : ' de braise',
           'C' : ' qui chante',
           'D' : ' qui danse',
           'E' : ' qui écoute', 
           'F' : ' de feu',
           'G' : ' des glaces',
           'H' : ' humide',
           'I' : ' invincible',
           'J' : ' juvénile',
           'K' : ' kamikaze',
           'L' : ' de lumière',
           'M' : ' du matin',
           'N' : ' nocturne',
           'O' : ' de l\'ombre',
           'P' : ' paisible',
           'Q' : ' sans querelle',
           'R' : ' qui rit',
           'S' : ' du soir',
           'T' : ' taciturne',
           'U' : ' ultime',
           'V' : ' qui voit',
           'W' : ' en week-end',
           'X' : ' xylophoniste',
           'Y' : ' yoyotant',
           'Z' : ' zig-zaguant'}

# Programme principal
if __name__=='__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=False)
    pass

