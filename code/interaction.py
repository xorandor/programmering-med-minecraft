import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.entity as entity
import time
import random
from chat_handler import get_latest_message
mc = minecraft.Minecraft.create()


def build_tower():
    mc.postToChat("Building a tower!")

    pos = mc.player.getPos()
    height = 10
    mc.setBlocks(pos.x, pos.y, pos.z, pos.x, pos.y +
                 height, pos.z, block.STONE.id)


valuables = [
    block.GOLD_BLOCK.id,
    block.DIAMOND_BLOCK.id,
    block.EMERALD_ORE.id
]


def walkOnGold():
    pos = mc.player.getTilePos()
    mc.setBlock(pos.x, pos.y-1, pos.z, block.GOLD_BLOCK.id)


running = True
walkingOnGold = False

while running:
    chat = get_latest_message(mc)

    if chat == "walk on gold":
        walkingOnGold = True
    if chat == "build_tower":
        build_tower()
    if chat == "exit":
        mc.postToChat("Goodbye!")
        running = False

    if walkingOnGold:
        walkOnGold()
    time.sleep(0.1)
