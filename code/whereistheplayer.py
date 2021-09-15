import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.entity as entity
import time
mc = minecraft.Minecraft.create()

pos = mc.player.getPos()

mc.setBlock(pos.x,pos.y+2,pos.z, block.TNT.id)
mc.setBlock(pos.x,pos.y+3,pos.z, block.FIRE.id)
print(pos.x)