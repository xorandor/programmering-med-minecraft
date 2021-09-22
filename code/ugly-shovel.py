import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.entity as entity
import time
mc = minecraft.Minecraft.create()

pos = mc.player.getPos()

mc.setBlock(pos.x-1,pos.y,pos.z, block.WOOD.id)
mc.setBlock(pos.x,pos.y,pos.z, block.WOOD.id)
mc.setBlock(pos.x+1,pos.y,pos.z, block.WOOD.id)

mc.setBlock(pos.x-1,pos.y+1,pos.z, block.WOOD.id)
mc.setBlock(pos.x,pos.y+1,pos.z, block.WOOD.id)
mc.setBlock(pos.x+1,pos.y+1,pos.z, block.WOOD.id)

mc.setBlock(pos.x-1,pos.y+2,pos.z, block.WOOD.id)
mc.setBlock(pos.x,pos.y+2,pos.z, block.WOOD.id)
mc.setBlock(pos.x+1,pos.y+2,pos.z, block.WOOD.id)

mc.setBlock(pos.x,pos.y+3,pos.z, block.WOOD.id)
mc.setBlock(pos.x,pos.y+4,pos.z, block.WOOD.id)
mc.setBlock(pos.x,pos.y+5,pos.z, block.WOOD.id)