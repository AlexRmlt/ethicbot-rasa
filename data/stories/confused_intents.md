## name | stakeholdergroup 1
* stakeholdergroup
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": true}
    - utter_ask_quantity
* quantity{"quantity": "24"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_ask_name_plural
* stakeholdergroup
    - action_update_stakeholder
    - slot{"name": "the Palatines"}
    - slot{"action_return": true}
    - utter_ask_moralstatus

## name | stakeholdergroup 2
* stakeholdergroup{"stakeholder": "The members of the club's board"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": true}
    - utter_ask_quantity
* quantity{"quantity": "ten"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_ask_name_plural
* stakeholdergroup{"stakeholder": "the board"}
    - action_update_stakeholder
    - slot{"name": "the board"}
    - slot{"action_return": true}
    - utter_ask_moralstatus

## name | stakeholdergroup 3
* stakeholdergroup{"stakeholder": "The members of the club's board"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": true}
    - utter_ask_quantity
* quantity{"quantity": "ten"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_ask_name_plural
* stakeholdergroup
    - action_update_stakeholder
    - slot{"name": "the board"}
    - slot{"action_return": true}
    - utter_ask_moralstatus

## name | stakeholdergroup 4
* stakeholdergroup
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": true}
    - utter_ask_quantity
* quantity{"quantity": "ten"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_ask_name_plural
* stakeholdergroup{"stakeholder": "the board"}
    - action_update_stakeholder
    - slot{"name": "the board"}
    - slot{"action_return": true}
    - utter_ask_moralstatus

## name | stakeholder 1
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
    - utter_ask_moralstatus

## stakeholder | name 1
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
    - utter_ask_moralstatus
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

## stakeholder | name 2
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* name{"name": "Mary"}
    - slot{"name": "Mary"}
    - slot{"moralstatus": null}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": true}
    - action_check_identified_name
    - slot{"action_return": false}
    - utter_ask_identified_name

## stakeholder | name 3
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
    - utter_ask_identified_moralstatus
* correct
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

## stakeholder | consequence 1
* greeting
    - action_intro
* consequence{"sentiment": "neu"}
    - slot{"sentiment": "neu"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - utter_ask_name_singular

## stakeholder | consequence 2
* greeting
    - action_intro
* consequence{"sentiment": "neu"}
    - slot{"sentiment": "neu"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": false}
    - utter_ask_name_plural

## stakeholder | consequence 3
* stakeholder{"name": "Ken"}
    - slot{"name": "Ken"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - action_check_identified_name
    - slot{"action_return": false}
    - utter_ask_identified_name
* correct
    - action_update_stakeholder
    - slot{"name": "Ken"}
    - slot{"action_return": true}
    - utter_ask_moralstatus
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* consequence{"sentiment": "neu"}
    - slot{"sentiment": "neu"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": false}
    - utter_ask_name_plural
* name

## stakeholder | consequence 4
* stakeholder{"name": "Ken"}
    - slot{"name": "Ken"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - action_check_identified_name
    - slot{"action_return": false}
    - utter_ask_identified_name
* correct
    - action_update_stakeholder
    - slot{"name": "Ken"}
    - slot{"action_return": true}
    - utter_ask_moralstatus
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* consequence{"sentiment": "neu"}
    - slot{"sentiment": "neu"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - utter_ask_name_singular
* name

## stakeholder | option 1
* stakeholder{"name": "Ken"}
    - slot{"name": "Ken"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - action_check_identified_name
    - slot{"action_return": false}
    - utter_ask_identified_name
* correct
    - action_update_stakeholder
    - slot{"name": "Ken"}
    - slot{"action_return": true}
    - utter_ask_moralstatus
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* option{"stakeholder": "the owner"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - utter_ask_name_singular
* name

## stakeholder | option 2
* greeting
    - action_intro
* option{"stakeholder": "the owner"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - utter_ask_name_singular
* name

## option | stakeholder 1
* decider{"name": "Thomas"}
    - slot{"name": "Thomas"}
    - action_update_stakeholder
    - slot{"decider": "Thomas"}
    - slot{"action_return": true}
    - utter_ask_options
* stakeholder{"name": "cleopatra", "deed": "kill"}
    - slot{"deed": "kill"}
    - slot{"name": "cleopatra"}
    - action_create_option
    - slot{"deed": "kill"}
    - slot{"action_return": true}
    - utter_ask_identified_deed

## option | stakeholder 2
* decider{"name": "Thomas"}
    - slot{"name": "Thomas"}
    - action_update_stakeholder
    - slot{"decider": "Thomas"}
    - slot{"action_return": true}
    - utter_ask_options
* stakeholder{"name": "cleopatra"}
    - slot{"name": "cleopatra"}
    - action_create_option
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_ask_option_universalizable

## option | stakeholder 3
* decider{"name": "Thomas"}
    - slot{"name": "Thomas"}
    - action_update_stakeholder
    - slot{"decider": "Thomas"}
    - slot{"action_return": true}
    - utter_ask_options
* stakeholder
    - action_create_option
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_ask_option_universalizable

## option | stakeholder 4
* deny
    - utter_next_option
* stakeholder{"name": "Thomas", "deed": "refuse to kill the dog"}
    - slot{"deed": "refuse to kill the dog"}
    - slot{"name": "Thomas"}
    - action_create_option
    - slot{"deed": "refuse to kill the dog"}
    - slot{"action_return": true}
    - utter_ask_identified_deed

## option | stakeholder 5
* deny
    - utter_next_option
* stakeholder{"name": "Thomas"}
    - slot{"name": "Thomas"}
    - action_create_option
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_ask_option_universalizable

## option | consequence 1
* deny
    - utter_next_option
* consequence{"name": "Thomas", "sentiment": "neg"}
    - slot{"sentiment": "neg"}
    - slot{"name": "Thomas"}
    - action_create_option
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_ask_option_universalizable
* correct
    - action_update_option
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_ask_consequences

## option | consequence 2
* deny
    - utter_next_option
* consequence{"sentiment": "pos"}
    - slot{"sentiment": "pos"}
    - action_create_option
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_ask_option_universalizable
* wrong
    - action_update_option
    - slot{"action_return": true}
    - utter_ask_inherent_evil

## option | consequence 3
* decider{"name": "thomas"}
    - slot{"name": "thomas"}
    - action_update_stakeholder
    - slot{"decider": "thomas"}
    - slot{"action_return": true}
    - utter_ask_options
* consequence{"sentiment": "pos"}
    - slot{"sentiment": "pos"}
    - action_create_option
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_ask_option_universalizable

## option | consequence 4
* decider{"name": "thomas"}
    - slot{"name": "thomas"}
    - action_update_stakeholder
    - slot{"decider": "thomas"}
    - slot{"action_return": true}
    - utter_ask_options
* consequence{"name": "alex", "sentiment": "pos"}
    - slot{"sentiment": "pos"}
    - slot{"name": "alex"}
    - action_create_option
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_ask_option_universalizable

## consequence | stakeholder 1
* correct
    - action_update_option
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_ask_consequences
* stakeholder{"name": "Andrea"}
    - slot{"name": "Andrea"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact

## consequence | stakeholder 2
* correct
    - action_update_option
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_ask_consequences
* stakeholder
    - action_create_consequence
    - slot{"name": null}
    - slot{"action_return": false}
    - action_choose_affected_stakeholder

## consequence | stakeholder 3
* correct
    - action_update_option
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_ask_consequences
* stakeholder{"stakeholder": "the victim"}
    - action_create_consequence
    - slot{"name": null}
    - slot{"action_return": false}
    - action_choose_affected_stakeholder

## consequence | stakeholder 4
* wrong
    - utter_ask_consequence_probability
* quantity{"quantity": "5"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* stakeholder{"stakeholder": "the victim"}
    - action_create_consequence
    - slot{"name": null}
    - slot{"action_return": false}
    - action_choose_affected_stakeholder

## consequence | stakeholder 5
* wrong
    - utter_ask_consequence_probability
* quantity{"quantity": "5"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* stakeholder{"name": "Andrea"}
    - slot{"name": "Andrea"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact

## consequence | option 1
* wrong
    - utter_ask_consequence_probability
* quantity{"quantity": "5"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* option{"name": "Andrea"}
    - slot{"name": "Andrea"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact


## consequence | option 2
* wrong
    - utter_ask_consequence_probability
* quantity{"quantity": "5"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* option{"deed": "kill"}
    - slot{"deed": "kill"}
    - action_create_consequence
    - slot{"action_return": false}
    - action_choose_affected_stakeholder

## consequence | option 3
* correct
    - action_update_option
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_ask_consequences
* option{"name": "Andrea"}
    - slot{"name": "Andrea"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact

## consequence | option 4
* correct
    - action_update_option
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_ask_consequences
* option{"name": "Andrea", "deed": "killing"}
    - slot{"name": "Andrea"}
    - slot{"deed": "killing"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact
