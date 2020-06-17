from functions import *

number_of_words = 10

urls = get_urls_from_file()

for url in urls:
    text = get_text_from_page(url)
    most_common_words = get_top_words_from_text(text, number_of_words)

