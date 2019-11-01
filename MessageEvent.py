class MessageEvent(Event):
    def __init__(self, negotiator_id, opponent_id, message):
        super()__init__(negotiator_id)
        self.event_type = message.__class__.__name__
        self.opponent_id = opponent_id
        self.message = message

    def makeJSONFormatEvent(self, history_number, event_time):
        offer_event_json = {
            history_number : {
                "eventtype" : self.event_type,
                "event_time" : event_time,
                "negotiator_id" : self.negotiator_id,
                "event_detail" : {
                    "opponent_id" : self.opponent_id,
                    "message" : message.strToDict()
                }
            }
        }
        return offer_event_json
