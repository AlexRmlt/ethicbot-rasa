## stakeholdergroup | quantity 1
* greeting
    - action_intro
* quantity
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - utter_ask_quantity
* quantity{"quantity": "24"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_ask_name_plural

## stakeholdergroup | quantity 2
* greeting
    - action_intro
* quantity{"quantity": "ten"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - utter_ask_name_plural

## stakeholdergroup | quantity 3
* stakeholder{"name": "Molly"}
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
* inform{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* quantity{"quantity": "three"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - utter_ask_name_plural

## stakeholdergroup | quantity 4
* stakeholder{"name": "Molly"}
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
* inform{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* quantity
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - utter_ask_quantity

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
* inform{"moralstatus": "human"}
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
* inform{"moralstatus": "human"}
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
* inform{"moralstatus": "human"}
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
* inform{"moralstatus": "human"}
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
* inform{"moralstatus": "human"}
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
    - utter_ask_deontic_modality

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
    - utter_ask_deontic_modality

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
    - utter_ask_deontic_modality

## option | consequence 1
* deny
    - utter_next_option
* consequence{"name": "Thomas", "sentiment": "neg"}
    - slot{"sentiment": "neg"}
    - slot{"name": "Thomas"}
    - action_create_option
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_ask_deontic_modality
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
    - utter_ask_deontic_modality
* wrong
    - action_update_option
    - slot{"action_return": true}
    - utter_ask_no_rule_reason

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
    - utter_ask_deontic_modality

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
    - utter_ask_deontic_modality

## option | name 1
* deny
    - utter_next_option
* name{"name": "Thomas"}
    - slot{"name": "Thomas"}
    - action_create_option
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_ask_deontic_modality

## option | name 2
* deny
    - utter_next_option
* name
    - action_create_option
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_ask_deontic_modality

## option | name 3
* decider{"name": "Thomas"}
    - slot{"name": "Thomas"}
    - action_update_stakeholder
    - slot{"decider": "Thomas"}
    - slot{"action_return": true}
    - utter_ask_options
* name{"name": "Thomas"}
    - slot{"name": "Thomas"}
    - action_create_option
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_ask_deontic_modality

## option | name 4
* decider{"name": "Thomas"}
    - slot{"name": "Thomas"}
    - action_update_stakeholder
    - slot{"decider": "Thomas"}
    - slot{"action_return": true}
    - utter_ask_options
* name
    - action_create_option
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_ask_deontic_modality

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

## option | decider 1
* deny
    - utter_next_option
* decider
    - action_create_option
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_ask_deontic_modality

## option | decider 2
* deny
    - utter_next_option
* decider{"name": "mia"}
    - slot{"name": "mia"}
    - action_create_option
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_ask_deontic_modality

## option | decider 3
* decider{"name": "Thomas"}
    - slot{"name": "Thomas"}
    - action_update_stakeholder
    - slot{"decider": "Thomas"}
    - slot{"action_return": true}
    - utter_ask_options
* decider{"name": "Thomas"}
    - slot{"name": "Thomas"}
    - action_create_option
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_ask_deontic_modality

## option | decider 4
* decider{"name": "Thomas"}
    - slot{"name": "Thomas"}
    - action_update_stakeholder
    - slot{"decider": "Thomas"}
    - slot{"action_return": true}
    - utter_ask_options
* decider
    - action_create_option
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_ask_deontic_modality

## option | decider 5
* decider{"name": "Thomas"}
    - slot{"name": "Thomas"}
    - action_update_stakeholder
    - slot{"decider": "Thomas"}
    - slot{"action_return": true}
    - utter_ask_options
* decider{"deed": "save mia"}
    - slot{"deed": "save mia"}
    - action_create_option
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_ask_deontic_modality

## option | decider 6
* decider
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 4}
    - slot{"action_return": true}
    - utter_ask_name_singular
* name{"name": "mia"}
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
* decider
    - action_create_option
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_ask_deontic_modality

## consequence | decider 1
* wrong
    - utter_ask_consequence_probability
* quantity{"quantity": "5"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* decider{"name": "Andrea"}
    - slot{"name": "Andrea"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact

## consequence | decider 2
* wrong
    - utter_ask_consequence_probability
* quantity{"quantity": "5"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* decider{"deed": "kill"}
    - slot{"deed": "kill"}
    - action_create_consequence
    - slot{"action_return": false}
    - action_choose_affected_stakeholder

## consequence | decider 3
* correct
    - action_update_option
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_ask_consequences
* decider{"name": "Andrea"}
    - slot{"name": "Andrea"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact

## consequence | decider 4
* correct
    - action_update_option
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_ask_consequences
* decider{"name": "Andrea", "deed": "killing"}
    - slot{"name": "Andrea"}
    - slot{"deed": "killing"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact

## consequence | decider 5
* wrong
    - utter_ask_consequence_probability
* quantity{"quantity": "5"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* decider
    - action_create_consequence
    - slot{"action_return": false}
    - action_choose_affected_stakeholder

## consequence | negative 1
* wrong
    - utter_ask_consequence_probability
* quantity{"quantity": "5"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* negative{"name": "Kilian"}
    - slot{"name": "Kilian"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_negative

## consequence | negative 2
* wrong
    - utter_ask_consequence_probability
* quantity{"quantity": "5"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* negative
    - action_create_consequence
    - slot{"action_return": false}
    - action_choose_affected_stakeholder
* consequence{"name": "Kilian"}
    - slot{"name": "Kilian"}
    - action_create_consequence
    - slot{"name": "Kilian"}
    - slot{"action_return": true}
    - utter_ask_impact_negative

## consequence | negative 3
* correct
    - action_update_option
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_ask_consequences
* negative{"name": "Kilian"}
    - slot{"name": "Kilian"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_negative

## consequence | negative 4
* correct
    - action_update_option
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_ask_consequences
* negative
    - action_create_consequence
    - slot{"action_return": false}
    - action_choose_affected_stakeholder
* consequence{"name": "Kilian"}
    - slot{"name": "Kilian"}
    - action_create_consequence
    - slot{"name": "Kilian"}
    - slot{"action_return": true}
    - utter_ask_impact_negative

## consequence | positive 1
* wrong
    - utter_ask_consequence_probability
* quantity{"quantity": "5"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* positive{"name": "Kilian"}
    - slot{"name": "Kilian"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_positive

## consequence | positive 2
* wrong
    - utter_ask_consequence_probability
* quantity{"quantity": "5"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* positive
    - action_create_consequence
    - slot{"action_return": false}
    - action_choose_affected_stakeholder
* consequence{"name": "Kilian"}
    - slot{"name": "Kilian"}
    - action_create_consequence
    - slot{"name": "Kilian"}
    - slot{"action_return": true}
    - utter_ask_impact_positive

## consequence | positive 3
* correct
    - action_update_option
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_ask_consequences
* positive{"name": "Kilian"}
    - slot{"name": "Kilian"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_positive

## consequence | positive 4
* correct
    - action_update_option
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_ask_consequences
* positive
    - action_create_consequence
    - slot{"action_return": false}
    - action_choose_affected_stakeholder
* consequence{"name": "Kilian"}
    - slot{"name": "Kilian"}
    - action_create_consequence
    - slot{"name": "Kilian"}
    - slot{"action_return": true}
    - utter_ask_impact_positive