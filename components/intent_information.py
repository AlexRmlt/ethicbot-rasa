from rasa_nlu.components import Component
from rasa_nlu import utils
from rasa_nlu.model import Metadata
import modules.constants as const
import modules.nlu_helper as nlu
import os

class IntentInformation(Component):
    """Sentiment identification"""

    name = "intent_information"
    provides = ["entities"]
    requires = ["entities"]
    defaults = {}
    language_list = ["en"]

    def __init__(self, component_config=None):
        super(IntentInformation, self).__init__(component_config)


    def convert_to_rasa(self, entity, value, confidence=1, start=0, end=0):
        """Convert model output into the Rasa NLU compatible output format."""
        
        entity = {"start": start,
        		  "end": end,
        		  "value": value,
                  "confidence": confidence,
                  "entity": entity,
                  "extractor": "intent_information_extractor"}

        return entity

    def process(self, message, **kwargs):  	
        """ 
        Extract additional information for intents:
        
        * Consequence:
        ** sentiment

        * Stakeholder:
        ** plural
        ** moralstatus 
        
        """
        extracted = []
        try:
            intent = message.get('intent')['name']
        except KeyError:
            intent = None

        if (intent == 'consequence'):
            # Get sentiment
            sentiment, confidence = nlu.get_sentiment(message.text)
            extracted.append(self.convert_to_rasa('sentiment', sentiment, confidence))
        elif (intent == 'stakeholder' or intent == 'decider'):
            entities = message.get("entities")

            stakeholder = None
            for ent in entities:
                if (ent['entity'] == 'stakeholder'):  
                    stakeholder = ent['value']
                    break
            # Get plural or singular
            # DEPRECATED: Replaced by own intent 'stakeholdergroup'
            """
            plural = nlu.get_plural(message.text, stakeholder)
            extracted.append(self.convert_to_rasa('plural', plural))"""

            # Get moral status
            moralstatus = nlu.get_moral_status(stakeholder)
            if not moralstatus == None: 
                extracted.append(self.convert_to_rasa('moralstatus', moralstatus))

        message.set("entities",
                message.get("entities", []) + extracted,
                add_to_output=True)