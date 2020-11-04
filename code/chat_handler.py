from mcpi.minecraft import Minecraft


def get_latest_message(mc):
    chatEvents = mc.events.pollChatPosts()
    if len(chatEvents) > 0:
        return chatEvents[-1].message
    else:
        return None
