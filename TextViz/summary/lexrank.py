# from sumy.summarizers.lex_rank import LexRankSummarizer
# from sumy.parsers.plaintext import PlaintextParser
# from sumy.nlp.tokenizers import Tokenizer
# from sumy.summarizers.lsa import LsaSummarizer
# import nltk
# from . import web_scraper
# nltk.download('punkt')



# def output(text,nol):
#     text=str(text).lower()
#     parser=PlaintextParser.from_string(text,Tokenizer("english"))

#     # creating object of class
#     summarizer_lex=LexRankSummarizer() 

#     # textrank
#     summary=summarizer_lex(parser.document,nol)

#     for sentence in summary:
#         print(sentence)

# LSA
# lsa_summarizer = LsaSummarizer()
# summary = lsa_summarizer(parser.document,10)
# for sentence in summary:
#     print(sentence)
# LEX_out=output(web_scraper.urls,20)