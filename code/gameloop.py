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

    if chat == "build_tower":
        pos = mc.player.getPos()
        mc.setBlocks(pos.x, pos.y, pos.z, pos.x, pos.y+8, pos.z, block.WOOD.id)
    if chat == "exit":
        mc.postToChat("Goodbye!")
        running = False

    time.sleep(0.1)
