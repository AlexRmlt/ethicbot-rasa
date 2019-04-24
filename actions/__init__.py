# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import requests, json
from typing import Dict, Text, Any, List, Union
from rasa_core_sdk import Tracker
from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
from rasa_core_sdk.forms import FormAction

import modules.constants as const
import modules.nlu_helper as nlu

import modules.datamodel.mind as mind
from modules.datamodel import Stakeholder, Option, Consequence, Deed, Context

logger = logging.getLogger(__name__)