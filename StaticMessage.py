from EmotionType import *

class StaticMessage:
    def __new__(self):
        raise NotImplementedError('Cannot instantiate this class')

    def getMessageList():
        return [
            ("I\'m happy!", EmotionType.Happy),
            ("I\'m angry!", EmotionType.Angry),
            ("I\'m surprised!", EmotionType.Surprised),
            ("I\'m sad...", EmotionType.Sad)
        ]

    @classmethod
    def getMessage(cls, message_no):
        return StaticMessage.getMessageList()[message_no][0]

    @classmethod
    def getMessageEmotion(cls, message_no):
        return StaticMessage.getMessageList()[message_no][1]

    @classmethod
    def messageToEmotion(self, message):
        return dict(StaticMessage.getMessageList())[message]
