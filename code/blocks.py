import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.entity as entity
import time
mc = minecraft.Minecraft.create()

pos = mc.player.getPos()
mc.setBlocks(pos.x-5,pos.y-5,pos.z-5, pos.x+5,pos.y+5,pos.z+5, block.TNT.id)
mc.setBlocks(pos.x-4,pos.y-4,pos.z-4, pos.x+4,pos.y+4,pos.z+4, block.AIR.id)