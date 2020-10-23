import json
from pprint import pprint
from collections import Counter
from hw_dec_2 import new_function

with open('C:/Users/79035/Desktop/py-33/old/hw-data_format/newsafr.json', encoding="utf-8") as f:
    json_file = json.load(f)

@new_function('log_code.txt')
def top_10_json(file_name):
    file_1 = file_name["rss"]["channel"]["items"]
    words_list = []
    final_words = []
    for news in file_1:
        news_descr = news['description']
        words_list = news_descr.split(' ')
        for words in words_list:
            if len(words) > 6:
                final_words.append(words)
    final_dict= Counter(final_words)
    for word, quantity in final_dict.most_common(10):
        pprint(word)

