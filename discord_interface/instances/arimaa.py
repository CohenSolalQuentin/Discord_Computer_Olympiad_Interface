from discord_interface.games.translator.quentin_games.Arimaa_vrai import Arimaa_vrai
from discord_interface.games.translator.quentin_games_interface import InterfaceJeuDiscord



class ArimaaDiscord(InterfaceJeuDiscord):

    def __init__(self):
        super().__init__('arimaa', Arimaa_vrai, params=None, rules='standard', move_keywords=['pass'])

