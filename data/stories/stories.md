## Generated Story 8921249185666987085
* greeting
    - action_intro
* stakeholder{"stakeholder": "me", "moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - utter_ask_name_singular
* name{"name": "graziella"}
    - slot{"name": "graziella"}
    - action_update_stakeholder
    - slot{"name": "graziella"}
    - slot{"action_return": true}
    - utter_ask_identified_moralstatus
* correct
    - utter_next_stakeholder
* stakeholder{"stakeholder": "unknown person", "moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": true}
    - utter_ask_name_singular
* deny{"stakeholder": "the person"}
    - action_update_stakeholder
    - slot{"name": "Sascha"}
    - slot{"action_return": true}
    - utter_ask_identified_moralstatus
* correct
    - utter_next_stakeholder
* stakeholder{"stakeholder": "me", "moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": true}
    - utter_ask_name_singular
* name{"stakeholder": "mum"}
    - action_update_stakeholder
    - slot{"name": "mum"}
    - slot{"action_return": true}
    - utter_ask_identified_moralstatus
* correct
    - utter_next_stakeholder
* deny
    - utter_confirm_stakeholders
    - action_choose_decider
* decider{"name": "graziella"}
    - slot{"name": "graziella"}
    - action_update_stakeholder
    - slot{"decider": "graziella"}
    - slot{"action_return": true}
    - utter_ask_options
* deny
    - utter_got_everything
    - utter_ask_method

## Generated Story 3496960145483561691
* greeting
    - action_intro
* stakeholder{"name": "erskine"}
    - slot{"name": "erskine"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - action_check_identified_name
    - slot{"action_return": false}
    - utter_ask_identified_name
* correct
    - action_update_stakeholder
    - slot{"name": "erskine"}
    - slot{"action_return": true}
    - utter_ask_moralstatus
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* name{"name": "Chris"}
    - slot{"name": "Chris"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": true}
    - action_check_identified_name
    - slot{"action_return": false}
    - utter_ask_identified_name
* correct
    - action_update_stakeholder
    - slot{"name": "Chris"}
    - slot{"action_return": true}
    - utter_ask_moralstatus
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* name{"name": "Solomon"}
    - slot{"name": "Solomon"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": true}
    - action_check_identified_name
    - slot{"action_return": false}
    - utter_ask_identified_name
* correct
    - action_update_stakeholder
    - slot{"name": "Solomon"}
    - slot{"action_return": true}
    - utter_ask_moralstatus
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* name
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 4}
    - slot{"action_return": true}
    - utter_ask_name_singular
* name{"name": "Kim"}
    - slot{"name": "Kim"}
    - action_update_stakeholder
    - slot{"name": "Kim"}
    - slot{"action_return": true}
    - utter_next_stakeholder
* name{"name": "Dan"}
    - slot{"name": "Dan"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 5}
    - slot{"action_return": true}
    - action_check_identified_name
    - slot{"action_return": false}
    - utter_ask_identified_name
* correct
    - action_update_stakeholder
    - slot{"name": "Dan"}
    - slot{"action_return": true}
    - utter_ask_moralstatus
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* deny
    - utter_confirm_stakeholders
    - action_choose_decider
* decider{"name": "erskine"}
    - slot{"name": "erskine"}
    - action_update_stakeholder
    - slot{"decider": "erskine"}
    - slot{"action_return": true}
    - utter_ask_options
* option{"name": "erskine", "deed": "hand over information"}
    - slot{"deed": "hand over information"}
    - slot{"name": "erskine"}
    - action_create_option
    - slot{"deed": "hand over information"}
    - slot{"action_return": true}
    - utter_ask_identified_deed
* correct
    - action_create_deed
    - slot{"action_return": true}
    - utter_ask_deed_universalizable
* wrong
    - action_update_deed
    - slot{"action_return": true}
    - utter_ask_inherent_evil
* deny{"name": "too_specific"}
    - slot{"name": "too_specific"}
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_ask_consequences
* consequence{"name": "erskine", "sentiment": "neu"}
    - slot{"name": "erskine"}
    - slot{"sentiment": "neu"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact
* negative
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_impact_weight
* consequence{"name": "erskine"}
    - slot{"name": "erskine"}
    - utter_ask_impact_weight
* quantity{"quantity": "8"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* correct
    - utter_next_consequence
* decider{"name": "erskine"}
    - slot{"name": "erskine"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact
* positive
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_impact_weight
* quantity{"quantity": "6"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* correct
    - utter_next_consequence
* decider{"name": "erskine"}
    - slot{"name": "erskine"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact
* negative
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_impact_weight
* quantity{"quantity": "6"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* correct
    - utter_next_consequence
* deny
    - utter_next_option

