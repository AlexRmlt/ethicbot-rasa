## Generated Story 5027437522549988447
* greeting
    - action_intro
* greeting
    - utter_greet
    - utter_ask_stakeholders
* stakeholdergroup
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": false}
    - utter_ask_quantity
* quantity{"quantity": "10"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_ask_name_plural
* name
    - action_update_stakeholder
    - slot{"name": "the Bavarians"}
    - slot{"action_return": true}
    - utter_ask_moralstatus
* inform{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholdergroup{"stakeholder": "plenty of people"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": false}
    - utter_ask_quantity
* dontknow
    - utter_ask_guess_quantity
* quantity{"quantity": "10000"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_ask_name_plural
* name{"stakeholder": "the city people"}
    - action_update_stakeholder
    - slot{"name": "the city people"}
    - slot{"action_return": true}
    - utter_ask_moralstatus
* inform{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* decider{"stakeholder": "one commander", "moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": true}
    - utter_ask_name_singular
* name
    - action_update_stakeholder
    - slot{"decider": "Kim"}
    - slot{"name": "Kim"}
    - slot{"action_return": true}
    - utter_ask_identified_moralstatus
* correct
    - utter_next_stakeholder
* deny
    - utter_confirm_stakeholders
    - utter_confirm_decider
    - utter_ask_options
* option
    - action_create_option
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_ask_deontic_modality
* inform{"deonticmodality": "prohibition"}
    - action_update_option
    - slot{"action_return": true}
    - utter_ask_universalizable
* wrong
    - action_update_option
    - slot{"action_return": true}
    - utter_ask_no_rule_reason
* inform{"reason": "needs_conditions"}
    - action_update_option
    - slot{"action_return": true}
    - utter_ask_consequences
* consequence{"stakeholder": "the city people", "sentiment": "neu"}
    - slot{"sentiment": "neu"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact
* positive
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_impact_weight
* quantity{"quantity": "8.5"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* wrong
    - utter_ask_consequence_probability
* quantity{"quantity": "80.4"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* consequence{"name": "the Bavarians", "sentiment": "neg"}
    - slot{"name": "the Bavarians"}
    - slot{"sentiment": "neg"}
    - action_create_consequence
    - slot{"name": "the Bavarians"}
    - slot{"action_return": true}
    - utter_ask_impact_negative
* correct
    - utter_ask_impact_weight
* quantity{"quantity": "5,6"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* correct
    - utter_next_consequence
* deny
    - utter_next_option
* option{"deed": "refuse to shoot the"}
    - slot{"deed": "refuse to shoot the"}
    - action_create_option
    - slot{"deed": "refuse to shoot the"}
    - slot{"action_return": true}
    - utter_ask_identified_deed
* affirm
    - action_create_deed
    - slot{"action_return": true}
    - utter_ask_deontic_modality
* inform{"deonticmodality": "option"}
    - action_update_deed
    - slot{"action_return": true}
    - utter_ask_universalizable
* correct
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_ask_consequences
* consequence{"name": "the Bavarians", "sentiment": "neg"}
    - slot{"name": "the Bavarians"}
    - slot{"sentiment": "neg"}
    - action_create_consequence
    - slot{"name": "them"}
    - slot{"action_return": true}
    - utter_ask_impact_negative
* correct
    - utter_ask_impact_weight
* quantity{"quantity": "9,99"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* correct
    - utter_next_consequence
* deny
    - utter_next_option
* deny
    - utter_got_everything
    - utter_ask_method
* utilitarism
    - utter_starting_evaluation_1
    - utter_starting_evaluation_2
    - action_evaluation_utilitarism
    - slot{"action_return": true}
    - utter_next_method
* affirm
    - utter_ask_method
* deontology
    - utter_starting_evaluation_1
    - utter_starting_evaluation_2
    - action_evaluation_deontology
    - slot{"action_return": false}
    - utter_next_method
* affirm
    - utter_ask_method
* deontology
    - utter_starting_evaluation_1
    - utter_starting_evaluation_2
    - action_evaluation_deontology
    - slot{"action_return": true}
    - utter_next_method

