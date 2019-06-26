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
    - utter_ask_moralstatus
* inform{"moralstatus": "human"}
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
    - utter_ask_moralstatus
* inform{"moralstatus": "human"}
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
    - utter_ask_moralstatus
* inform{"moralstatus": "human"}
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
* inform{"moralstatus": "human"}
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

## Don't ask identified name if it was found to be already assigned
* stakeholder{"name": "jane"}
    - slot{"name": "jane"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": true}
    - action_check_identified_name
    - slot{"action_return": true}
    - utter_ask_name_singular

## Don't ask identified name if there was no name found
* stakeholder{"stakeholder": "the shopkeeper"}
    - slot{"name": "jane"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": true}
    - utter_ask_name_singular

## Handle greeting as first message 1
* greeting
    - action_intro
* greeting
    - utter_greet
    - utter_ask_stakeholders
* stakeholder{"name": "Andrea"}
    - action_create_stakeholder

## Handle greeting as first message 2
* greeting
    - action_intro
* greeting
    - utter_greet
    - utter_ask_stakeholders

## Choose evaluation principles twice or more times 1
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
    - slot{"action_return": true}
    - utter_next_method
* utilitarism
    - utter_starting_evaluation_1
    - utter_starting_evaluation_2
    - action_evaluation_utilitarism
    - slot{"action_return": true}
    - utter_next_method

## Choose evaluation principles twice or more times 2
* deny
    - utter_next_option
* deny
    - utter_got_everything
    - utter_ask_method
* deontology
    - utter_starting_evaluation_1
    - utter_starting_evaluation_2
    - action_evaluation_deontology
    - slot{"action_return": true}
    - utter_next_method
* affirm
    - utter_ask_method
* utilitarism
    - utter_starting_evaluation_1
    - utter_starting_evaluation_2
    - action_evaluation_utilitarism
    - slot{"action_return": true}
    - utter_next_method
* deontology
    - utter_starting_evaluation_1
    - utter_starting_evaluation_2
    - action_evaluation_deontology
    - slot{"action_return": true}
    - utter_next_method

## Choose evaluation principles twice or more times 3
* deny
    - utter_next_option
* deny
    - utter_got_everything
    - utter_ask_method
* deontology
    - utter_starting_evaluation_1
    - utter_starting_evaluation_2
    - action_evaluation_deontology
    - slot{"action_return": true}
    - utter_next_method
* affirm
    - utter_ask_method
* deontology
    - utter_starting_evaluation_1
    - utter_starting_evaluation_2
    - action_evaluation_deontology
    - slot{"action_return": true}
    - utter_next_method
* utilitarism
    - utter_starting_evaluation_1
    - utter_starting_evaluation_2
    - action_evaluation_utilitarism
    - slot{"action_return": true}
    - utter_next_method

## Choose evaluation principles twice or more times 4
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
    - slot{"action_return": true}
    - utter_next_method
* deontology
    - utter_starting_evaluation_1
    - utter_starting_evaluation_2
    - action_evaluation_deontology
    - slot{"action_return": true}
    - utter_next_method

## Create decider when user says it is someone else 1
* greeting
    - action_intro
* stakeholder{"stakeholder": "some person"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - utter_ask_name_singular
* dontknow
    - action_update_stakeholder
    - slot{"name": "Robin"}
    - slot{"action_return": true}
    - utter_ask_moralstatus
* inform{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholdergroup{"stakeholder": "a crowd of people"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": false}
    - utter_ask_quantity
* quantity{"quantity": "1000"}
    - action_update_stakeholder
    - followup{"name": "utter_ask_name_plural"}
    - slot{"action_return": true}
    - utter_ask_name_plural
* deny
    - action_update_stakeholder
    - slot{"name": "the Saxons"}
    - slot{"action_return": true}
    - utter_ask_moralstatus
* inform{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* deny
    - utter_confirm_stakeholders
    - action_choose_decider
* decider
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": true}
    - utter_ask_name_singular
* name{"name": "Akin"}
    - slot{"name": "Akin"}
    - action_update_stakeholder
    - slot{"decider": "Akin"}
    - slot{"name": "Akin"}
    - slot{"action_return": true}
    - utter_ask_moralstatus
* inform{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_ask_options

## Create decider when user says it is someone else 2
* deny
    - utter_confirm_stakeholders
    - action_choose_decider
* decider
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": true}
    - utter_ask_name_singular

## Create non-human decider with moral status weight 1
* greeting
    - action_intro
* stakeholder{"stakeholder": "my neighbor"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - utter_ask_name_singular
* name
    - action_update_stakeholder
    - slot{"name": "Yves"}
    - slot{"action_return": true}
    - utter_ask_moralstatus
* inform{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* name
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": true}
    - utter_ask_name_singular
* name
    - action_update_stakeholder
    - slot{"name": "Charlie"}
    - slot{"action_return": true}
    - utter_ask_moralstatus
* inform{"moralstats": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* name
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": true}
    - utter_ask_name_singular
* name
    - action_update_stakeholder
    - slot{"name": "Xiao"}
    - slot{"action_return": true}
    - utter_ask_moralstatus
* inform{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* deny
    - utter_confirm_stakeholders
    - action_choose_decider
* decider
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 4}
    - slot{"action_return": true}
    - utter_ask_name_singular
* stakeholder
    - action_update_stakeholder
    - slot{"decider": "Kim"}
    - slot{"name": "Kim"}
    - slot{"action_return": true}
    - utter_ask_moralstatus
* inform{"moralstatus": "other"}
    - slot{"moralstatus": "other"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_ask_moralstatus_weight
* quantity{"quantity": "5"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_ask_options

## Create non-human decider with moral status weight 2
* inform{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* deny
    - utter_confirm_stakeholders
    - action_choose_decider
* decider
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 4}
    - slot{"action_return": true}
    - utter_ask_name_singular
* name
    - action_update_stakeholder
    - slot{"decider": "Kim"}
    - slot{"name": "Kim"}
    - slot{"action_return": true}
    - utter_ask_moralstatus
* inform{"moralstatus": "animal"}
    - slot{"moralstatus": "animal"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_ask_moralstatus_weight
* quantity{"quantity": "5"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_ask_options

## Create non-human decider with moral status weight 3
* inform{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* deny
    - utter_confirm_stakeholders
    - action_choose_decider
* decider
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 4}
    - slot{"action_return": true}
    - utter_ask_name_singular
* name
    - action_update_stakeholder
    - slot{"decider": "Kim"}
    - slot{"name": "Kim"}
    - slot{"action_return": true}
    - utter_ask_moralstatus
* inform{"moralstatus": "other"}
    - slot{"moralstatus": "other"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_ask_moralstatus_weight
* quantity{"quantity": "5"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_ask_options

## Create non-human decider with moral status weight 4
* inform{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* deny
    - utter_confirm_stakeholders
    - action_choose_decider
* decider
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 4}
    - slot{"action_return": true}
    - utter_ask_name_singular
* name{"name": "Hans"}
    - slot{"name": "Hans"}
    - action_update_stakeholder
    - slot{"decider": "Kim"}
    - slot{"name": "Kim"}
    - slot{"action_return": true}
    - utter_ask_moralstatus
* inform{"moralstatus": "animal"}
    - slot{"moralstatus": "animal"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_ask_moralstatus_weight
* quantity{"quantity": "5"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_ask_options

## Create non-human decider with moral status weight 5
* inform{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* deny
    - utter_confirm_stakeholders
    - action_choose_decider
* decider
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 4}
    - slot{"action_return": true}
    - utter_ask_name_singular
* name{"name": "Hans"}
    - slot{"name": "Hans"}
    - action_update_stakeholder
    - slot{"decider": "Kim"}
    - slot{"name": "Kim"}
    - slot{"action_return": true}
    - utter_ask_moralstatus
* inform{"moralstatus": "other"}
    - slot{"moralstatus": "other"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_ask_moralstatus_weight
* quantity{"quantity": "5"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_ask_options