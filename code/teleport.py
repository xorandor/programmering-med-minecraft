import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.entity as entity
import time
mc = minecraft.Minecraft.create()
mc.player.setTilePos(0,0,0)
mc.setBlock(0,2,-1, block.LAVA.id)
mc.setBlock(0,2,-2, block.LAVA.id)
mc.setBlock(0,2,-3, block.LAVA.id)
mc.setBlock(0,2,-4, block.LAVA.id)
mc.setBlock(0,2,-5, block.LAVA.id)
mc.setBlock(0,2,-6, block.LAVA.id)