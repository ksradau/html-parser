from functions import *

number_of_words = 10

urls = get_urls_from_file()

for url in urls:
    text = get_text_from_page(url)
    clean_text = get_clean_text(text)
    most_common_words = get_top_words_from_text(clean_text, number_of_words)
    print(beautiful_output_for_common_words(most_common_words))
