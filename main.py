from flask import Flask
from flask import render_template
import json
import csv
import pandas as pd
from flask_sqlalchemy import SQLAlchemy

#the goal of this is to grab the spotify playlist with ID 3To0rDryJknvoWZaiaW34z
    #take the data from that (song name, song ID, song parent albumn, song release date) and put it into a database file
#Secondarily, use the SteamAPI to get game information from my profile