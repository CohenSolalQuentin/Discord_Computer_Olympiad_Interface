from discord_interface.games.translator.quentin_games.Amazons import Amazons
from discord_interface.games.translator.quentin_games.Quoridor import Quoridor
from discord_interface.games.translator.quentin_games_interface import InterfaceJeuDiscord




class QuoridorDiscord(InterfaceJeuDiscord):

    def __init__(self):
        super().__init__('quoridor', Quoridor, params=None, rules='standard', move_keywords=[])

