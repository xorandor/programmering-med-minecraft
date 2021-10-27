from mcpi.minecraft import Minecraft

# poll the server for the latest messages
def get_latest_message(mc):
    chatEvents = mc.events.pollChatPosts()
    
    if len(chatEvents) > 0:
        #mc.postToChat(chatEvents[-1].message)
        m=chatEvents[-1].message
        return chatEvents[-1].message
    else:
        return None