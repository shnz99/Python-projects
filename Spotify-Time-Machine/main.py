from bs4 import BeautifulSoup
import requests

# Which year do you want to travel to? Type the date in this format YYYY-MM-DD:
YEAR = input(
    "Which year do you want to travel to? Type the date in this format YYYY-MM-DD:\n"
)

contents = requests.get()
soup = BeautifulSoup(contents, "html.parser")
