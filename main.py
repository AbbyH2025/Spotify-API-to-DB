from flask import Flask
from flask import render_template
import json
import csv
import pandas as pd
from flask_sqlalchemy import SQLAlchemy
import os 
import sys
import spotipy.util as util
import webbrowser
import spotipy
from json.decoder import JSONDecodeError
from APIKey import apiKey

#the goal of this is to grab the spotify playlist with ID 3To0rDryJknvoWZaiaW34z
    #take the data from that (song name, song ID, song parent albumn, song release date) and put it into a database file
#Secondarily, use the SteamAPI to get game information from my profile
#user ID
#z9xc6iyksrgs1p8ekhjqklyyn
# get user ID 
username = input('Spotify User name: ')

scope = 'playlist-read-private' 
client_id = 'ec039216d41f4f9ea4585292828f6077'
client_secret = apiKey
redirect_uri = 'https://www.google.com/callback/'
#erase cache and prompt for user permision
try: 
    token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)
except:
    os.remove(f'.cache-{username}')
    token = util.prompt_for_user_token(username)
#create our spoityfy oobject
spotifyObject = spotipy.Spotify(auth=token)

# print(json.dumps(VARIABLE, sort_keys=True, indent=4))

user = spotifyObject.current_user()

#https://www.youtube.com/watch?v=vipVEWe86Lg