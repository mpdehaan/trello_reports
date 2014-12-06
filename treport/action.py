import os
import json

class Action(object):
    # activity on a card
 
    def __init__(self, data):
        self._data = data
        self._info = data['data']
        self._type = data['type']
        print self._data

    def name(self):
        return self._type

    def vivify(self):
        self._info.update(self._data)
        if self._type == 'commentCard':
            return CommentCard(self._info)
        elif self._type == 'updateCard':
            return UpdateCard(self._info)
        else:
            print json.dumps(self._info, indent=4, sort_keys=True)
            raise Exception("no handling coded for: %s" % self._type)

class CommentCard(object):

    def __init__(self, data):
        self._data = data

    def board(self):
        # hash of id, name, shortLink
        return self._data['board']
        
    def card(self):
        # hash of id, idShort, name, shortLink
        return self._data['card']

    def text(self):
        return self._data['text']

    def date(self):
        # FIXME: make real date
        return self._data['date']

    def id(self):
        return self._data['id']

    def id_member_creator(self):
        return self._data['idMemberCreator']

    def creator(self):
        # hash of avatarHash, fullName, id, initials (string), username (string)
        return self._data['memberCreator']

class UpdateCard(object):

    def __init__(self, data):
        self._data = data

    def board(self):
        # hash of id, name, shortLink
        return self._data['board']

    def card(self):
        # hash of id, idList, idShort, name, shortLink
        return self._data['card']
   
    def list_after(self):
        # hash of id, name
        return self._data['listAfter']    
   
    def list_before(self):
        # hash of id, name
        return self._data['listBefore']

    def old(self):
        # ???
        return self._data['old']  
    
    def date(self):
        # FIXME:
        return self._data['date']

    def creator(self):
        # hash of avatarHash, fullName, id, initials (string), username (string)
        return self._data['memberCreator']
