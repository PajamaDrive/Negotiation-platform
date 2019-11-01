class OfferEvent(Event):
    def __init__(self, event_type, negotiator_id, opponent_id, offer):
        super()__init__(negotiator_id)
        self.event_type = event_type
        self.opponent_id = opponent_id
        self.offer = offer

    def makeJSONFormatEvent(self, history_number, event_time):
        offer_event_json = {
            history_number : {
                "eventtype" : self.event_type,
                "event_time" : event_time,
                "negotiator_id" : self.negotiator_id,
                "event_detail" : {
                    "opponent_id" : self.opponent_id,
                    "offer_detail" : offer.strToDict()
                }
            }
        }
        return offer_event_json
