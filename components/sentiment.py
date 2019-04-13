from rasa_nlu.components import Component
from rasa_nlu import utils
from rasa_nlu.model import Metadata
import modules.constants as const

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import os

class SentimentAnalyzer(Component):
    """Sentiment identification"""

    name = "sentiment"
    provides = ["entities"]
    requires = []
    defaults = {}
    language_list = ["en"]

    def __init__(self, component_config=None):
        super(SentimentAnalyzer, self).__init__(component_config)


    def convert_to_rasa(self, value, confidence):
        """Convert model output into the Rasa NLU compatible output format."""
        
        entity = {"start": 0,
        		  "end": 0,
        		  "value": value,
                  "confidence": confidence,
                  "entity": 'sentiment',
                  "extractor": "sentiment_extractor"}

        return entity

    def process(self, message, **kwargs):  	
        """Retrieve the text message, pass it to the classifier
            and append the prediction results to the message class."""

        sid = SentimentIntensityAnalyzer()
        res = sid.polarity_scores(message.text)
        key, value = max(res.items(), key=lambda x: x[1])

        extracted = self.convert_to_rasa(key, value)

        message.set("entities",
                    message.get("entities", []) + [extracted],
                    add_to_output=True)