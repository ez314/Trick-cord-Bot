# Trick-cord-Bot
Automating Trick'cord Treat on Discord

## What is this Trick'cord Treat?
[Trick'cord Treat](https://blog.discord.com/discord-saves-halloween-7816b934c0b1?gi=6c70954035c) is a bot developed by Discord that spawns tricks and treats in servers based on activities. Players must type `h!trick` or `h!treat` based on the contents of the spawn message.  

## What does Trick-cord Bot do?
Trick-cord Bot is a simple selfbot that automatically sends `h!trick` and `h!treat` for you at lightning speeds! Snipe your friends and trick them into thinking you type at 500 WPM :)  

The goal of this project is to demonstrate an extremely simple Python Discord bot that reads embeds. 

## How to run  
### Configuration
Edit `config.json` with your configuration.  
 - **token**: your Discord token. There are plenty of guides on how to get this.  
 - **channels**: list of IDs for channels to watch for possible Trick'cord Treat messages. Learn how to find these IDs [here](https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID).  
 - **treatBot**: ID of the bot itself. Instructions on how to do this can be found at the previous link.

### Starting the bot
Assuming `python` defaults to Python 3:
```sh
python -m pip install requirements.txt
python bot.py
```

## Note on selfbots  
Please read Discord's [official stance on selfbots](https://support.discord.com/hc/en-us/articles/115002192352-Automated-user-accounts-self-bots) before running this project.