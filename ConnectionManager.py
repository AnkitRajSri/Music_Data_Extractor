import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from sqlalchemy import create_engine

project_folder = os.path.expanduser(r'C:\Users\sriva\OneDrive\Desktop\MusicDataExtractor')
load_dotenv(os.path.join(project_folder, '.env'))
os.chdir(r'C:\Users\sriva\OneDrive\Desktop\MusicDataExtractor')

class ConnectionManager:
    def __init__(self):
        self.CLIENT_ID = os.environ.get('CLIENT_ID')
        self.CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
        self.CONNECTION_STRING = os.environ.get('CONNECTION_STRING')

    def spotify_connection(self):
        client_credentials_manager = SpotifyClientCredentials(self.CLIENT_ID, self.CLIENT_SECRET)
        sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
        return sp

    def database_connection(self):
        engine = create_engine(self.CONNECTION_STRING)
        return engine
