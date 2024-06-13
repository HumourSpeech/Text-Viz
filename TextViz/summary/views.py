from django.shortcuts import render,HttpResponse
# from . import web_scraper
import pandas as pd
import urllib
import requests
from bs4 import BeautifulSoup
import wikipedia
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import nltk
nltk.download('punkt')
# url=str('https://en.wikipedia.org/wiki/Anime')
def smry(u_r_l):
    url=u_r_l
    res=requests.get(url)
    html_page=res.content
    print(res)
    check=url.split('/')
    z=check[-1]
    x=z.replace('_',' ')
    for i in check:
        if i=='en.wikipedia.org':
                results = wikipedia.search(x)
                page = wikipedia.page(results[0])
                df = page.content
                # print(df)
                break
        else:

                try:
                        response = requests.get(url)
                        soup = BeautifulSoup(response.content, 'html.parser')
                        text = soup.get_text()
                        df=text
                except Exception as e:
                        print(f"An error occurred: {e}")
                        return None

    from sumy.summarizers.lex_rank import LexRankSummarizer
    from sumy.parsers.plaintext import PlaintextParser
    from sumy.nlp.tokenizers import Tokenizer
    from sumy.summarizers.lsa import LsaSummarizer
    import nltk
    #nltk.download('punkt')
    text=df
    text=str(text).lower()
    parser=PlaintextParser.from_string(text,Tokenizer("english"))
    summarizer_lex=LexRankSummarizer()
    # textrank
    summary=summarizer_lex(parser.document,5)
    h=str(summary)
    j=h.replace('>, <Sentence:',' ' )

    return j

def popup(request):
    context={}
    if request.method == 'POST':
        # print("reached")
        text=request.POST['textArea']
        #
        url=request.POST['urlArea']
        print('url stored')
        print(url)
        summary=smry(url)
        context={'OUTPUT':summary}
        # return httpResponse(lexrank.LEX_out)
        return render(request,'popup.html',context)
    else:
        return render(request,'popup.html')