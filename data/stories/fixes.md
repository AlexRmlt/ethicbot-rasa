## Avoid loop after adding decider 1
* decider
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 4}
    - slot{"action_return": true}
    - utter_ask_name_singular
* dontknow
    - action_update_stakeholder
    - slot{"decider": "Roswitha"}
    - slot{"name": "Roswitha"}
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_ask_options

## Avoid loop after adding decider 2
* decider
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 4}
    - slot{"action_return": true}
    - utter_ask_name_singular
* name
    - action_update_stakeholder
    - slot{"decider": "Roswitha"}
    - slot{"name": "Roswitha"}
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_ask_options

## Avoid loop after adding decider 3
* decider
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 4}
    - slot{"action_return": true}
    - utter_ask_name_singular
* deny
    - action_update_stakeholder
    - slot{"decider": "Roswitha"}
    - slot{"name": "Roswitha"}
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_ask_options

## Do not output image when action failed 1
* deny
    - utter_got_everything
    - utter_ask_method
* utilitarism
    - utter_starting_evaluation_1
    - utter_starting_evaluation_2
    - action_evaluation_utilitarism
    - slot{"action_return": false}
    - utter_next_method
* affirm
    - utter_ask_method
* deontology
    - utter_starting_evaluation_1
    - utter_starting_evaluation_2
    - action_evaluation_deontology
    - slot{"action_return": false}
    - utter_next_method
* deny
    - utter_goodbye

## Do not output image when action failed 2
* deny
    - utter_got_everything
    - utter_ask_method
* deontology
    - utter_starting_evaluation_1
    - utter_starting_evaluation_2
    - action_evaluation_deontology
    - slot{"action_return": false}
    - utter_next_method
* utilitarism
    - utter_starting_evaluation_1
    - utter_starting_evaluation_2
    - action_evaluation_utilitarism
    - slot{"action_return": false}
    - utter_next_method
* affirm
    - utter_ask_method
* deny
    - utter_goodbye

## Do not output image when action failed 3
* deny
    - utter_got_everything
    - utter_ask_method
* deontology
    - utter_starting_evaluation_1
    - utter_starting_evaluation_2
    - action_evaluation_deontology
    - slot{"action_return": false}
    - utter_next_method
* deny
    - utter_goodbye

## Do not output image when action failed 4
* deny
    - utter_got_everything
    - utter_ask_method
* utilitarism
    - utter_starting_evaluation_1
    - utter_starting_evaluation_2
    - action_evaluation_utilitarism
    - slot{"action_return": false}
    - utter_next_method
* deny
    - utter_goodbye

## Call update_stakeholder if quantity is finally denied 1
* stakeholdergroup
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": false}
    - utter_ask_quantity
* dontknow
    - utter_ask_guess_quantity
* dontknow
    - action_update_stakeholder
    - slot{"action_return": false}
    - utter_ask_name_plural


## Call update_stakeholder if quantity is finally denied 2
* stakeholdergroup
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": false}
    - utter_ask_quantity
* dontknow
    - utter_ask_guess_quantity
* deny
    - action_update_stakeholder
    - slot{"action_return": false}
    - utter_ask_name_plural

## Call update_stakeholder if quantity is finally denied 3
* stakeholdergroup
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": false}
    - utter_ask_quantity
* deny
    - utter_ask_guess_quantity
* deny
    - action_update_stakeholder
    - slot{"action_return": false}
    - utter_ask_name_plural

## Call update_stakeholder if quantity is finally denied 4
* stakeholdergroup
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": false}
    - utter_ask_quantity
* deny
    - utter_ask_guess_quantity
* dontknow
    - action_update_stakeholder
    - slot{"action_return": false}
    - utter_ask_name_plural

## User answers affirm instead of telling the next stakeholder 1
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* affirm

## User answers affirm instead of telling the next stakeholder 2
* deny
    - action_update_stakeholder
    - slot{"name": "the Palatines"}
    - slot{"action_return": true}
    - utter_next_stakeholder
* affirm
    - utter_next_stakeholder

## User answers affirm instead of telling the next stakeholder 3
* correct
    - action_update_stakeholder
    - slot{"name": "Molly"}
    - slot{"action_return": true}
    - utter_next_stakeholder
* affirm
    - utter_next_stakeholder

## User answers affirm instead of telling the next stakeholder 4
* wrong
    - action_update_stakeholder
    - slot{"name": "Inga"}
    - slot{"action_return": true}
    - utter_next_stakeholder
* affirm
    - utter_next_stakeholder

## User answers affirm instead of telling the next stakeholder 5
* name
    - action_update_stakeholder
    - slot{"name": "Inga"}
    - slot{"action_return": true}
    - utter_next_stakeholder
* affirm
    - utter_next_stakeholder

## Name is falsly recognized as stakeholder
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