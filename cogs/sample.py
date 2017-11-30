import discord
from discord.ext import commands


class Sample:
    def __init__(self, bot):
        self.bot = bot


    def on_guild_join(self, guild):
        """
        Events in cogs don't need the decorator

        This event receives the the guild when the bot joins.
        """
        print(f'Joined {guild.name} with {guild.member_count} users!')
    
    @commands.command()
    async def test(self, ctx):
        """
        A test command, Mainly used to show how commands and cogs should be laid out.
        """
        await ctx.send('Tested!')
    
    @commands.group(invoke_without_command=True)
    async def foo(self, ctx):
        """
        A sub command group, Showing how sub command groups can be made.
        """
        await ctx.send('try my subcommand')
    
    @foo.command(aliases=['an_alias'])
    async def bar(self, ctx):
        """
        I have an alias!, I also belong to command 'foo'
        """
        await ctx.send('foo bar!')


def setup(bot):
    bot.add_cog(Sample(bot))
