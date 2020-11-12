import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.entity as entity
import time
mc = minecraft.Minecraft.create()

while True:
    pos = mc.player.getPos()
    mc.spawnEntity(pos.x, pos.y+2, pos.z, entity.COW.id)
    time.sleep(0.5)