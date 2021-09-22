import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.entity as entity
import time
mc = minecraft.Minecraft.create()



while True:	
  pos = mc.player.getPos()
  mc.setBlock(pos.x, pos.y-1, pos.z, block.WOOD.id)
  time.sleep(0.1)