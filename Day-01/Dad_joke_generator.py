import random
import requests

categories_url = "https://api.chucknorris.io/jokes/categories"
response = requests.get(categories_url, timeout=10)
response.raise_for_status()

categories = response.json()
selected_categories = random.sample(categories, k=min(5, len(categories)))

print("Here are 5 random joke categories and one joke from each:\n")

for category in selected_categories:
    joke_response = requests.get(
        f"https://api.chucknorris.io/jokes/random?category={category}",
        timeout=10,
    )
    joke_response.raise_for_status()
    joke_data = joke_response.json()

    print(f"Category: {category}")
    print(f"Joke: {joke_data['value']}")
    print("-" * 70)
