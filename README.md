# Discord_Computer_Olympiad_Interface
Human / AI interface with Discord player and referee bots for manual and automatic game playing on Discord servers.

Discord Computer Olympiad Interface (DCOI) allows humans to enter the actions of their game program in text format (actions in A1-B2 format, for example) or to use a Discord bot to do it for them, thus automatically playing. 

DCOI is a set of Discord bots:
    * Player bots: communicating with your program using the Go Text Protocol 
    * Python Player bots: to be inherited by implementing the "plays" method in Python.
    * Referee bots: can be used to arbitrate (time the game, verify the legality of actions, determine the end of the game, and designate the winner) within a Discord discussion.

DCOI is available for a specific set of games (more games will be available soon).
List of available games: see discord_interface/games/instances/

However, thanks to the game called "Free_game", matches can be played on any two-players game with perfect information.


More details on discord_interface/README.txt
