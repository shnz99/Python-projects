from bs4 import BeautifulSoup
import requests
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint

YEAR = input(
    "Which year do you want to travel to? Type the date in this format YYYY-MM-DD:\n"
)

spotify_id = os.environ.get("SPOTIFY_ID")
spotify_secret = os.environ.get("SPOTIFY_SECRET")
spotify_user = os.environ.get("SPOTIFY_USER")

pp = pprint.PrettyPrinter()
auth_manager = SpotifyOAuth(
    client_id=spotify_id,
    client_secret=spotify_secret,
    redirect_uri="http://example.com",
    scope="playlist-modify-private",
)
sp = spotipy.Spotify(auth_manager=auth_manager)
list_of_urls = []

###################################### download 100 songs from desired time #########################################################
response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{YEAR}/")
soup = BeautifulSoup(response.text, "html.parser")

titles = soup.select(".chart-results-list .o-chart-results-list__item h3")
###################################### #################################### #########################################################

for title in titles:
    result = sp.search(
        q=f"track: {title.getText().strip()} year: {YEAR[:4]}",
        limit=1,
        offset=0,
        type="track",
        market=None,
    )
    # pp.pprint(result)
    list_of_urls.append(result["tracks"]["items"][0]["uri"])

print(list_of_urls)
