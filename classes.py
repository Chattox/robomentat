# Robomentat classes

# User class
class User:
    def __init__(self, userid):
        self.userid = userid
    name = ''
    # (Voice channel ID : (Channel name : time spent in it))
    voiceChannels = {}
    # (Text channel ID : (Channel name : # of messages sent))
    textChannels = {}

# Channel class, for both voice and text
class Channel:
    def __init__(self, channelid):
        self.channelid = channelid
    name = ''
    # Whether the channel is voice or not
    isVoice = ''
    # (User ID : (User name : time spent in channel))
    voiceUsage = {}
    # (User ID : (User name : # of messages sent))
    textUsage = {}