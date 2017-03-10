import json
import re
from collections import Counter
from html.parser import HTMLParser
  
pattern = r'\b[a-zA-Zа-яА-Я]{1}[a-zA-Zа-яА-Я\-]{5,}[a-zA-Zа-яА-Я]{1}\b'

json_file = open('newsafr.json', encoding='UTF-8')
json_news = json.load(json_file)

news =  json_news['rss']['channel']['item']
words = []

for news_item in news:
	news_words = news_item['description']['__cdata']
	suitable_words = re.findall(pattern, news_words)
	words = words + suitable_words
words_count = Counter(words)
top10 = words_count.most_common(10)
for item in top10:
	print (item[0] + ', ' + '%d раз(а)' % (item[1]))	