import mcpi.block as block

def build_2d_statue(mc, sketch, axis="x"):
    pos = mc.player.getPos()

    # height of the statue
    height = sketch.count("\n") - 1
    # width of the statue
    width = max([len(row) for row in sketch.split("\n")])

    # start coordinates
    y = pos.y + height

    if axis == "x":
        x = pos.x
        z = pos.z + width // 2
    elif axis == "z":
        x = pos.x + width // 2
        z = pos.z

    # draw each block
    for i in sketch:
        if i == "\n":
            # we have reached end of a line, go down and back to starting coordinate
            y -= 1

            if axis == "x":
                x = pos.x
                z = pos.z + width // 2
            elif axis == "z":
                x = pos.x + width // 2
                z = pos.z
        else:
            # figure out which block to build
            if i == "1":
                blockType = block.IRON_BLOCK.id
            if i == "2":
                blockType = block.WOOD.id
            if i == "3":
                blockType = block.STONE.id
            if i == "#":
                blockType = block.COBBLESTONE.id
            if i == "X":
                blockType = block.TNT.id
            if i == " ":
                blockType = block.AIR.id

            # set block at the current coordinate
            mc.setBlock(x, y, z + width//2, blockType)
            # move one to the side
            if axis == "x":
                x += 1
            elif axis == "z":
                z += 1

def build_3d_statue(mc, sketch):
    build_2d_statue(mc, sketch, "x")
    build_2d_statue(mc, sketch, "z")
