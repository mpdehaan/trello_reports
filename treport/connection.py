from board import Board
from card import Card
from organization import Organization
from action import Action
import os
import json
import requests

class Connection(object):

   def __init__(self, base='api.trello.com', version='1', key=None, token=None):
       self.base = base
       self.version = version
       self.key = key
       self.token = token

   def _get(self, url):
       url2 = url
       if self.key is not None:
           url2 = url2 + "?key=%s" % self.key
       if self.token is not None:
           url2 = url2 + "&token=%s" % self.token
       r = requests.get(url2)
       status_code = r.status_code
       if status_code != 200:
          raise Exception("invalid status code: %s on %s" % (status_code, url2))
       return r.json()

   def base_url(self):
       return "https://%s/%s" % (self.base, self.version)

   def organizations(self):
       url = "%s/members/my/organizations" % (self.base_url())
       data = self._get(url)
       return [ Organization(o) for o in data ]

   def boards(self, organization=None):
       url = "%s/organizations/%s/boards" % (self.base_url(), organization.organization_id())
       data = self._get(url)
       return [ Board(b) for b in data ]

   def board(self, board_number=None):
       url = "%s/boards/%s" % (self.base_url(), board_number)
       data = self._get(url)
       return Board(data)

   def cards(self, board=None):
       url = "%s/boards/%s/cards" % (self.base_url(), board.board_id())
       data = self._get(url)
       return [ Card(d) for d in data ]

   def actions(self, card=None):
       url = "%s/cards/%s/actions" % (self.base_url(), card.card_id())
       data = self._get(url)
       return [ Action(a) for a in data ]

if __name__ == '__main__':
    key = os.getenv('TRELLO_KEY',None)
    token = os.getenv('TRELLO_TOKEN',None)
    conn = Connection(key=key,token=token)
    board = conn.board(board_number='4d5ea62fd76aa1136000000c')
    cards = conn.cards(board=board)
    actions = conn.actions(card=cards[0])
    for a in actions:
       print json.dumps(a._data, indent=4, sort_keys=True)
       raise Exception("STOP")





