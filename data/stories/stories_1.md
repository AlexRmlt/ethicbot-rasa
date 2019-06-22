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
* inform{"moralstatus": "human"}
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
* inform{"moralstatus": "human"}
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
* inform{"moralstatus": "human"}
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
* inform{"moralstatus": "human"}
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
* affirm
    - action_create_deed
    - slot{"action_return": true}
    - utter_ask_deontic_modality
* inform{"deonticmodality": "permission"}
    - action_update_deed
    - slot{"action_return": true}
    - utter_ask_universalizable
* wrong
    - action_update_deed
    - slot{"action_return": true}
    - utter_ask_no_rule_reason
* inform{"reason": "inherently_evil"}
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

## Generated Story 5647621002996390469
* greeting
    - action_intro
* stakeholder{"name": "anton"}
    - slot{"name": "anton"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - action_check_identified_name
    - slot{"action_return": false}
    - utter_ask_identified_name
* correct
    - action_update_stakeholder
    - slot{"name": "anton"}
    - slot{"action_return": true}
    - utter_ask_moralstatus
* inform{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholdergroup
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": false}
    - utter_ask_quantity
* quantity{"quantity": "24"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_ask_name_plural
* name
    - action_update_stakeholder
    - slot{"name": "the Hessians"}
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
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": true}
    - utter_ask_name_singular
* name
    - action_update_stakeholder
    - slot{"name": "Toni"}
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
* decider{"name": "anton"}
    - slot{"name": "anton"}
    - action_update_stakeholder
    - slot{"decider": "anton"}
    - slot{"action_return": true}
    - utter_ask_options
* stakeholder{"name": "anton"}
    - slot{"name": "anton"}
    - action_create_option
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_ask_deontic_modality
* inform{"deonticmodality": "permission"}
    - action_update_option
    - slot{"action_return": true}
    - utter_ask_universalizable
* wrong
    - action_update_option
    - slot{"action_return": true}
    - utter_ask_no_rule_reason
* inform{"reason": "inherently_evil"}
    - action_update_option
    - slot{"action_return": true}
    - utter_ask_consequences
* consequence{"sentiment": "pos", "name": "Anton"}
    - slot{"name": "Anton"}
    - slot{"sentiment": "pos"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_positive
* correct
    - utter_ask_impact_weight
* quantity{"quantity": "7"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* correct
    - utter_next_consequence
* name{"name": "the Hessians"}
    - slot{"name": "the Hessians"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_positive
* wrong
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_impact_weight
* quantity{"quantity": "4"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* correct
    - utter_next_consequence
* consequence{"name": "the Hessians", "sentiment": "pos"}
    - slot{"name": "the Hessians"}
    - slot{"sentiment": "pos"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_positive
* wrong
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_impact_weight
* quantity{"quantity": "3"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* wrong
    - utter_ask_consequence_probability
* quantity{"quantity": "60"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* consequence{"sentiment": "pos"}
    - slot{"sentiment": "pos"}
    - action_create_consequence
    - followup{"name": "action_choose_affected_stakeholder"}
    - slot{"name": null}
    - slot{"action_return": false}
    - action_choose_affected_stakeholder
* consequence{"name": "the Hessians"}
    - slot{"name": "the Hessians"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_positive
* wrong
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

## Generated Story -261531004980772878
* greeting
    - action_intro
* stakeholder{"stakeholder": "my kitten"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - utter_ask_name_singular
* name{"name": "kitty"}
    - slot{"name": "kitty"}
    - action_update_stakeholder
    - slot{"name": "kitty"}
    - slot{"action_return": true}
    - utter_ask_moralstatus
* inform{"moralstatus": "animal"}
    - slot{"moralstatus": "animal"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_ask_moralstatus_weight
* quantity{"quantity": "9"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"stakeholder": "my cat", "moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": true}
    - utter_ask_name_singular
* name
    - action_update_stakeholder
    - slot{"name": "Alex"}
    - slot{"action_return": true}
    - utter_ask_identified_moralstatus
* correct
    - utter_next_stakeholder
* deny
    - utter_confirm_stakeholders
    - action_choose_decider
* decider{"name": "Alex"}
    - slot{"name": "Alex"}
    - action_update_stakeholder
    - slot{"decider": "Alex"}
    - slot{"action_return": true}
    - utter_ask_options
* option{"name": "Alex", "deed": "punish the cat"}
    - slot{"deed": "punish the cat"}
    - slot{"name": "Alex"}
    - action_create_option
    - slot{"deed": "punish the cat"}
    - slot{"action_return": true}
    - utter_ask_identified_deed
* deny
    - action_update_option
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_ask_deontic_modality
* inform{"deonticmodality": "permission"}
    - action_update_option
    - slot{"action_return": true}
    - utter_ask_universalizable
* correct
    - action_update_option
    - slot{"action_return": true}
    - utter_ask_consequences

## Generated Story 8273658228823907417
* greeting
    - action_intro
* stakeholder{"stakeholder": "a man", "moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - utter_ask_name_singular
* name
    - action_update_stakeholder
    - slot{"name": "Quinn"}
    - slot{"action_return": true}
    - utter_ask_identified_moralstatus
* correct
    - utter_next_stakeholder
* stakeholder
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": true}
    - utter_ask_name_singular
* name{"name": "kilian"}
    - slot{"name": "kilian"}
    - action_update_stakeholder
    - slot{"name": "kilian"}
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
    - utter_next_stakeholder
* deny
    - utter_confirm_stakeholders
    - action_choose_decider
* decider{"name": "Quinn"}
    - slot{"name": "Quinn"}
    - action_update_stakeholder
    - slot{"decider": "Quinn"}
    - slot{"action_return": true}
    - utter_ask_options

## Generated Story 6770686197240496771
* greeting
    - action_intro
* stakeholder
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - utter_ask_name_singular
* name{"name": "Kevin"}
    - slot{"name": "Kevin"}
    - action_update_stakeholder
    - slot{"name": "Kevin"}
    - slot{"action_return": true}
    - utter_ask_moralstatus
* inform{"name": "human"}
    - slot{"name": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"stakeholder": "a tourist", "name": "george", "moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - slot{"name": "george"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": true}
    - action_check_identified_name
    - slot{"action_return": false}
    - utter_ask_identified_name
* correct
    - action_update_stakeholder
    - slot{"name": "george"}
    - slot{"action_return": true}
    - utter_ask_identified_moralstatus
* correct
    - utter_next_stakeholder
* stakeholder{"name": "isabel"}
    - slot{"name": "isabel"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": true}
    - action_check_identified_name
    - slot{"action_return": false}
    - utter_ask_identified_name
* correct
    - action_update_stakeholder
    - slot{"name": "isabel"}
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
* decider{"name": "Kevin"}
    - slot{"name": "Kevin"}
    - action_update_stakeholder
    - slot{"decider": "Kevin"}
    - slot{"action_return": true}
    - utter_ask_options

