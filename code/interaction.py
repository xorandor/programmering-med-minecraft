import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.entity as entity
import time
from chat_handler import get_latest_message
mc = minecraft.Minecraft.create()

def build_tower():
    mc.postToChat("Building a tower!")

    pos = mc.player.getPos()
    height = 10
    mc.setBlocks(pos.x, pos.y, pos.z, pos.x, pos.y + height, pos.z, block.STONE.id)

running = True

while running:
    chat = get_latest_message(mc)

    if chat == "build_tower":
        build_tower()

    if chat == "exit":
        mc.postToChat("Goodbye!")
        running = False
    
    time.sleep(0.2)