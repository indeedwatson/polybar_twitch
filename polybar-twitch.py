#!/bin/python
import requests
import time
import itertools
import settings
from settings import username

def getID(client, user):
    '''
    Get the user id from the twitch login username
    '''
    r = requests.get('https://api.twitch.tv/helix/users?login=' + user, \
            headers = client)
    data = r.json()
    reqID = data['data'][0]['id']
    return reqID


def getFollowedChans(client, user):
    '''
    return a list of all the user id's followed by the given user id
    '''
    r = requests.get('https://api.twitch.tv/helix/users/follows?from_id=' \
            + user, headers = client)
    data = r.json()
    # look into this with mpas
    followedChans = list()
    for i in data['data']:
        followedChans.append(i['to_id'])
    return followedChans


def getOnlineChans(channels, headers):
    '''
    Check followed channels to see which are streaming, make a dict with the
    channel name, containing the game name
    '''
    onlineChans = {}
    for stream in itertools.cycle(channels):
        r = requests.get('https://api.twitch.tv/kraken/streams/' + stream, \
                headers = headers)
        online = r.json()
        if online['stream'] != None:
            # stream = online['stream']['channel']['_id']
            # make a dict with the display_name as the stream, containing 
            # selected attr from the dict
            onlineChans[stream] = {'name': \
                    online['stream']['channel']['display_name'], \
                    'game': online['stream']['game']}
            printStreams(onlineChans.items())
            time.sleep(10)

    #return onlineChans

def printStreams(dic):
    for chan, info in dic:
        print('{}: {}'.format(info.get('name'), info.get('game')))

#username = 'tacticcarrotcake'
headers = {'Client-ID': 'l62zpdkfreec6bbsoffjw0lyjtiwkc',
         'Accept': 'application/vnd.twitchtv.v5+json'}

if __name__ == "__main__":
    if username:
        userID = getID(headers, username)
        onlineChans = getOnlineChans(getFollowedChans(headers, userID), headers)
    else:
        print('Invalid or empty Twitch username.\nWrite your username in the '
        'settings.py file')
