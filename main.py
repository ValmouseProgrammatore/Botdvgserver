from webserver import keep_alive
import os
import discord
from discord.ext import commands
from discord import client
import time
import random

print("Il bot è in fase di avvio.. attendere")
prefix = "."
intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix=prefix, intents=intents)
client.remove_command('help')



#Cosa far fare al bot quando è online
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(
        type=discord.ActivityType.listening, name=".help | DVG ╏ Server"))
    print("online")



#Messaggio di benvenuto
@client.event
async def on_member_join(member):
    if member.guild.name == 'DVG ╏ Server':  #type your server name
        embed = discord.Embed(
            title="Benvenuto!",
            description=
            f"Benvenuto {member.mention} in {member.guild.name}, ti auguriamo una buona permanenza!",
            color=0x0061ff,
            font_size=200)
        await client.get_channel(989624702295216148).send(embed=embed)


#Verifica di riserva
@client.command()
async def verifyuser(ctx):
  member = discord.utils.get(ctx.guild.roles, name="DVG╏Utente")
  embed = discord.Embed(
  title="Verifica - DVG ╏ Server",
  description="Ora sei Verificato, buon proseguimento nel server!",
  color=0xe67e22)
  if ctx.channel.id == 989867520561389588:
    await ctx.author.add_roles(member)
    await ctx.message.delete()
    await ctx.send(embed=embed, delete_after=3)


#Ti fornisce una lista di comandi del bot
@client.command()
async def comandi(ctx):
    embed_cmd = discord.Embed(
        title="Comandi - DVG ╏ Server",
        description=
        "Ciao!\nEcco i comandi del bot di DVG ╏ Server:\n**.say**: fai dire qualcosa al bot\n**.help**: mostra le info sul server Discord\n**.userinfo**: mostra le info taggando un utente\n**.botstatus**: visualizza lo stato del bot\n**.consiglio**: manda un consiglio allo staff\n**.stupido**: il bot è stupido\n**.ciao**: ti regala una buona permanenza\n**.server**: ti fornisce le informazioni sul Server\n**.pallamagica**: sceglie le risposte alle tue domande (gli spazi si devono mettere come **_** .Il gioco sarebbe 8Ball)\n**.regole**: ti fornisce le regole del server\n**.assistenza**: comando per ricevere l'assistenza\n**.comandi**: mostra questo messaggio",
        color=0xff0000)
    await ctx.send(embed=embed_cmd)


#Info Server-Bot
@client.command()
async def help(ctx):
    embed_info = discord.Embed(
        title="Help - DVG ╏ Server",
        description=
        "Ciao!\nDVG ╏ Server è un server creato da <@917448585266741248> e <@794658572267946045> per la loro community.\nIn questo server si parla di programmazione, piu in dettaglio di Bot Discord Developing (linguaggi in programmazione: JS e PYTHON)\nIo sono uno dei bot del server e se vuoi informazioni sui comandi digita **.comandi**",
        color=0xff00ff)
    await ctx.send(embed=embed_info)


#Comando per richiedere assistenza
@client.command()
async def assistenza(ctx):
    embed_assistenza = discord.Embed(
        title="Assistenza",
        description=
        "Per ricevere assistenza dallo staff, apri un ticket dal canale <#989885304544579674>",
        color=0x00ff00)
    await ctx.send(embed=embed_assistenza)



#Comando per mandare i Consigli
@client.command()
async def consiglio(ctx, *, arg):
  channel= client.get_channel(993459922002006016)
  embed_consiglio=discord.Embed(title="Grazie per il consiglio", description=f"Grazie per averci mandato il consiglio e miglioreremo il server al piu presto!")
  await ctx.send(embed=embed_consiglio)
  embed_consiglio_staff=discord.Embed(title="Consiglio:", description=arg)
  embed_consiglio_staff.set_author(name=f'{ctx.message.author}', icon_url=ctx.message.author.avatar_url)
  consiglio = await channel.send(embed=embed_consiglio_staff)
  await consiglio.add_reaction("✅")
  await consiglio.add_reaction("❌")



  
#Info User
@client.command()
async def userinfo(ctx, member: discord.Member, roles=None, author=None):
    embed_userinfo = discord.Embed(title=f"UserInfo di {member.name}")
    embed_userinfo.add_field(
        name="Unito al server il",
        value=member.joined_at.strftime("%d/%m/%y, %H:%M:%S"))
    embed_userinfo.add_field(
        name="Account creato il",
        value=member.created_at.strftime("%d/%m/%y, %H:%M:%S"))
    embed_userinfo.set_footer(text=f"Richiesto da {ctx.message.author}")
    if member.bot == True:
        embed_userinfo.add_field(name="É un bot:", value=("Si"))
    if member.bot == False:
        embed_userinfo.add_field(name="É un bot:", value=("No"))
    embed_userinfo.set_thumbnail(url=member.avatar_url)
    await ctx.send(embed=embed_userinfo)



#Informazioni Sul Server
@client.command()
async def server(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name} Info", description="Informazioni su questo Server", color=discord.Colour.blue())
    embed.add_field(name='🆔 Server ID', value=f"{ctx.guild.id}", inline=True)
    embed.add_field(name='📆 Creato il', value=ctx.guild.created_at.strftime("%b %d %Y"), inline=True)
    embed.add_field(name='👑 Owner', value=f"{ctx.guild.owner.mention}", inline=True)
    embed.add_field(name='👥 Utenti', value=f'{ctx.guild.member_count} Members', inline=True)
    embed.add_field(name='💬 Canali', value=f'{len(ctx.guild.text_channels)} Testo | {len(ctx.guild.voice_channels)} Vocali', inline=True)
    embed.set_thumbnail(url=ctx.guild.icon_url) 

    await ctx.send(embed=embed)


  
#Comando per Cancellare i messaggi
@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=100000000000):
    await ctx.channel.purge(limit=amount)
    await ctx.send("Ho cancellato i messaggi!")
    time.sleep(2)
    await ctx.channel.purge(limit=1)


#Stato del Bot #🟢 Online #🧑‍💻 In Developing
@client.command()
async def botstatus(ctx):
    await ctx.send(
        "**Stato del Bot <@989874043601682494>**\n \nBot: 🟢 Online\nPrivacy: Bot Privato\nCreato il: 24/06/2022\nCreato da: ValmouseDJ#2730"
    )


#8ball command
@client.command()
async def pallamagica(ctx, arg):
    responses = [
        'Si, sicuro', 'Si', 'No', 'Dal mio punto di vista è si',
        'Si, convinto', 'Nope', 'Alta possibilità', 'Negativo', 'Non convinto',
        'Si dai'
    ]
    response = random.choice(responses)
    embed = discord.Embed(title="La palla magica ha deciso!")
    embed.add_field(name='Domanda: ', value=f'{arg}', inline=False)
    embed.add_field(name='Risposta: ', value=f'{response}', inline=False)
    await ctx.send(embed=embed)


#Regole del Server
@client.command()
async def regole(ctx):
    embed_regole = discord.Embed(
        title="Regole - DVG ╏ Server",
        description=
        "**1. Non bestemmiare\n2. Non       dire le parolacce\n3. Non insultare\n4. Non pingare     TheGulps e ValmouseDJ, per casi estremi si\n5. Non     aprire più di 1 ticket\n6. Non criticare ne il server ne i bot\n7. Rispettarsi a vicenda\n8. Non       Floddare e/o Flammare/Spammare\n8. Buona permanenza**",
        color=0xFF5733)
    await ctx.send(embed=embed_regole)


#Fai dire al Bot qualcosa
@client.command()
async def say(ctx, *, arg, amount=1):
    embed = discord.Embed(title=arg, color=0xFF5733)
    await ctx.channel.purge(limit=amount)
    await ctx.channel.send(embed=embed)


#Comando stupido
@client.command()
async def stupido(ctx):
    await ctx.send("Si lo sono")


#Comando stupido
@client.command()
async def ciao(ctx):
    await ctx.send(
        f'Ciao anche a te! Ti regaliamo buona permanenza nel server DVG ╏ Server!'
    )


  
keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
