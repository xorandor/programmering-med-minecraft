from mcpi.minecraft import Minecraft

# poll the server for the latest messages
def get_latest_message(mc):
    chatEvents = mc.events.pollChatPosts()
    if len(chatEvents) > 0:
        return chatEvents[-1].message
    else:
        return None
