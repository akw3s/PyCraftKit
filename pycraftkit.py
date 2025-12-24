# PyCraftKit Metadata
name = "PyCraftKit"
version = "Alpha 1.0"
author = "Akwes" 
description = "This is a library made by {author} to help you create Minecraft bots and many other stuff in one library."
license = "MIT" # Not licensed yet
url = "https://github.com/akw3s/PyCraftKit" # Project URL
dependencies = [ 
    "json", "system"
]

# Example function

def say_hello():
    print(f"Hello from {name} v{version} by {author}!")

class Bot:
    def __init__(self, name):
        self.name = name


"""
 _______           _______  _______  _______  _______ _________ _       __________________
(  ____ )|\     /|(  ____ \(  ____ )(  ___  )(  ____ \\__   __/| \    /\\__   __/\__   __/
| (    )|( \   / )| (    \/| (    )|| (   ) || (    \/   ) (   |  \  / /   ) (      ) (   
| (____)| \ (_) / | |      | (____)|| (___) || (__       | |   |  (_/ /    | |      | |   
|  _____)  \   /  | |      |     __)|  ___  ||  __)      | |   |   _ (     | |      | |   
| (         ) (   | |      | (\ (   | (   ) || (         | |   |  ( \ \    | |      | |   
| )         | |   | (____/\| ) \ \__| )   ( || )         | |   |  /  \ \___) (___   | |   
|/          \_/   (_______/|/   \__/|/     \||/          )_(   |_/    \/\_______/   )_(   
                                                                        Akwes 2025-2026                  
"""

import json
import sys

class MineBot:
    def __init__(self, username, server):
        self.username = username
        self.server = server
        self.position = (0, 70, 0)

    def connect(self):
        print(f"{self.username} connecting to {self.server}...")

    def send_chat(self, message):
        print(f"[CHAT] {self.username}: {message}")

    def move_to(self, x, y, z):
        self.position = (x, y, z)
        print(f"{self.username} moved to {self.position}")

# Example usage
"""
Bot = MineBot("PyBot", "localhost")
Bot.connect()
Bot.send_chat("Hello, Minecraft!")
Bot.move_to(100, 65, 200)
"""

class ConfigGenerator:
    def __init__(self, server_type):
        self.server_type = server_type
        self.config = {}

    def performance_mode(self):
        self.config["view-distance"] = 6
        self.config["max-players"] = 20

    def save(self, filename):
        with open(filename, "w") as f:
            json.dump(self.config, f, indent=4)

# Example usage
"""
cfg = ConfigGenerator("paper")
cfg.performance_mode()
cfg.save("server_config.json")
"""

# CLI
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python pycraftkit.py bot | config")
        sys.exit()

    if sys.argv[1] == "bot":
        bot = MineBot("PyBot", "localhost")
        bot.connect()
        bot.send_chat("Started from CLI")

    elif sys.argv[1] == "config":
        cfg = ConfigGenerator("paper")
        cfg.performance_mode()
        cfg.save("server_config.json")
        print("Config generated")

# End of PyCraftKit