"""
Eksempel på at finde spillerens placering og bruge den
til at placere blokke. Fra dag 2.
I eksemplet sættes TNT over spilleren og over TNT sættes ild.
"""

import mcpi.minecraft as minecraft
import mcpi.block as block
from time import sleep

mc = minecraft.Minecraft.create()

while True:
    pos = mc.player.getPos()
    mc.setBlock(pos.x, pos.y + 2, pos.z, block.TNT.id)
    mc.setBlock(pos.x, pos.y + 3, pos.z, block.FIRE.id)

    sleep(1)