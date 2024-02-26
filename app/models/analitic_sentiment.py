import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')
from translate import Translator
import random
from app.models.jsons.sentiment_positive import getResponse_positive
from app.models.jsons.sentiment_negative import getResponse_negative
from app.models.jsons.sentiment_neutre import getResponse_neutre

class Sentiment:
    def __init__(self, sentiment):
        self.sentiment = sentiment

    def get(self):
        return self.sentiment
    
    def instance(self):

        TO_EN = Translator(to_lang='en', from_lang='pt')

        sentiment_en = TO_EN.translate(self.sentiment)

        sentimentIntensity = SentimentIntensityAnalyzer()
        instance_sentiment = sentimentIntensity.polarity_scores(sentiment_en)
        return instance_sentiment
    
    def execute(self):
        instance_sentiment = self.instance()

        print(f'Nova Instance >>> {instance_sentiment}')

        if instance_sentiment['pos'] > instance_sentiment['neg'] and instance_sentiment['pos'] > instance_sentiment['neu']:
            # sentimento positivo
            id = sorter_frase()
            frase = getResponse_positive(id)
            return frase
        elif instance_sentiment['neg'] > instance_sentiment['pos'] and instance_sentiment['neg'] > instance_sentiment['neu']:
            #sentimento negativo
            id = sorter_frase()
            frase = getResponse_negative(22)
            return frase
        else:
            #sentimento neutro
            id = sorter_frase()
            frase = getResponse_neutre(id)
            return frase
        
def sorter_frase():
    id = random.randint(0,45)
    return id


    

