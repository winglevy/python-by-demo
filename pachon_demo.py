import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_douban_top250():
    url = "https://movie.douban.com/top250"
    headers = {"User-Agent": "Mozilla/5.0"}
    movies = []

    for page in range(0, 250, 25):  # 分页处理
        params = {"start": page}
        response = requests.get(url, headers=headers, params=params)
        soup = BeautifulSoup(response.text, "html.parser")

        for item in soup.select(".item"):
            title = item.select_one(".title").text
            rating = item.select_one(".rating_num").text
            movies.append({"title": title, "rating": rating})

    df = pd.DataFrame(movies)
    df.to_csv("douban_top250.csv", index=False)

scrape_douban_top250()