import discord
from keep_alive import keep_alive
import openai
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(intents=intents, command_prefix='!')

openai.api_key = "API_KEY"


@bot.event
async def boot():
    print(bot.user.id)


@bot.command()
async def generate(ctx, *args):
  try:
    message = " ".join(args)
    response = openai.Image.create(
    prompt=f"{message}",
    n=1,
    size="1024x1024")
    image_url = response['data'][0]['url']
    await ctx.send(image_url)
  except:
    pass

      

@bot.listen()
async def on_message(message):
  if message.author == bot.user or message.content.startswith('!'):
    return
  try:
    if message.content.startswith("BOT") or bot.user.mentioned_in(message):
      try:
        response = openai.Completion.create(
           model="text-davinci-003",
           prompt=f"{message.content}",
           temperature=0.9,
           max_tokens=150,
           top_p=1,
           frequency_penalty=0.0,  
           presence_penalty=0.6,
           stop=[" BOT", " BOT#3060"]
        )
      except:
        response = {"choices": [{"text": "yed ped analysis"}]}
      
      await message.channel.send(
        f"{message.author.mention} " + response["choices"][0]["text"]
      )
    
  except:
    pass

token = "TOKEN"

keep_alive()
bot.run(token)
