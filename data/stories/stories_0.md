## Generated Story 550948592752613427
* greeting
    - action_intro
* stakeholder{"stakeholder": "the manager", "moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - utter_ask_name_singular
* name{"name": "michael"}
    - slot{"name": "michael"}
    - action_update_stakeholder
    - slot{"name": "michael"}
    - slot{"action_return": true}
    - utter_ask_identified_moralstatus
* correct
    - utter_next_stakeholder
* stakeholdergroup
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": true}
    - utter_ask_quantity
* quantity{"quantity": "50000"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_ask_name_plural
* name
    - action_update_stakeholder
    - slot{"name": "the Palatines"}
    - slot{"action_return": true}
    - utter_next_stakeholder
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
* name{"stakeholder": "the board"}
    - action_update_stakeholder
    - slot{"name": "the board"}
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

## Generated Story -929222555983096880
* stakeholder{"name": "thomas"}
    - slot{"name": "thomas"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - action_check_identified_name
    - slot{"action_return": false}
    - utter_ask_identified_name
* correct
    - action_update_stakeholder
    - slot{"name": "thomas"}
    - slot{"action_return": true}
    - utter_ask_moralstatus
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"name": "dirk"}
    - slot{"name": "dirk"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": true}
    - action_check_identified_name
    - slot{"action_return": false}
    - utter_ask_identified_name
* correct
    - action_update_stakeholder
    - slot{"name": "dirk"}
    - slot{"action_return": true}
    - utter_ask_moralstatus
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"stakeholder": "the victim"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": true}
    - utter_ask_name_singular
* name{"stakeholder": "victim"}
    - action_update_stakeholder
    - slot{"name": "victim"}
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
* decider{"name": "thomas"}
    - slot{"name": "thomas"}
    - action_update_stakeholder
    - slot{"decider": "thomas"}
    - slot{"action_return": true}
    - utter_ask_options
* option
    - action_create_option
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_ask_option_universalizable
* correct
    - action_update_option
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_ask_consequences
* consequence{"sentiment": "neg"}
    - slot{"sentiment": "neg"}
    - action_create_consequence
    - slot{"name": null}
    - slot{"action_return": false}
    - action_choose_affected_stakeholder
* consequence{"name": "thomas"}
    - slot{"name": "thomas"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_negative
* correct
    - action_update_consequence
    - slot{"action_return": false}
    - utter_ask_impact_weight
* quantity{"quantity": "8"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* correct
    - utter_next_consequence
* deny
    - utter_next_option
* option{"deed": "kill"}
    - slot{"deed": "kill"}
    - action_create_option
    - slot{"deed": "kill"}
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
* affirm
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_ask_consequences
* consequence{"stakeholder": "the victim", "name": "blue", "sentiment": "neg"}
    - slot{"name": "blue"}
    - slot{"sentiment": "neg"}
    - action_create_consequence
    - slot{"name": "victim"}
    - slot{"action_return": true}
    - utter_ask_impact_negative
* correct
    - utter_ask_impact_weight
* quantity{"quantity": "8"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* correct
    - utter_next_consequence
* consequence{"name": "thomas", "sentiment": "neu"}
    - slot{"name": "thomas"}
    - slot{"sentiment": "neu"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact
* negative
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_impact_weight
* quantity{"quantity": "3"}
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

## Generated Story -4255966964017846779
* stakeholder{"name": "thomas"}
    - slot{"name": "thomas"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - action_check_identified_name
    - slot{"action_return": false}
    - utter_ask_identified_name
* correct
    - action_update_stakeholder
    - slot{"name": "thomas"}
    - slot{"action_return": true}
    - utter_ask_moralstatus
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"name": "django"}
    - slot{"name": "django"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": true}
    - action_check_identified_name
    - slot{"action_return": false}
    - utter_ask_identified_name
* correct
    - action_update_stakeholder
    - slot{"name": "django"}
    - slot{"action_return": true}
    - utter_ask_moralstatus
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"stakeholder": "the victim"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": true}
    - utter_ask_name_singular
* name{"stakeholder": "victim"}
    - action_update_stakeholder
    - slot{"name": "victim"}
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
* decider{"name": "thomas"}
    - slot{"name": "thomas"}
    - action_update_stakeholder
    - slot{"decider": "thomas"}
    - slot{"action_return": true}
    - utter_ask_options
* option{"deed": "kill"}
    - slot{"deed": "kill"}
    - action_create_option
    - slot{"deed": "kill"}
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
* affirm
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_ask_consequences
* consequence{"stakeholder": "the victim", "sentiment": "neg", "name": "Will"}
    - slot{"name": "Will"}
    - slot{"sentiment": "neg"}
    - action_create_consequence
    - slot{"name": "victim"}
    - slot{"action_return": true}
    - utter_ask_impact_negative
* correct
    - utter_ask_impact_weight
* quantity{"quantity": "10"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* correct
    - utter_next_consequence
* consequence{"name": "thomas", "sentiment": "neg"}
    - slot{"name": "thomas"}
    - slot{"sentiment": "neg"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_negative
* wrong
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_impact_weight
* quantity{"quantity": "10"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* correct
    - utter_next_consequence
* consequence{"name": "thomas", "sentiment": "neg"}
    - slot{"name": "thomas"}
    - slot{"sentiment": "neg"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_negative
* correct
    - utter_ask_impact_weight
* quantity{"quantity": "10"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* wrong
    - utter_ask_consequence_probability
* quantity{"quantity": "30"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* deny
    - utter_next_option
* option{"name": "thomas", "deed": "refuse to commit the murder"}
    - slot{"deed": "refuse to commit the murder"}
    - slot{"name": "thomas"}
    - action_create_option
    - slot{"deed": "refuse to commit the murder"}
    - slot{"action_return": true}
    - utter_ask_identified_deed
* correct
    - action_create_deed
    - slot{"action_return": true}
    - utter_ask_deed_universalizable
* correct
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_ask_consequences
* consequence{"name": "thomas", "sentiment": "neg"}
    - slot{"name": "thomas"}
    - slot{"sentiment": "neg"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_negative
* correct
    - utter_ask_impact_weight
* quantity{"quantity": "10"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* wrong
    - utter_ask_consequence_probability
* quantity{"quantity": "80"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* deny
    - utter_next_option
* deny
    - utter_got_everything
    - utter_ask_method

## Generated Story 155021442888258806
* stakeholder{"name": "django", "deed": "kill"}
    - slot{"deed": "kill"}
    - slot{"name": "django"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - action_check_identified_name
    - slot{"action_return": false}
    - utter_ask_identified_name
* wrong
    - action_update_stakeholder
    - slot{"name": "Zisan"}
    - slot{"action_return": true}
    - utter_ask_moralstatus
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"name": "django", "stakeholder": "the dog owner", "moralstatus": "animal"}
    - slot{"moralstatus": "animal"}
    - slot{"name": "django"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": true}
    - action_check_identified_name
    - slot{"action_return": false}
    - utter_ask_identified_name
* correct
    - action_update_stakeholder
    - slot{"name": "django"}
    - slot{"action_return": true}
    - utter_ask_identified_moralstatus
* wrong
    - utter_ask_moralstatus
* moralstatus{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": true}
    - utter_ask_name_singular
* name{"name": "happy"}
    - slot{"name": "happy"}
    - action_update_stakeholder
    - slot{"name": "happy"}
    - slot{"action_return": true}
    - utter_ask_moralstatus
* moralstatus{"moralstatus": "animal"}
    - slot{"moralstatus": "animal"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_ask_moralstatus_weight
* quantity{"quantity": "5"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* deny
    - utter_confirm_stakeholders
    - action_choose_decider

## Generated Story 6954279179884651322
* stakeholder{"name": "peter"}
    - slot{"name": "peter"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - action_check_identified_name
    - slot{"action_return": false}
    - utter_ask_identified_name
* correct
    - action_update_stakeholder
    - slot{"name": "peter"}
    - slot{"action_return": true}
    - utter_ask_moralstatus
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"name": "christian", "stakeholder": "the dog owner", "moralstatus": "animal"}
    - slot{"moralstatus": "animal"}
    - slot{"name": "christian"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": true}
    - action_check_identified_name
    - slot{"action_return": false}
    - utter_ask_identified_name
* correct
    - action_update_stakeholder
    - slot{"name": "christian"}
    - slot{"action_return": true}
    - utter_ask_identified_moralstatus
* wrong
    - utter_ask_moralstatus
* moralstatus{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": true}
    - utter_ask_name_singular
* name{"name": "happy"}
    - slot{"name": "happy"}
    - action_update_stakeholder
    - slot{"name": "happy"}
    - slot{"action_return": true}
    - utter_ask_moralstatus
* moralstatus{"moralstatus": "animal"}
    - slot{"moralstatus": "animal"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_ask_moralstatus_weight
* quantity{"quantity": "5"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* deny
    - utter_confirm_stakeholders
    - action_choose_decider
* decider{"name": "peter"}
    - slot{"name": "peter"}
    - action_update_stakeholder
    - slot{"decider": "peter"}
    - slot{"action_return": true}
    - utter_ask_options
* option{"deed": "kill"}
    - slot{"deed": "kill"}
    - action_create_option
    - slot{"deed": "kill"}
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
* deny
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_ask_consequences
* consequence{"name": "peter", "sentiment": "neg"}
    - slot{"name": "peter"}
    - slot{"sentiment": "neg"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_negative
* correct
    - utter_ask_impact_weight
* quantity{"quantity": "3"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* correct
    - utter_next_consequence
* consequence{"name": "yves", "sentiment": "neg"}
    - slot{"name": "yves"}
    - slot{"sentiment": "neg"}
    - action_create_consequence
    - slot{"name": null}
    - slot{"action_return": false}
    - action_choose_affected_stakeholder
* consequence{"name": "happy"}
    - slot{"name": "happy"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_negative
* correct
    - utter_ask_impact_weight
* quantity{"quantity": "10"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* correct
    - utter_next_consequence
* deny
    - utter_next_option
* option{"deed": "allow yves to continue living"}
    - slot{"deed": "allow yves to continue living"}
    - action_create_option
    - slot{"deed": "allow yves to continue living"}
    - slot{"action_return": true}
    - utter_ask_identified_deed
* correct
    - action_create_deed
    - slot{"action_return": true}
    - utter_ask_deed_universalizable
* correct
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_ask_consequences
* consequence{"name": "yves", "sentiment": "neg"}
    - slot{"name": "yves"}
    - slot{"sentiment": "neg"}
    - action_create_consequence
    - slot{"name": null}
    - slot{"action_return": false}
    - action_choose_affected_stakeholder
* consequence{"name": "happy"}
    - slot{"name": "happy"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_negative
* correct
    - action_update_consequence
    - slot{"action_return": false}
    - utter_ask_impact_weight
* quantity{"quantity": "3"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* correct
    - utter_next_consequence
* consequence{"name": "christian", "sentiment": "neg"}
    - slot{"name": "christian"}
    - slot{"sentiment": "neg"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_negative
* correct
    - utter_ask_impact_weight
* quantity{"quantity": "2"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* correct
    - utter_next_consequence
* deny
    - utter_next_option
* affirm
    - utter_next_option

## Generated Story -3455233882383967956
* greeting
    - action_intro
* stakeholder{"name": "Thomas"}
    - slot{"name": "Thomas"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - action_check_identified_name
    - slot{"action_return": false}
    - utter_ask_identified_name
* correct
    - action_update_stakeholder
    - slot{"name": "Thomas"}
    - slot{"action_return": true}
    - utter_ask_moralstatus
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"name": "Dirk"}
    - slot{"name": "Dirk"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": true}
    - action_check_identified_name
    - slot{"action_return": false}
    - utter_ask_identified_name
* correct
    - action_update_stakeholder
    - slot{"name": "Dirk"}
    - slot{"action_return": true}
    - utter_ask_moralstatus
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"stakeholder": "the victim"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": true}
    - utter_ask_name_singular
* name{"stakeholder": "victim"}
    - action_update_stakeholder
    - slot{"name": "victim"}
    - slot{"action_return": true}
    - utter_ask_moralstatus
* moralstatus{"moralstatus": "machine"}
    - slot{"moralstatus": "machine"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* deny
    - utter_confirm_stakeholders
    - action_choose_decider
* decider{"name": "Thomas"}
    - slot{"name": "Thomas"}
    - action_update_stakeholder
    - slot{"decider": "Thomas"}
    - slot{"action_return": true}
    - utter_ask_options

## Generated Story 1206486904248161554
* greeting
    - action_intro
* stakeholder
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - utter_ask_name_singular
* name{"name": "alex"}
    - slot{"name": "alex"}
    - action_update_stakeholder
    - slot{"name": "alex"}
    - slot{"action_return": true}
    - utter_ask_moralstatus
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"stakeholder": "the owner"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": true}
    - utter_ask_name_singular
* name{"name": "mike"}
    - slot{"name": "mike"}
    - action_update_stakeholder
    - slot{"name": "mike"}
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
* decider{"name": "alex"}
    - slot{"name": "alex"}
    - action_update_stakeholder
    - slot{"decider": "alex"}
    - slot{"action_return": true}
    - utter_ask_options
* option{"deed": "keep the purse"}
    - slot{"deed": "keep the purse"}
    - action_create_option
    - slot{"deed": "keep the purse"}
    - slot{"action_return": true}
    - utter_ask_identified_deed
* correct
    - action_create_deed
    - slot{"action_return": true}
    - utter_ask_deed_universalizable
* correct
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_ask_consequences
* consequence{"name": "mike"}
    - slot{"name": "mike"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact
* positive
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_impact_weight
* quantity{"quantity": "8"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* correct
    - utter_next_consequence
* consequence{"name": "mike"}
    - slot{"name": "mike"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact
* positive{"name": "mike"}
    - slot{"name": "mike"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_impact_weight
* quantity{"quantity": "4"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* correct
    - utter_next_consequence
* deny
    - utter_next_option
* option{"deed": "keep the money"}
    - slot{"deed": "keep the money"}
    - action_create_option
    - slot{"deed": "keep the money"}
    - slot{"action_return": true}
    - utter_ask_identified_deed
* wrong{"name": "deed"}
    - slot{"name": "deed"}
    - action_update_option
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_ask_option_universalizable
* wrong{"name": "option"}
    - slot{"name": "option"}
    - action_update_option
    - slot{"action_return": true}
    - utter_ask_inherent_evil
* affirm
    - action_update_option
    - slot{"action_return": true}
    - utter_ask_consequences
* consequence{"stakeholder": "the consequence", "name": "alex", "sentiment": "pos"}
    - slot{"name": "alex"}
    - slot{"sentiment": "pos"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_positive
* correct
    - utter_ask_impact_weight
* quantity{"quantity": "8"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* wrong
    - utter_ask_consequence_probability
* quantity{"quantity": "5"}
    - action_update_consequence
    - slot{"action_return": true}
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

## Generated Story -9080873729863372859
* greeting
    - action_intro
* stakeholder{"name": "Dirk"}
    - slot{"name": "Dirk"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - action_check_identified_name
    - slot{"action_return": false}
    - utter_ask_identified_name
* correct
    - action_update_stakeholder
    - slot{"name": "Dirk"}
    - slot{"action_return": true}
    - utter_ask_moralstatus
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"name": "Thomas"}
    - slot{"name": "Thomas"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": true}
    - action_check_identified_name
    - slot{"action_return": false}
    - utter_ask_identified_name
* correct
    - action_update_stakeholder
    - slot{"name": "Thomas"}
    - slot{"action_return": true}
    - utter_ask_moralstatus
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"stakeholder": "a dog", "name": "cleopatra", "moralstatus": "animal"}
    - slot{"moralstatus": "animal"}
    - slot{"name": "cleopatra"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": true}
    - action_check_identified_name
    - slot{"action_return": false}
    - utter_ask_identified_name
* correct
    - action_update_stakeholder
    - slot{"name": "cleopatra"}
    - slot{"action_return": true}
    - utter_ask_identified_moralstatus
* correct
    - utter_ask_moralstatus_weight
* quantity{"quantity": "5"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* deny
    - utter_confirm_stakeholders
    - action_choose_decider
* decider{"name": "Thomas"}
    - slot{"name": "Thomas"}
    - action_update_stakeholder
    - slot{"decider": "Thomas"}
    - slot{"action_return": true}
    - utter_ask_options
* option{"name": "cleopatra", "deed": "kill"}
    - slot{"deed": "kill"}
    - slot{"name": "cleopatra"}
    - action_create_option
    - slot{"deed": "kill"}
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
* deny{"name": "needs_conditions"}
    - slot{"name": "needs_conditions"}
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_ask_consequences
* consequence{"name": "cleopatra", "sentiment": "neg"}
    - slot{"name": "cleopatra"}
    - slot{"sentiment": "neg"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_negative
* correct
    - utter_ask_impact_weight
* quantity{"quantity": "10"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* correct
    - utter_next_consequence
* consequence{"name": "Thomas", "sentiment": "neg"}
    - slot{"name": "Thomas"}
    - slot{"sentiment": "neg"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_negative
* correct
    - utter_ask_impact_weight
* quantity{"quantity": "6"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* wrong
    - utter_ask_consequence_probability
* quantity{"quantity": "60"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* deny
    - utter_next_option
* option{"name": "Thomas", "deed": "refuse to kill the dog"}
    - slot{"deed": "refuse to kill the dog"}
    - slot{"name": "Thomas"}
    - action_create_option
    - slot{"deed": "refuse to kill the dog"}
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
* consequence{"name": "cleopatra"}
    - slot{"name": "cleopatra"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact
* negative
    - action_update_consequence
    - slot{"action_return": false}
    - utter_ask_impact_weight
* quantity{"quantity": "9"}
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
    - slot{"action_return": true}
    - utter_next_method

