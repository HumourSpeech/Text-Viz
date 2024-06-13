# import pandas as pd
# import urllib
# import requests
# from bs4 import BeautifulSoup
# import wikipedia

# # url='https://en.wikipedia.org/wiki/South_Asian_river_dolphin'
# #url='https://www.gutenberg.org/files/11/11-0.txt'


# url=str('https://en.wikipedia.org/wiki/Anime')
# res=requests.get(url)
# html_page=res.content
# print(res)
# check=url.split('/')
# z=check[-1]
# x=z.replace('_',' ')
# df=None
# for i in check:
#        if i=='en.wikipedia.org':
#               results = wikipedia.search(x)
#               page = wikipedia.page(results[0])
#               df = page.content

#        else:
#               soup=BeautifulSoup(html_page,features='html.parser')
#               text=soup.find_all(string=True)
#               lines={line2 for line in text for line2 in
#               line.strip().split('.') if line2}
#               df=pd.DataFrame(lines,columns=['text'])
#               df.replace(to_replace=[r'\\t|\\n|\\r', '\t|\n|\r'],value=['',''],regex=True,inplace=True)
#               df=df.rename_axis('Id',axis='columns')
#               #df.to_csv('test.csv',index_label='Id')

# from sumy.summarizers.lex_rank import LexRankSummarizer
# from sumy.parsers.plaintext import PlaintextParser
# from sumy.nlp.tokenizers import Tokenizer
# from sumy.summarizers.lsa import LsaSummarizer
# import nltk
# nltk.download('punkt')

# text=str(df).lower()
# parser=PlaintextParser.from_string(text,Tokenizer("english"))

#     # creating object of class
# summarizer_lex=LexRankSummarizer()

#     # textrank
# summary=summarizer_lex(parser.document,70)

# for sentence in summary:
#        print(sentence)
# out=sentence