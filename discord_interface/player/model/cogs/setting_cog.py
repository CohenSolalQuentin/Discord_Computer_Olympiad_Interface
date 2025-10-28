from discord import Colour, Embed
from discord.ext import commands
from discord_interface.player.model.player_bot import PlayerBot
from discord.ext.commands import Context

#Metadata
__author__ = "Oscar PERIANAYAGASSAMY"
__copyright__ = "Copyright 2025, Interface Computer Olympiad"
__status__ = "Development"
__email__ = "oscar.perianayagassamy@dauphine.eu"

from discord_interface.utils.terminal import blue

if __name__ != '__main__':

    class Setting(commands.Cog):
        """Class that inherits commands.Cog, that represents a fraction of the commands and features of the PlayerBot that are about settings.

        ATTRIBUTES
        ----------
        bot : player_bot.PlayerBot
            The model to which this Cog will be added.
        """

        def __init__(self, bot: PlayerBot) -> None:
            self.bot = bot

        @commands.command(name="quit", description="command to shut down the model.")
        @commands.dm_only()
        async def _quit(self, ctx: Context, *args: None) -> None:
            """Coroutine that implements the quit command"""
            #print('> quit to close')

            # If the author is not the owner, raise a CheckFailure...
            if not self.bot.check_owner(ctx.author):
                #raise commands.CheckFailure("Only the owner of the model can use this command.")
                return

            # ...Otherwise shut down the model
            await ctx.send(f"shutting down {self.bot.user.mention}...")

            await self.bot.close()

        @commands.command(name="resign", description="command to resign.")
        #@commands.dm_only()
        async def _resign(self, ctx: Context, *args: None) -> None:
            """Coroutine that implements the resign command"""

            # If the author is not the owner, raise a CheckFailure...
            if not self.bot.check_owner(ctx.author):
                #raise commands.CheckFailure("Only the owner of the model can use this command.")
                #await ctx.send(f"test... "+str(ctx.author))
                return

            #await ctx.send(f"resigning...")

            await self.bot.resign()



        @commands.command(name="info", description="command used for debugging purposes")
        @commands.dm_only()
        async def _info(self, ctx: Context) -> None:
            """Coroutine that implements the info command by displaying the PlayerBot player field's attributes entirely."""


            # If the author is not the owner
            if not self.bot.check_owner(ctx.author):
                return

            embedVar = Embed(title="Player's Settings", description=self.bot.player.__str__(), color=Colour.random())
            await ctx.send(embed=embedVar)




        @commands.command(name='continue', description='Continue the match.', aliases=['c'])
        #@commands.dm_only()
        @commands.guild_only()
        async def _continue(self, ctx: Context) -> None:
            #print("???")
            """Command that starts the game

            After verifying that the bot is neither in game nor in preparation, invoke the function that starts the game

            PARAMETERS
            ----------
            ctx : discord.Context
                The invocation context.

            RETURNS
            -------
            None
            """
            #print('+continue')
            # Checking section
            # To start a game, the model should be in 'in-game' mode
            if self.bot.check_in_game():
                raise commands.CheckFailure("The model shouldn't be in game when invoking this command.")

            # If the author is not the owner, raise a CheckFailure...
            if not self.bot.check_owner(ctx.author):
                #raise commands.CheckFailure("Only the owner of the model can use this command.")
                return

            await self.bot.continue_match(ctx)#
            #print('-continue')


        @commands.command(name='slow_continue', description='Continue the match [alternative (slow) command].', aliases=['sc'])
        #@commands.dm_only()
        @commands.guild_only()
        async def _slow_continue(self, ctx: Context) -> None:
            #print("???")
            """Command that starts the game

            After verifying that the bot is neither in game nor in preparation, invoke the function that starts the game

            PARAMETERS
            ----------
            ctx : discord.Context
                The invocation context.

            RETURNS
            -------
            None
            """
            #print('+continue')
            # Checking section
            # To start a game, the model should be in 'in-game' mode
            if self.bot.check_in_game():
                raise commands.CheckFailure("The model shouldn't be in game when invoking this command.")

            # If the author is not the owner, raise a CheckFailure...
            if not self.bot.check_owner(ctx.author):
                #raise commands.CheckFailure("Only the owner of the model can use this command.")
                return

            await self.bot.continue_match_slow(ctx)#
            #print('-continue')


        @commands.command(name='profiler', description='Profiler.', aliases=['p'])
        #@commands.dm_only()
        @commands.guild_only()
        async def _profiler(self, ctx: Context) -> None:
            """Command that profil the serveur

            PARAMETERS
            ----------
            ctx : discord.Context
                The invocation context.

            RETURNS
            -------
            None
            """

            # If the author is not the owner, raise a CheckFailure...
            if not self.bot.check_owner(ctx.author):
                #raise commands.CheckFailure("Only the owner of the model can use this command.")
                return

            await self.bot.profile(ctx)

        @commands.command(name='load_log', description='Load last log.')
        # @commands.dm_only()
        @commands.guild_only()
        async def _load_log(self, ctx: Context) -> None:
            """Command that profil the serveur

            PARAMETERS
            ----------
            ctx : discord.Context
                The invocation context.

            RETURNS
            -------
            None
            """

            # If the author is not the owner, raise a CheckFailure...
            if not self.bot.check_owner(ctx.author):
                #raise commands.CheckFailure("Only the owner of the model can use this command.")
                return

            if self.bot.check_in_game():
                raise commands.CheckFailure("The model shouldn't be in game when invoking this command.")

            await self.bot.log_loading(only_not_ended=False)


        @commands.command(name='conf_test', description='Test the configuration file.', aliases=['et'])
        #@commands.dm_only()
        @commands.guild_only()
        async def _conf_testing(self, ctx: Context) -> None:

            # If the author is not the owner, raise a CheckFailure...
            if not self.bot.check_owner(ctx.author):
                raise commands.CheckFailure("Bad OWNER_ID in parameters.conf")#'Bot id '+str(self.bot.user.id)+

            print(blue('All is OK!'))
