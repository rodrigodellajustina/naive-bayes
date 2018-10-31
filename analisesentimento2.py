from goose3 import Goose

url = 'https://economia.uol.com.br/cotacoes/noticias/redacao/2018/10/16/dolar-bolsa-operam-cotacoes.htm'
g = Goose()
article = g.extract(url=url)
print(article.title)

print(article.cleaned_text)

words = article.cleaned_text

import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords
...
stops = set(stopwords.words("portuguese"))
words = ' '.join([w for w in words if not w in stops])

print(words)

from pandas import DataFrame