import discord
from discord.commands import Option

bot = discord.Bot()

def autocomplete_func(ctx: discord.AutocompleteContext) -> list:
    return [
        'test',
        'foo',
        'bar'
    ]

@bot.slash_command()
async def hello(
    ctx, 
    option: Option(
        str,
        "This is an autocomplete option",
        autocomplete=autocomplete_func
    )):
    name = ctx.author.name
    await ctx.respond(f"Hello {name}!")

@bot.user_command(name="Say Hello")
async def hi(ctx, user):
    await ctx.respond(f"{ctx.author.mention} says hello to {user.name}!")

bot.run("token")
