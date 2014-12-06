import os
import json

class Card(object):
 
    def __init__(self, data):
        self._data = data

    def badges(self):
       # returns a hash with keys like:
       #  "attachments": 1, 
       #  "checkItems": 0, 
       #  "checkItemsChecked": 0, 
       #  "comments": 547, 
       #  "description": true, 
       #  "due": null, 
       #  "fogbugz": "", 
       #  "subscribed": false, 
       #  "viewingMemberVoted": false, 
       #  "votes": 354
      return self._data['badges']

    def check_item_states(self):
        return self._data['checkItemStates']

    def is_closed(self):
        return self._data['closed']

    def last_activity(self):
        # FIXME: convert to python date
        return self._data['dateLastActivity'] 

    def description(self):
        return self._data['desc']
   
    def description_data(self):
        return self._data['desc_data']

    def due(self):
        return self._data['due']

    def email(self):
        return self._data['email']

    def card_id(self):
        return self._data['id']

    # idAttachmentCover
    
    def board_id(self):
        return self._data['idBoard']

    # idChecklists => []
    # idLabels => []
    # idList => scalar
    # idMembers => []
    # idMembersVoted = []
    # idShort

    def labels(self):
       return self._data['labels']
       # array like:
       #[
       #{
       #     "color": "orange", 
       #     "id": "545a3fe374d650d567ab3c75", 
       #     "idBoard": "4d5ea62fd76aa1136000000c", 
       #     "name": "Feature", 
       #     "uses": 205
       #}
       #] 

    # manualCoverAttachment => bool
    
    def name(self):
       return self._data['name']

    def position(self):
       # why is this a float?
       return self._data['pos'] 

    def short_url(self):
       return self._data['shortUrl']

    def url(self):
       return self._data['url']



