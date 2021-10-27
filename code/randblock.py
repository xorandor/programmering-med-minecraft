import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.entity as entity
import time
import random
mc = minecraft.Minecraft.create()

while True:
    pos = mc.player.getPos()
    x = random.randint(-10,10)
    mc.setBlock(pos.x + x,pos.y+2,pos.z, 7)
    time.sleep(0.1)
    
