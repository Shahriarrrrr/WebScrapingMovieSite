import requests
from bs4 import BeautifulSoup
import re
response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
movie_webpage = response.text
soup = BeautifulSoup(movie_webpage,"html.parser")


all_article_tag = soup.find_all(name="h3",class_="title")
all_names_of_movies = [re.sub(r"^\d+\)\s*", "", art.getText()) for art in all_article_tag]
all_names_of_movies.reverse()
print(all_names_of_movies)
with open("movies.txt", "w",encoding="utf-8") as file:
    for names in all_names_of_movies:
        file.write(f"{all_names_of_movies.index(names)+1}) {names}\n")

