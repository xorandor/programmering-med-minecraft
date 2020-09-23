import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.entity as entity
import time
import random
mc = minecraft.Minecraft.create()


def build_tower():
    randomHeight = random.randint(10, 20)
    randomWidth = random.randint(10, 20)
    randomDepth = random.randint(10, 20)
    blockType = random.randint(1, 100)
    pos = mc.player.getPos()
    mc.setBlocks(pos.x, pos.y, pos.z,
                 pos.x + randomWidth, pos.y + randomHeight, pos.z + randomDepth,
                 blockType)


build_tower()
