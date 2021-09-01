import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
mc.postToChat("Her er en lille gave til dig")
pos = mc.player.getPos()
print(pos.x)
"""
for i in range(0, 100):
    mc.setBlock(pos.x+i, pos.y, pos.z, block.TNT.id)
    mc.setBlock(pos.x+i, pos.y+1, pos.z, block.FIRE.id)
"""
# create stone shell
mc.setBlocks(pos.x, pos.y, pos.z, pos.x+5, pos.y+5, pos.z+5, block.STONE.id)
# fill with tnt
mc.setBlocks(pos.x+1, pos.y+1, pos.z+1, pos.x+5-1,
             pos.y+5-1, pos.z+5-1, block.TNT.id)
# switch out a top stone with fire
mc.setBlock(pos.x+1, pos.y+5, pos.z+1, block.FIRE.id)