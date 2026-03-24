import requests
from collections import Counter
import string

def fetch_text(url, timeout=10):
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Ошибка загрузки {url}: {e}")
        return None

def clean_word(word):
    return word.lower().strip(string.punctuation)

def main():
    words_file = "words.txt"
    url = "https://eng.mipt.ru/why-mipt/"

    print("Загрузка страницы...")
    text = fetch_text(url)
    if text is None:
        return

    raw_words = text.split()
    words = [clean_word(w) for w in raw_words]

    freq_counter = Counter(words)

    try:
        with open(words_file, 'r') as f:
            target_words = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Файл {words_file} не найден.")
        return

    frequencies = {}
    for word in target_words:
        cleaned = clean_word(word)
        frequencies[word] = freq_counter.get(cleaned, 0)

    print(frequencies)

if __name__ == "__main__":
    main()