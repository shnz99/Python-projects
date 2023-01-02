from bs4 import BeautifulSoup
import requests
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Which year do you want to travel to? Type the date in this format YYYY-MM-DD:
YEAR = input(
    "Which year do you want to travel to? Type the date in this format YYYY-MM-DD:\n"
)
spotify_id = os.environ.get("SPOTIFY_ID")
spotify_secret = os.environ.get("SPOTIFY_SECRET")
spotify_user = os.environ.get("SPOTIFY_USER")

auth_manager = SpotifyOAuth(
    client_id=spotify_id,
    client_secret=spotify_secret,
    redirect_uri="http://example.com",
    scope="playlist-modify-private",
)

sp = spotipy.Spotify(auth_manager=auth_manager)

response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{YEAR}/")
contents = response.text
soup = BeautifulSoup(contents, "html.parser")

titles = soup.select(".chart-results-list .o-chart-results-list__item h3")

with open("100songs.txt", mode="+w") as file:
    for title in titles:
        file.write(f"{title.getText().strip()}\n")
