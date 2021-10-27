import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.entity as entity
import time
import random
from chat_handler import get_latest_message
mc = minecraft.Minecraft.create()

running = True

while running:
    chat = get_latest_message(mc)
    if chat==None:
        continue

    pieces = chat.split(" ")
    command = pieces[0]
    arg = pieces[1]

    if command=="spawn":
        if arg == "cow":
            pos = mc.player.getPos()
            mc.spawnEntity(pos.x, pos.y, pos.z, entity.COW.id)
    
    
    

    

    if chat == "exit":
        mc.postToChat("Goodbye!")
        running = False

    time.sleep(1)
