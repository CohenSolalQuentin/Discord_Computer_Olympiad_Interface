from discord_interface.player.model.textual_ai import Textual_AI
from discord_interface.utils.mytime import Time


class GTP_AI(Textual_AI):


    async def reset(self):

        await super().reset()

        await self.send('clear_board')


    async def undo(self):
        await self.send('undo')


    def get_response_symbol(self):
        return '='

    async def invalid_action_processing(self):
        await self.undo()

    async def replays(self, action):
        await self.send('play '+self.self_color()+' '+self.move_conversion_to_gtp(action))


    async def opponent_plays(self, action):
        await self.send('play '+self.opponent_color()+' '+self.move_conversion_to_gtp(action))



    async def plays(self, time_left: Time=None, opponent_time_left: Time=None):
        #print('A')
        await self.send('time_left ' + self.self_color() + ' ' + str(time_left.to_seconds()))
        await self.send('time_left ' + self.opponent_color() + ' ' + str(opponent_time_left.to_seconds()))
        #print('A')
        action = await self.send('genmove')
        #print("'"+action+"'")
        action = self.move_conversion_from_gtp(action)
        #print("'"+self.move_conversion_from_gtp(action)+"'")
        return action

    def move_conversion_from_gtp(self, move):
        action=''
        is_number=False
        if '-' not in move:
            for c in move:
                if is_number and not c.isdigit():
                    action += '-'+c
                else:
                    action += c
                if c.isdigit():
                    is_number= True
        #print('>',move, '>>', action)
        return action.upper()

    def move_conversion_to_gtp(self, action):
        return action.lower().replace('-','')

