import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.entity as entity
import time
mc = minecraft.Minecraft.create()

pos = mc.player.getPos()

x0 = pos.x
y0 = pos.y
z0 = pos.z

def pyramide(height):
    for i in range(0, height):
        bredde = height * 2 - 2
        mc.setBlocks(x0 + i, i, z0 + i, x0 + bredde - i, i, z0 + bredde - i, block.DIAMOND_BLOCK.id)
        mc.setBlocks(x0 + i + 1, i, z0 + i + 1, x0 + bredde - i - 1, i, z0 + bredde - i - 1, block.AIR.id)

pyramide(10)
