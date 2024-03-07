import disnake
import random

token = 'MTIxNTMzMjk0ODA2MDkzODMxMA.GumUJ2.O79i2fLZyXj48dxLtgEhA4iZBpr7yEEwx0F4WU'

intents = disnake.Intents.default()
intents.message_content = True

client = disnake.Client(intents=intents)

@client.event 
async def on_message(message):
    if message.author == client.user:
        return

    
    if message.content == '!насри':

        text = ''
        x = random.randint(1, 10)

        with open('messages.txt', 'r', encoding='UTF-8') as f:
            words = f.read().split('\n')

        for i in range(x):
            c = random.choice([True, False])

            word: str = random.choice(words)
            

            if c:
                word = word.upper()
            text += word + ' '
        
        await message.channel.send(text)
        return

    with open('messages.txt', 'a', encoding='UTF-8') as f:
        f.write(f'{message.content}\n')
    


client.run(token)