## Handle possible confusion of intents stakeholder and name 1
* stakeholder
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 4}
    - slot{"action_return": true}
    - utter_ask_name_singular
* stakeholder
    - action_update_stakeholder
    - slot{"name": "Katharina"}
    - slot{"action_return": true}
    - utter_ask_moral_status

## Handle possible confusion of intents stakeholder and name 2
* greeting
    - action_intro
* name{"name": "Molly"}
    - slot{"name": "Molly"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - action_check_identified_name
    - slot{"action_return": false}
    - utter_ask_identified_name
* correct
    - action_update_stakeholder
    - slot{"name": "Molly"}
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* name{"name": "Andrea"}
    - slot{"name": "Andrea"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - action_check_identified_name
    - slot{"action_return": false}
    - utter_ask_identified_name

## Handle possible confusion of intents stakeholder and name 3
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* name{"name": "Mary"}
    - slot{"name": "Mary"}
    - slot{"moralstatus": "human"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": true}
    - action_check_identified_name
    - slot{"action_return": false}
    - utter_ask_identified_name

## Handle possible confusion of intents stakeholder and name 4
* stakeholder{"name": "Mary", "moralstatus": "human"}
    - slot{"name": "Mary"}
    - slot{"moralstatus": "human"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": true}
    - action_check_identified_name
    - slot{"action_return": false}
    - utter_ask_identified_name
* wrong
    - action_update_stakeholder
    - slot{"name": "Samuel"}
    - slot{"action_return": true}
    - utter_next_stakeholder
* name{"name": "Samuel"}
    - slot{"name": "Samuel"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": true}
    - action_check_identified_name
    - slot{"action_return": false}
    - utter_ask_identified_name


## Handle possible confusion of intents deed and option
* decider{"name": "Inga"}
    - slot{"name": "Inga"}
    - action_update_stakeholder
    - slot{"decider": "Inga"}
    - slot{"action_return": true}
    - utter_ask_options
* deed
    - action_create_option
    - slot{"deed": null}
    - slot{"option": 4}
    - slot{"action_return": true}
    - utter_ask_deed
* option{"deed": "rescuing"}
    - slot{"deed": "rescuing"}
    - action_create_deed
    - slot{"action_return": true}
    - utter_ask_universalizable

## Handle possible confusion of intents deed and consequence
* decider{"name": "Inga"}
    - slot{"name": "Inga"}
    - action_update_stakeholder
    - slot{"decider": "Inga"}
    - slot{"action_return": true}
    - utter_ask_options
* deed
    - action_create_option
    - slot{"deed": null}
    - slot{"option": 4}
    - slot{"action_return": true}
    - utter_ask_deed
* consequence{"deed": "rescuing"}
    - slot{"deed": "rescuing"}
    - action_create_deed
    - slot{"action_return": true}
    - utter_ask_universalizable