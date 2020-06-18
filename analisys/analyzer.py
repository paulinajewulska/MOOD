import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords

#nltk.download('stopwords')
#set(stopwords.words('english'))


def analyzer(text):
    stop_words = stopwords.words('english')
    text1 = text
    processed_doc1 = ' '.join([word for word in text1.split() if word not in stop_words])
    sa = SentimentIntensityAnalyzer()
    dd = sa.polarity_scores(text=processed_doc1)
    compound = round((1 + dd['compound']) / 2, 2)
    return compound
