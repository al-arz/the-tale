
import logging

from discord.ext import commands as discord_commands


class Bot(discord_commands.Bot):

    async def on_ready(self):
        logging.info('logged as "%s"', self.user)

    async def on_message(self, message):
        logging.info(f'Message from {message.author}: {message.content}')
