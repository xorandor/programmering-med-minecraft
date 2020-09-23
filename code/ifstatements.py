import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.entity as entity
import time
import random
mc = minecraft.Minecraft.create()


def buildBlock(width, height, depth, type=block.STONE_BRICK.id, hollow=False):
    pos = mc.player.getPos()
    mc.setBlocks(pos.x, pos.y, pos.z, pos.x+width,
                 pos.y+height, pos.z+depth, type)
    if hollow:
        inner = block.AIR.id
        if random.randint(1, 10) < 5:
            inner = block.LAVA.id

        mc.setBlocks(pos.x+1, pos.y, pos.z+1, pos.x+width-1,
                     pos.y+height-1, pos.z+depth-1, inner)


buildBlock(5, 5, 5, random.randint(1, 20), True)


"""
math random
num = 1
while True:
    if num==1:
        place tnt 
    if num==2:
        place melon 
    num++
    if num > 2:
        num=1    

pos = mc.player.getPos()
x = pos.x+1
y = pos.y
z = pos.z
# mc.setBlock(x,y,z)
direction = "up"
while True:

    mc.setBlock(x, y, z, 0)
    if mc.getBlock(x+1, y, z) == 0:
        x = x+1
        mc.setBlock(x, y, z, block.MELON.id)

    elif mc.getBlock(x, y, z+1) == 0:
        z = z+1
        mc.setBlock(x, y, z, block.MELON.id)
    elif mc.getBlock(x-1, y, z) == 0:
        x = x-1
        mc.setBlock(x, y, z, block.MELON.id)
    elif mc.getBlock(x, y, z-1) == 0:

        y = y-1
        mc.setBlock(x, y, z, block.MELON.id)
    time.sleep(0.5)
    # mc.setBlock(x,y,z, block)
"""
