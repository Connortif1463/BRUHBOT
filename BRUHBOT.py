import random
import time

import os

from discord import message
from dotenv import load_dotenv
import psycopg2

from discord.ext import commands
from discord.ext.commands import Bot

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
DATABASE_URL = os.getenv('DATABASE_URL')

DEPLOYED = os.getenv('DEPLOYED')
command_prefix = '+'
if (DEPLOYED == 'true'):
    command_prefix = '-'

client: Bot = commands.Bot(command_prefix=command_prefix)

@client.event
async def on_ready():
    print('bot is ready')


@client.command(aliases=['bruh moment', 'BRUH MOMENT', 'bruh', 'BRUH', 'br', 'b', 'Br'])
async def bruh_command(ctx):
    responses = [
        'Bruh moment.',
        'Bruh.',
        'Yep, bruh.',
        'Ah, yes. Bruh.',
        'Bruh moment.',
        'BRUH.',
        'Uhh... bruh.',
        'Nah fuck you.',
        'Bruh denied.',
        'JK. No bruh for you.',
        'There is no bruh... uh..\nTake off your-clothes.',
        'https://www.youtube.com/watch?v=V263ad2e2uk',
        'https://www.youtube.com/watch?v=D2_r4q2imnQ',
        'https://www.youtube.com/watch?v=2ZIpFytCSVc',
        'https://www.youtube.com/watch?v=aSGSOVTObtU',
        'https://youtu.be/AiiujN_Bnn4',
        'https://www.youtube.com/watch?v=fXu3BxfHSPo',
        'sike.\nhttps://www.youtube.com/watch?v=6n3pFFPSlW4',
        'https://www.youtube.com/watch?v=Go9_DeFmt5Y',
        'https://www.youtube.com/watch?v=yEqZPXlrI0Q',
        'https://media.giphy.com/media/3ohc0VmrLRmy5om1q0/giphy.gif',
        'https://media.giphy.com/media/NrqabhEpXWsGA/giphy.gif',
        'https://media.giphy.com/media/VIOkcgpsnA2Zy/giphy.gif',
        'BRUH\nhttps://media.giphy.com/media/6RXkMDpm1Qppu/giphy.gif',
        'https://media.giphy.com/media/LpKvmzTYeufcnoZqx5/giphy.gif',
        'https://media.giphy.com/media/fwcdbnYMfLadmVjie3/giphy.gif',
        'https://youtu.be/s7CWaLrTPWA'
    ]
    dialog = [
        'BRUH MACHINE go BRRRRR...',
        'One moment...\nBEEP BOOP...\nbruh processor evaluating...',
        'It is bruh time...',
        'Incoming bruh moment...',
        'Bruh moment?',
        'Is that a bruh request I see?',
        'Bruh?',
        'Bruh time.',
        'Bruh bruh bruh bruh bruh bruh bruh...'
    ]
    index = random.randint(1, len(dialog)) - 1
    print(index)
    await ctx.send(f'' + dialog[index])
    time.sleep(2)
    index = random.randint(1, len(responses)) - 1
    print(index)
    await ctx.send(f'' + responses[index])


@client.command(aliases=['bonk', 'BONK', 'bo', 'Bo'])
async def bonk_command(ctx):
    responses = [
        'Bonk!',
        'U get bonked.',
        'https://www.youtube.com/watch?v=vhhiyC7OmYA',
        'https://www.youtube.com/watch?v=gomdgnprFXs',
        'https://www.youtube.com/watch?v=0yoRaVRHhg8',
        'https://www.youtube.com/watch?v=ckSkVkC5x1M',
        'https://www.youtube.com/watch?v=8Z3dBRQMe5U',
        'https://youtu.be/QqInmTXNP_s',
        'https://youtu.be/ItjHNxDd9d4',
        'https://youtu.be/QH0vkuqMJF0',
        'https://youtu.be/235vzbMRzDU',
        'https://www.youtube.com/watch?v=cLZq-_vymzI',
        'https://www.youtube.com/watch?v=EWw59hP-yfg',
        'https://www.youtube.com/watch?v=6oLeOPlQQ2w',
        'https://youtu.be/-o1Q_4kv2Bg'
    ]
    index = random.randint(1, len(responses)) - 1
    print(index)
    await ctx.send(f'' + responses[index])


@client.command(aliases=['walter', 'Walter', 'WALTER', 'w', 'W'])
async def walter_command(ctx):
    responses = [
        'https://www.youtube.com/watch?v=RBmW-ATFSiA',
        'https://www.youtube.com/watch?v=vhhiyC7OmYA',
        'https://www.youtube.com/watch?v=DfnrxZouSwY',
        'https://www.youtube.com/watch?v=oES4c84trgw&feature=emb_rel_end',
        'https://www.youtube.com/watch?v=lXBNLptIx_Y',
        'https://www.youtube.com/watch?v=ysGTVCLDpwg',
        'https://www.youtube.com/watch?v=7GqQ_4gJkQ4',
        'https://www.youtube.com/watch?v=hMsNLHKjXmI',
        'https://www.youtube.com/watch?v=J3yBeXfoKH4',
        'https://www.youtube.com/watch?v=NJ55Yy0wj3U',
        'https://www.youtube.com/watch?v=-y4U4jEqKDM',
        'https://www.youtube.com/watch?v=VXkBJECDEZ8',
        'https://www.youtube.com/watch?v=c6k4_y9IDQk',
        'https://www.youtube.com/watch?v=ckSkVkC5x1M'
    ]
    index = random.randint(1, len(responses)) - 1
    print(index)
    await ctx.send(f'' + responses[index])


@client.command(aliases=['twomad', 'two', '2mad', '2'])
async def twomad_command(ctx):
    responses = [
        'https://www.youtube.com/watch?v=AG6YIYW19mU',
        'https://www.youtube.com/watch?v=0yN6lfPcxI4',
        'https://www.youtube.com/watch?v=0yN6lfPcxI4',
        'https://www.youtube.com/watch?v=HkfPM8HWmlc',
        'https://www.youtube.com/watch?v=w2KveJudVkM',
        'https://www.youtube.com/watch?v=XpZTO8-u3fw',
        'https://www.youtube.com/watch?v=-AEnEsR18PY',
        'https://www.youtube.com/watch?v=sPgYth8tCXo',
        'https://youtu.be/Q_PctqvKJ80',
        'https://www.youtube.com/watch?v=utyxtJPF2l4',
        'youtube.com/watch?v=HddWniwIb_w',
        'https://www.youtube.com/watch?v=FJzMm-Cmfqk',
        'https://www.youtube.com/watch?v=bUa5hKHWvRk',
        'https://www.youtube.com/watch?v=2FHtL5gLVOE',
        'https://www.youtube.com/watch?v=Kv9DTAAPjaw',
        'https://www.youtube.com/watch?v=bMjDlJbNNas',
        'https://www.youtube.com/watch?v=vqNTJg9EnsQ',
        'https://www.youtube.com/watch?v=ocCKMSy_4So',
        'https://www.youtube.com/watch?v=uLOo13R-ZFI',
        'https://www.youtube.com/watch?v=YtwIGUNyAew',
        'https://www.youtube.com/watch?v=YiYoC84ernA',
        'https://www.youtube.com/watch?v=SL-L5Pm_T1g',
        'https://www.youtube.com/watch?v=WZ72M6d_fGM',
        'https://www.youtube.com/watch?v=OYnp5RcC2WU',
        'https://www.youtube.com/watch?v=PMCBsvwBVGs',
        'https://www.youtube.com/watch?v=3S5x9GG4k10',
        'https://www.youtube.com/watch?v=C7EU86EHzpk',
        'https://www.youtube.com/watch?v=4ZtwnfpAKPA'
    ]
    index = random.randint(1, len(responses)) - 1
    print(index)
    await ctx.send(f'' + responses[index])


@client.command(aliases=['bruhcount', 'bc', 'BC', 'BRUHCOUNT'])
async def bruh_count(ctx):
    global bruhcount
    await ctx.send(f'_(BEEP-BOOP)_')
    time.sleep(1)
    await ctx.send(f'_(CALCULATING TOTAL BRUH MOMENTS)_')
    time.sleep(2)
    conn = None
    try:
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        cur = conn.cursor()
        query = """
                    SELECT * FROM counts WHERE bruhname='thebruhcount'
                    """
        cur.execute(query)
        row = cur.fetchone()
        await ctx.send(f'_TOTAL NUMBER OF BRUH MOMENTS:_ ' + str(row[1]))
        print(cur)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


@client.event
async def on_message(message):
    if message.author.name != 'BRUH BOT':
        if 'bruh' in message.content.lower():
            conn = None
            try:
                conn = psycopg2.connect(DATABASE_URL, sslmode='require')
                cur = conn.cursor()
                query = """
                SELECT * FROM counts WHERE bruhname='thebruhcount'
                """
                cur.execute(query)
                row = cur.fetchone()
                newbruhcount = row[1] + 1

                updateQuery = """
                UPDATE counts
                SET bruhcount =
                """ + str(newbruhcount) + """
                WHERE bruhname='thebruhcount'
                """
                cur.execute(updateQuery)

                #print(cur)
                cur.close()
                conn.commit()
            except (Exception, psycopg2.DatabaseError) as error:
                print(error)
            finally:
                if conn is not None:
                    conn.close()
                    print('Database connection closed.')
            print('someone said bruh')
    await client.process_commands(message)


@client.command(aliases=['r', 'rep', 're', 'R', 'RE', 'REP'])
async def replace(ctx):
    await ctx.send(f'Welcome to the substring replacement tool.')

    await ctx.send(f'Paste a line of text you want to edit:')

    def pred(m):
        return m.author.name == ctx.message.author.name and m.channel == ctx.message.channel

    msg = await client.wait_for('message', check=pred)
    text = msg.content

    await ctx.send(f'Type the string you intend to replace:')

    def pred(m):
        return m.author.name == ctx.message.author.name and m.channel == ctx.message.channel

    msg = await client.wait_for('message', check=pred)
    replace = msg.content

    await ctx.send(f'Type the text you want to replace it with:')

    def pred(m):
        return m.author.name == ctx.message.author.name and m.channel == ctx.message.channel

    msg = await client.wait_for('message', check=pred)
    replacewith = msg.content

    await ctx.send(text.replace(replace, replacewith))


@client.command()
async def ping(ctx):
    await ctx.send(f'Bonked at {round(client.latency * 1000)} milliseconds.')


client.run(TOKEN)
