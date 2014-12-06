from connection import Connection
# from board import Board
# from card import Card
import os
import json
import sys
# import requests


class Analyzer(object):

   def __init__(self, key=None, token=None, organization_filter=None, board_filter=None):
       self.key = key 
       self.token = token
       self.connection = Connection(key=self.key, token=self.token)
       self.organization_filter = organization_filter
       self.board_filter = board_filter

   def analyze(self):

       # TODO: use organization filter setting
       # TODO: use board filter setting

       organizations = self.connection.organizations()

       for organization in organizations:

           print organization.name()

           if organization.name() not in self.organization_filter:
               print "! SKIPPING UNCONFIGURED ORGANIZATION: %s" % org.name()
               continue


           print "- PROCESSING AN ORGANIZATION - %s" % (organization.name())
 
           boards = self.connection.boards(organization)

           for board in boards:

               #board = self.connection.board(board_number=board_number)

               if board.name() not in self.board_filter:
                   print "! SKIPPING UNCONFIGURED BOARD: %s" % board.name()
                   continue

               print "\ PROCESSING A BOARD - %s" % board.name()

               cards = self.connection.cards(board=board) 

               for card in cards:
                   print "| PROCESSING A CARD - %s" % card.name()

                   actions = self.connection.actions(card=card)

                   for action in actions:
                       print "/ PROCESSING AN ACTION - %s" % action.name()
           
                       action_obj = action.vivify()           

                       # TODO: pay attention to dates of new cards
                       # TODO: record comment events
                       # TODO: record changes to listAfter/listBefore on UpdateCard events
              

if __name__ == '__main__':

    def setting(data, which):
        result = data.get(which, None)
        if result is None:
            print sys.stderr, "missing required setting: %s" % which
            sys.exit(1)
        return result

    config = os.getenv('TREPORT_CONFIG',None)
    if config is None:
        print sys.stderr, "environment variable TREPORT_CONFIG not set"
        sys.exit(1)

    # TODO: error handling, meh
    key = None
    token = None
    with open(config) as f:
        data = json.loads(f.read())

    key   = setting(data,'key')
    token = setting(data,'token')
    organization_filter = setting(data, 'organization_filter')
    board_filter = setting(data,'board_filter')

    analyzer = Analyzer(
        key=key, 
        token=token, 
        organization_filter=organization_filter, 
        board_filter=board_filter
    )
    analyzer.analyze()


