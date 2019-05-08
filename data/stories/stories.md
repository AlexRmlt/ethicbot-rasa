## Generated Story -8310868963727852152
* greeting
    - action_intro
* stakeholder{"ORG": "Mark", "plural": "singular", "moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - slot{"plural": "singular"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - utter_ask_name_singular
* name{"PERSON": "Mark"}
    - slot{"PERSON": "Mark"}
    - action_update_stakeholder
    - slot{"PERSON": "Mark"}
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"plural": "unspecific_plural", "moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - slot{"plural": "unspecific_plural"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": false}
    - utter_ask_quantity
* dontknow
    - utter_ask_guess_quantity
* quantity{"CARDINAL": "5"}
    - action_update_stakeholder
    - slot{"plural": "specific_plural"}
    - slot{"action_return": true}
    - utter_ask_name_plural
* deny
    - action_update_stakeholder
    - slot{"PERSON": "the Hessians"}
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"plural": "singular"}
    - slot{"plural": "singular"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": true}
    - utter_ask_name_singular
* name{"PERSON": "Achmed"}
    - slot{"PERSON": "Achmed"}
    - action_update_stakeholder
    - slot{"PERSON": "Achmed"}
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* deny
    - utter_confirm_stakeholders
    - action_choose_decider
* decider{"name": "Mark"}
    - action_update_stakeholder
    - slot{"decider": "Mark"}
    - slot{"action_return": true}
    - utter_ask_options
* option{"ORG": "Mark"}
    - action_create_option
    - slot{"deed": null}
    - slot{"option": 4}
    - slot{"action_return": true}
    - utter_ask_deed
* deed{"PERSON": "Achmed"}
    - slot{"PERSON": "Achmed"}
    - action_create_deed
    - slot{"deed": "It would mean crushing Achmed and killing him"}
    - slot{"action_return": true}
    - utter_ask_universalizable
* wrong
    - action_update_deed
    - slot{"action_return": true}
    - utter_ask_inherent_evil
* affirm
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deed{"deed": "rescuing"}
    - slot{"deed": "rescuing"}
    - utter_ask_identified_deed
* correct
    - action_create_deed
    - slot{"action_return": true}
    - utter_ask_universalizable
* correct
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deny
    - utter_ask_consequences
* consequence{"sentiment": "neg"}
    - slot{"sentiment": "neg"}
    - action_create_consequence
    - utter_ask_impact_negative
* correct
    - utter_ask_impact_weight
* quantity{"CARDINAL": "10"}
    - action_update_consequence
    - slot{"action_return": false}

## Generated Story -4386739142444682408
* greeting
    - action_intro
* stakeholder{"plural": "singular"}
    - slot{"plural": "singular"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - utter_ask_name_singular
* name{"PERSON": "Johannes"}
    - slot{"PERSON": "Johannes"}
    - action_update_stakeholder
    - slot{"PERSON": "Johannes"}
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder

## Generated Story -975241215883549483
* greeting
    - action_intro
* stakeholder{"plural": "unspecific_plural"}
    - slot{"plural": "unspecific_plural"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": false}
    - utter_ask_quantity
* quantity{"CARDINAL": "one"}
    - action_update_stakeholder
    - slot{"plural": "singular"}
    - slot{"action_return": true}
    - utter_ask_name_singular
* deny
    - action_update_stakeholder
    - slot{"PERSON": "Samuel"}
    - slot{"action_return": true}
    - utter_ask_moral_status

