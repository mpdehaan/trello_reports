import os
import json

class Board(object):
 
   def __init__(self, data):
      self._data = data

   def is_closed(self):
      return self._data['closed']

   def description(self):
      return self._data['desc']

   def board_id(self):
      return self._data['id']

   def organization_id(self):
      return self._data['idOrganization']

   def label_names(self):
      # a hash of color => label name
      return self._data['labelNames']

   def name(self):
      return self._data['name']

   def is_pinned(self):
       return self._data['is_pinned']

   def prefs(self):
       # returns a hash, keys include:
       #  "canBeOrg": false, 
       #  "canBePrivate": false, 
       #  "canBePublic": false, 
       #  "canInvite": true, 
       #  "cardCovers": true, 
       #  "comments": "public", 
       #  "invitations": "members", 
       #  "permissionLevel": "public", 
       #  "selfJoin": false, 
       #  "voting": "public"
       return self._data['prefs']

   def short_url(self):
       return self._data['short_url']

   def url(self):
       return self._data['url']


