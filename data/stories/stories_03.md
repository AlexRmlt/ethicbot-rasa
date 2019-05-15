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

## Generated Story -5316799613091547610
* greeting
    - action_intro
* stakeholder{"GPE": "Heather", "plural": "singular"}
    - slot{"plural": "singular"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - utter_ask_name_singular
* name{"GPE": "Heather"}
    - action_update_stakeholder
    - slot{"PERSON": "Frank"}
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"PERSON": "frank", "CARDINAL": "three", "plural": "unspecific_plural", "moralstatus": "human"}
    - slot{"PERSON": "frank"}
    - slot{"moralstatus": "human"}
    - slot{"plural": "unspecific_plural"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": true}
    - utter_ask_quantity
* quantity{"stakeholder": "three people", "CARDINAL": "Three"}
    - action_update_stakeholder
    - slot{"plural": "specific_plural"}
    - slot{"action_return": true}
    - utter_ask_name_plural
* dontknow
    - action_update_stakeholder
    - slot{"PERSON": "the Saxons"}
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"CARDINAL": "One", "plural": "singular"}
    - slot{"plural": "singular"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": true}
    - utter_ask_name_singular
* dontknow
    - action_update_stakeholder
    - slot{"PERSON": "J\u00f6rg"}
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
* decider{"name": "Frank"}
    - action_update_stakeholder
    - slot{"decider": "Frank"}
    - slot{"action_return": true}
    - utter_ask_options
* option{"deed": "refuse to give the injured person"}
    - slot{"deed": "refuse to give the injured person"}
    - action_create_option
    - slot{"deed": "refuse to give the injured person"}
    - slot{"option": 4}
    - slot{"action_return": true}
    - utter_ask_identified_deed
* correct
    - action_create_deed
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
* deed
    - action_create_deed
    - slot{"deed": "It would also mean saving the rest of the crew"}
    - slot{"action_return": true}
    - utter_ask_universalizable
* correct
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deny
    - utter_ask_consequences
* consequence{"PERSON": "frank", "sentiment": "neu"}
    - slot{"PERSON": "frank"}
    - slot{"sentiment": "neu"}
    - action_create_consequence
    - slot{"action_return": false}
    - utter_ask_impact
* positive
    - action_update_consequence
    - slot{"action_return": false}
    - utter_ask_impact_weight
* quantity{"CARDINAL": "8"}
    - action_update_consequence
    - slot{"action_return": false}
    - utter_next_consequence
* consequence{"PERSON": "J\u00f6rg", "sentiment": "neg"}
    - slot{"PERSON": "J\u00f6rg"}
    - slot{"sentiment": "neg"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_negative
* correct
    - action_update_consequence
    - slot{"action_return": false}
    - utter_ask_impact_weight
* quantity{"CARDINAL": "10"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* deny
    - utter_next_option
* option{"PERSON": "J\u00f6rg"}
    - slot{"PERSON": "J\u00f6rg"}
    - action_create_option
    - slot{"deed": null}
    - slot{"option": 9}
    - slot{"action_return": true}
    - utter_ask_deed
* deed{"PERSON": "Saving J\u00f6rgs"}
    - slot{"PERSON": "Saving J\u00f6rgs"}
    - action_create_deed
    - slot{"deed": "Saving J\u00f6rgs live would be a moral action"}
    - slot{"action_return": true}
    - utter_ask_universalizable
* correct
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deny
    - utter_ask_consequences
* consequence{"PERSON": "J\u00f6rg", "sentiment": "pos"}
    - slot{"PERSON": "J\u00f6rg"}
    - slot{"sentiment": "pos"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_positive
* correct
    - utter_ask_impact_weight
* quantity{"CARDINAL": "9"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* consequence{"PERSON": "the saxons", "ORG": "Saxons"}
    - slot{"PERSON": "the saxons"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_positive
* wrong
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_impact_weight
* quantity{"CARDINAL": "5"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* deny
    - utter_next_option
* deny
    - utter_got_everything
    - utter_ask_method
* utilitarism
    - action_evaluation_utilitarism
    - utter_next_method
* deny
    - utter_goodbye

