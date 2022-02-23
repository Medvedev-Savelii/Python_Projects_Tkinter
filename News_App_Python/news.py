import requests
import tkinter as tk

def getNews():
	api_key = "acda8e1f7824400daf099f6b4a088925"
	url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=" +api_key
	news = requests.get(url).json()

	articles = news["articles"]

	my_articles = []
	my_news = ''

	for article in articles:
		my_articles.append(article["title"])


	for i in range(10):
		my_news = my_news + str(i) + ". " + my_articles[i] + "\n"

	label.config(text= my_news)

canvas = tk.Tk()
canvas.geometry("900x600")
canvas.title("News App")

button = tk.Button(canvas, font = 24, text = "Reload", command = getNews)
button.pack(pady = 20)

label = tk.Label(canvas, font = 18, justify="left")
label.pack(pady = 20)




canvas.mainloop()
