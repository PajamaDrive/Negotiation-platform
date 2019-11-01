import json

class History:
    def __init__(self):
        self.__event_number = 1
        self.__history = {}

    """
    json format
    {
        event_number : {
            event_type :
            event_time :
            negotiator_type :
            event_detail : {

            }
        }
    }
    """

    def addHistory(self, json_format_event):
        self.__history[self.__event_number] = json_format_event
        self.__event_number += 1

    def saveHistoryToJSONFile(self, file_name):
        fp = open(file_name + ".json", "w")
        json.dump(self.__history, file, indent = 4)

    def getHistoryNumber(self):
        return self.__event_number

    def getCurrentGameTime(self):
        return time
