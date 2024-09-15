from hvicorn import Bot, CommandContext
import os
import json

if os.path.exists("user.txt"):
    with open("user.txt", "r", encoding="utf-8") as user_file:
        lines = user_file.readlines()
        for line in lines:
            if line.startswith("username:"):
                nick = line.replace("username:", "").strip()
            elif line.startswith("password:"):
                password = line.replace("password:", "").strip()
            elif line.startswith("channel:"):
                channel = line.replace("channel:", "").strip()
            elif line.startswith("trustedusers:"):
                trustedusers = json.loads(line.replace("trustedusers:", "").strip())
                bot = Bot(nick=nick,password=password,channel=channel)
            else:
                print("Error: 'user.txt' file not found. Please ensure the file exists.")

@bot.command("ping")
def pingpong(ctx: CommandContext):
    return ctx.respond("Pong!")

bot.run()
