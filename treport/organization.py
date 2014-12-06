import os
import json

class Organization(object):
 
    def __init__(self, data):
        self._data = data

    def billable_member_count(self):
        return self._data['billableMemberCount']

    def desc(self):
        return self._data['desc']

    def display_name(self):
        # this is the org name really
        return self._data['displayName']

    def organization_id(self):
        return self._data['id']
    
    def board_ids(self):
        # array of ids
        return self._data['idBoards']
 
    # "invitations": [], 
    # "invited": false, 
    # "logoHash": null, 

    def memberships(self):
        return self._data['memberships']
        # array of hashes of things like
        #{
        #    "deactivated": false, 
        #    "id": "goes here"
        #    "idMember": "goes here"
        #    "memberType": "admin", # or normal 
        #    "unconfirmed": false
        #}

    def name(self):
        return self._data['name']

    def power_ups(self):
        # array of integers
        return self._data['power_ups']
 
    # prefs -> hash
    # premiumFeatures -> list of strings
    # products -> list of integers

    def url(self):
        return self._data['url']
  
    # "website": null

