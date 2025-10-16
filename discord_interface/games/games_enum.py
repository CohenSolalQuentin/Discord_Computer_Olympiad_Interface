"""File used for game enumeration.

This file contains a class called EnumGames that stores games used by the RefereeBot as well as the PlayerBot.
"""
from enum import Enum#, verify, UNIQUE

from discord_interface.games.instances.amazons import AmazonsDiscord
from discord_interface.games.instances.breakthrough import BreakthroughDiscord
from discord_interface.games.instances.clobber import *

#Metadata
__author__ = "Oscar PERIANAYAGASSAMY"
__copyright__ = "Copyright 2025, Interface Computer Olympiad"
__status__ = "Development"
__email__ = "oscar.perianayagassamy@dauphine.eu"

from discord_interface.games.instances.free_game import FreeGame
from discord_interface.games.instances.gtp_game import GTP_Game
from discord_interface.games.instances.santorini import SantoriniDiscord

if __name__ != "__main__":

    #@verify(UNIQUE)
    class EnumGames(Enum):
        BREAKTHROUGH = BreakthroughDiscord()
        SANTORINI = SantoriniDiscord()
        AMAZONS = AmazonsDiscord()
        CLOBBER = Clobber()
        #AMAZONS_BUGUER = AmazonsDiscordBugger()
        FREE_GAME = FreeGame()
        GTP_GAME = GTP_Game()
        #ECHECS = EchecDiscord()




        #**** .................... ****"
        #**** add other games here ****#

        def __eq__(self, other):
            if type(other) != str and type(other) != self.__class__:
                raise TypeError()
            return other == self.value

        @classmethod
        def get_available_games(cls) -> List[Game]:
            """Class method that returns a list of the different available games"""
            return [cls.__members__[game].value.__class__() for game in cls.__members__]

        @classmethod
        def find_game(cls, game_name:str):
            """Method that tries to find the game specified by game_name in the enumeration"""
            if game_name.upper() not in EnumGames.__members__:
                return None
            return EnumGames.__members__[game_name.upper()].value.__class__()


def Discord_Game(game_name):

    game_name = game_name.lower()

    for game_members in EnumGames.__members__:

        if game_name == game_members.lower():
            return EnumGames[game_members].value

    """if game_name == 'santorini':
        return SantoriniDiscord()
    elif game_name == 'clobber':
        return Clobber()
    elif game_name == 'amazons':
        return AmazonsDiscord()
    elif game_name == 'free_game':
        return FreeGame()
    elif game_name == 'echecs':
        return EchecDiscord()
    elif game_name == 'amazons-bugguer':
        return AmazonsDiscordBugger()

    elif game_name == 'gtp':
        return GTP_Game()"""