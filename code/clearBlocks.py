def clearBlocks():
    pos = mc.player.getPos()
    mod = 1
    xHigh = pos.x+mod
    xLow = pos.x-mod
    yHigh = pos.y+mod
    yLow = pos.y
    zHigh = pos.z+mod
    zLow = pos.z-mod
    y_list = list(range(yHigh-yLow+1))
    y_list.reverse()
    for y in y_list:
        for x in range(xHigh - xLow+1):
            for z in range(zHigh-zLow+1):
                tx = xLow + x
                ty = yLow + y
                tz = zLow + z
                block = mc.getBlock(tx, ty, tz)
                mc.setBlock(tx, ty, tz, 0)
