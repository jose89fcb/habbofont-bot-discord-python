import discord
from discord.ext import commands
import io
import requests
from PIL import Image, ImageDraw, ImageFont, ImageFile
 
 
bot = commands.Bot(command_prefix='!', description="ayuda bot")
bot.remove_command("help")
 
 
@bot.command()
async def texto(ctx,   habbofont, *, texto):
    fuente = f"{habbofont}"
    url = f"https://habbofont.net/font/{fuente}/{texto}.gif".replace(' ','+')
    imagen = Image.open(io.BytesIO(requests.get(url).content))
    r = requests.get(url)
    if  r.status_code ==200:
        imagen = Image.open(io.BytesIO(requests.get(url).content))
        with io.BytesIO() as imagen_binary:
            imagen.save(imagen_binary, 'PNG')
            imagen_binary.seek(0)
            embed=discord.Embed(title="Fuente habbo Hotel", url="https://habbofont.net", description=f"")
    
            embed.set_image(url=f"attachment://Fuente.png")
            embed.set_footer(text="Créditos habbofont.net -  BOT Programado Por Jose89fcb")
            await ctx.send(embed=embed, file=discord.File(fp=imagen_binary, filename=f"Fuente.png"))
    else:
        await ctx.send(f":(")

@texto.error
async def texto_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Debes de añadir un texto / tipo de fuente")


 
 

 
 
 
@bot.event
async def on_ready():
    print("BOT listo!")
    
 
    
bot.run('') 
