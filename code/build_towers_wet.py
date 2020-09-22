"""
Eksempel på "våd" kode fra dag 3. 
WET: Write Everything Twice
"""

import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.entity as entity
import time
mc = minecraft.Minecraft.create()

pos = mc.player.getPos()
# første tårn - 10 blokke
mc.setBlocks(pos.x, pos.y, pos.z, pos.x, pos.y + 10, pos.z, block.STONE.id)
mc.setBlock(pos.x, pos.y + 11, pos.z, block.GOLD_BLOCK.id)
time.sleep(5)
pos = mc.player.getPos()
# andet tårn - 15 blokke
mc.setBlocks(pos.x, pos.y, pos.z, pos.x, pos.y + 15, pos.z, block.STONE.id)
mc.setBlock(pos.x, pos.y + 16, pos.z, block.GOLD_BLOCK.id)
time.sleep(5)
pos = mc.player.getPos()
# tredje tårn - 20 blokke
mc.setBlocks(pos.x, pos.y, pos.z, pos.x, pos.y + 20, pos.z, block.STONE.id)
mc.setBlock(pos.x, pos.y + 21, pos.z, block.GOLD_BLOCK.id)
