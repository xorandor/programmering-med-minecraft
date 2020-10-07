import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.entity as entity
import time
import random
from chat_handler import get_latest_message
mc = minecraft.Minecraft.create()

running = True
isWalkingOnGold = False
blocks = [block.LAVA.id, block.WATER.id, block.GOLD_BLOCK, block.TNT.id]


def walkOnGold():
    pos = mc.player.getTilePos()
    randomTal = random.randint(0, len(blocks)-1)
    mc.setBlock(pos.x, pos.y-1, pos.z, blocks[randomTal])


while running:
    chat = get_latest_message(mc)

    if chat == "exit":
        mc.postToChat("Goodbye!")
        running = False

    if chat == "guld sti":
        isWalkingOnGold = True

    if chat == "stop":
        isWalkingOnGold = False

    if isWalkingOnGold:
        walkOnGold()
    time.sleep(0.1)
