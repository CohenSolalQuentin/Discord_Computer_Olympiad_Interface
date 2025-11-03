import json
import os

from discord_interface.games.games_enum import Discord_Game
from jeux.interfaces_graphiques.Interface_square_amazons import Interface_square_amazons
from jeux.interfaces_graphiques.Interface_square_deplacement import Interface_square_deplacement

import os

class GameChange(Exception):
    pass

def more_recent_file(dossier: str) -> str | None:
    """
    Retourne le chemin complet du fichier le plus récent dans un dossier.
    Si le dossier est vide ou ne contient pas de fichiers, retourne None.
    """
    # Liste les fichiers seulement (pas les sous-dossiers)
    fichiers = [os.path.join(dossier, f) for f in os.listdir(dossier)
                if os.path.isfile(os.path.join(dossier, f))]

    if not fichiers:
        return None

    # Cherche le fichier avec le temps de modification le plus récent
    return max(fichiers, key=os.path.getmtime)

def game_construction():
    _json_file = more_recent_file('../log/bot_ref_log/')

    with (open(_json_file, 'r') as file):
        _bot_ref_log = json.load(file)
        #print(_bot_ref_log)


        histo = _bot_ref_log['moves']

        game_name = _bot_ref_log['game_name']
        game = Discord_Game(game_name)
        histo = [game.string_to_action(m) for m in histo]

        for a in histo:
            assert a in game.valid_actions()
            game.plays(a)


    return game_name, game

def lire_fichier_et_maj():
    global game_name

    old_game_name = game_name
    game_name, game = game_construction()

    if old_game_name != game_name:
        interface.quit()
        #raise GameChange()

    interface.hex = game

    #print(len(jeu.historique))

    interface.actualisation_graphique(interface.canvas)

    # Relancer la lecture dans 1000 ms (1 seconde)
    interface.after(1000, lire_fichier_et_maj)


game_name, game = game_construction()

while True:
    try:
        if game_name == 'clobber':
            interface = Interface_square_deplacement(game, ia_noir=None, ia_blanc=None, permu_couleur=False, affichage_valeurs=False)
        elif game_name == 'amazons':
            interface = Interface_square_amazons(game, ia_noir=None, ia_blanc=None, permu_couleur=False, affichage_valeurs=False)

        # Démarrer la boucle de lecture/maj
        lire_fichier_et_maj()

        interface.lancer()

    except GameChange:
        """"""

