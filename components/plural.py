from rasa_nlu.components import Component
from rasa_nlu import utils
from rasa_nlu.model import Metadata
import modules.constants as const
import modules.nlu_helper as nlu

class PluralAnalyzer(Component):
    """Identify plural expressions"""

    name = "plural"
    provides = ["entities"]
    requires = ["entities"]
    defaults = {}
    language_list = ["en"]

    def __init__(self, component_config=None):
        super(PluralAnalyzer, self).__init__(component_config)

    def get_plural(self, text):
    	with open(const.FILE_PLURAL_WORDS) as file:
            plw = file.read().split(' ')
            if any(w in text.lower() for w in plw):
                return True
    	return False

    def convert_to_rasa(self, value, confidence):
        """Convert model output into the Rasa NLU compatible output format."""
        
        entity = {"start": 0,
        		  "end": 0,
        		  "value": value,
                  "confidence": confidence,
                  "entity": 'plural',
                  "extractor": "plural_extractor"}

        return entity


    def process(self, message, **kwargs):  	
        extracted = []

        # Are there words in the message indicating plural?
        assumed_plural = self.get_plural(message.text)

        # Is there a quantity indicating plural?
        entities = message.get("entities")
        quantity = -1
        for ent in entities:
            if (ent['entity'] == 'stakeholder'):  
                quantity = nlu.get_quantity(ent['value'])
                break
            
        if quantity > 1:
            assumed_plural = True

        if not assumed_plural:
            plural = const.SINGULAR
        else:
            if quantity > 1:
                plural = const.SPECIFIC_PLURAL
            else:
                plural = const.UNSPECIFIC_PLURAL

        extracted.append(self.convert_to_rasa(plural, 1))

        message.set("entities",
            message.get("entities", []) + extracted,
            add_to_output=True)