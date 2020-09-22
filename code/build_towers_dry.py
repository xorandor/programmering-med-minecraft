"""
Eksempel på "tør" kode fra dag 3.
DRY: Don't Repeat Yourself 
"""

import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.entity as entity
import time
mc = minecraft.Minecraft.create()

def build_tower(height):
    pos = mc.player.getPos()
    mc.setBlocks(pos.x, pos.y, pos.z, 
                 pos.x, pos.y + height, pos.z, 
                 block.STONE.id)
    mc.setBlock(pos.x, pos.y + height + 1, pos.z, 
                block.GOLD_BLOCK.id)

# første tårn - 10 blokke
build_tower(10)
time.sleep(5)
# andet tårn - 15 blokke            
build_tower(15)
time.sleep(5)
# tredje tårn - 20 blokke            
build_tower(20)