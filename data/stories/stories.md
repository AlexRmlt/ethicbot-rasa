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
    - followup{"name": "utter_ask_name_plural"}
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
    - followup{"name": "utter_ask_name_plural"}
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

## Generated Story 7168840357583075545
* greeting
    - action_intro
* stakeholder{"stakeholder": "i"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - utter_ask_name_singular
* name{"name": "Alex"}
    - slot{"name": "Alex"}
    - action_update_stakeholder
    - slot{"name": "Alex"}
    - slot{"action_return": true}
    - utter_ask_moralstatus
* inform{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholdergroup{"stakeholder": "a group of 100 people", "moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": true}
    - utter_ask_name_plural
* name
    - action_update_stakeholder
    - slot{"name": "the Hessians"}
    - slot{"action_return": true}
    - utter_ask_identified_moralstatus
* correct
    - utter_next_stakeholder
* stakeholdergroup{"stakeholder": "a lot of people", "moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": false}
    - utter_ask_quantity
* quantity{"quantity": "1"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_ask_name_singular
* name{"name": "Michael"}
    - slot{"name": "Michael"}
    - action_update_stakeholder
    - slot{"name": "Michael"}
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
* option{"stakeholder": "i"}
    - action_create_option
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_ask_deontic_modality
* inform{"deonticmodality": "obligation"}
    - action_update_option
    - slot{"action_return": true}
    - utter_ask_universalizable
* correct
    - action_update_option
    - slot{"action_return": true}
    - utter_ask_consequences
* consequence{"name": "Michael"}
    - slot{"name": "Michael"}
    - action_create_consequence
    - slot{"sentiment": null}
    - slot{"name": "them"}
    - slot{"action_return": true}
    - utter_ask_impact
* negative
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_impact_weight
* quantity{"quantity": "3,6"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* correct
    - utter_next_consequence
* consequence{"name": "Alex", "sentiment": "neu"}
    - slot{"name": "Alex"}
    - slot{"sentiment": "neu"}
    - action_create_consequence
    - slot{"name": "Alex"}
    - slot{"action_return": true}
    - utter_ask_impact
* deny
    - utter_next_option
* option{"deed": "not tell anyone"}
    - slot{"deed": "not tell anyone"}
    - action_create_option
    - slot{"deed": "keep his knowledge to himself"}
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
* inform{"reason": "no_reason"}
    - action_update_deed
    - slot{"deed": "not tell anyone"}
    - slot{"action_return": true}
    - utter_ask_identified_deed
* affirm
    - action_create_deed
    - slot{"action_return": true}
    - utter_ask_deontic_modality
* inform{"deonticmodality": "obligation"}
    - action_update_deed
    - slot{"action_return": true}
    - utter_ask_universalizable
* correct
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_ask_consequences
* consequence{"sentiment": "neu", "name": "Hessians"}
    - slot{"name": "Hessians"}
    - slot{"sentiment": "neu"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact
* negative
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_impact_weight
* quantity{"quantity": "4,56"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* correct
    - utter_next_consequence
* option
    - action_create_consequence
    - followup{"name": "action_choose_affected_stakeholder"}
    - slot{"name": null}
    - slot{"action_return": false}
    - action_choose_affected_stakeholder
* consequence{"name": "the Hessians"}
    - slot{"name": "the Hessians"}
    - action_create_consequence
    - slot{"name": "the Hessians"}
    - slot{"action_return": true}
    - utter_ask_impact
* positive
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_impact_weight
* quantity{"quantity": "4.78"}
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

## Generated Story -6793579357886827193
* greeting
    - action_intro
* stakeholdergroup{"quantity": "5"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": false}

## Generated Story -4803877908768115130
* greeting
    - action_intro
* stakeholdergroup{"quantity": "5"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": true}
    - utter_ask_name_plural
* deny
    - action_update_stakeholder
    - slot{"name": "the Hessians"}
    - slot{"action_return": true}
    - utter_ask_moralstatus
* inform{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"stakeholder": "a guy", "quantity": "5", "name": "Johann"}
    - slot{"name": "Johann"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": true}
    - action_check_identified_name
    - followup{"name": "utter_ask_identified_name"}
    - utter_ask_identified_name
* correct
    - action_update_stakeholder
    - slot{"name": "Johann"}
    - slot{"action_return": true}
    - utter_ask_moralstatus
* inform{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder

## Generated Story -500919905742562163
* greeting
    - action_intro
* stakeholder{"name": "leon"}
    - slot{"name": "leon"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - action_check_identified_name
    - followup{"name": "utter_ask_identified_name"}
    - utter_ask_identified_name
* correct
    - action_update_stakeholder
    - slot{"name": "leon"}
    - slot{"action_return": true}
    - utter_ask_moralstatus
* inform{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"name": "kilian", "moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - slot{"name": "kilian"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": true}
    - action_check_identified_name
    - followup{"name": "utter_ask_identified_name"}
    - utter_ask_identified_name
* correct
    - action_update_stakeholder
    - slot{"name": "kilian"}
    - slot{"action_return": true}
    - utter_ask_identified_moralstatus
* correct
    - utter_next_stakeholder
* stakeholder{"name": "luis", "moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - slot{"name": "luis"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": true}
    - action_check_identified_name
    - followup{"name": "utter_ask_identified_name"}
    - utter_ask_identified_name
* correct
    - action_update_stakeholder
    - slot{"name": "luis"}
    - slot{"action_return": true}
    - utter_ask_identified_moralstatus
* correct
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
* name{"name": "Harald"}
    - slot{"name": "Harald"}
    - action_update_stakeholder
    - slot{"decider": "Harald"}
    - slot{"name": "Harald"}
    - slot{"action_return": true}
    - utter_ask_moralstatus
* inform{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_ask_options
* option
    - action_create_option
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_ask_deontic_modality
* inform{"deonticmodality": "indifference"}
    - action_update_option
    - slot{"action_return": true}
    - utter_ask_universalizable
* correct
    - action_update_option
    - slot{"action_return": true}
    - utter_ask_consequences
* option
    - action_create_consequence
    - slot{"sentiment": null}
    - followup{"name": "action_choose_affected_stakeholder"}
    - slot{"name": null}
    - slot{"action_return": false}
    - action_choose_affected_stakeholder
* consequence{"name": "leon"}
    - slot{"name": "leon"}
    - action_create_consequence
    - slot{"sentiment": null}
    - slot{"name": "leon"}
    - slot{"action_return": true}
    - utter_ask_impact
* neutral
    - utter_next_consequence
* consequence{"name": "harry", "sentiment": "neg"}
    - slot{"name": "harry"}
    - slot{"sentiment": "neg"}
    - action_create_consequence
    - followup{"name": "action_choose_affected_stakeholder"}
    - slot{"name": null}
    - slot{"action_return": false}
    - action_choose_affected_stakeholder
* consequence{"name": "Harald"}
    - slot{"name": "Harald"}
    - action_create_consequence
    - slot{"name": "Harald"}
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

## Generated Story -1956901734285764416
* greeting
    - action_intro
* stakeholdergroup{"stakeholder": "a lot of people", "moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": false}
    - utter_ask_quantity
* quantity{"quantity": "20"}
    - action_update_stakeholder
    - followup{"name": "utter_ask_name_plural"}
    - slot{"action_return": true}
    - utter_ask_name_plural
* name{"stakeholder": "the terrorists"}
    - action_update_stakeholder
    - slot{"name": "the terrorists"}
    - slot{"action_return": true}
    - utter_ask_identified_moralstatus
* correct
    - utter_next_stakeholder
* stakeholdergroup{"stakeholder": "many people", "moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": false}
    - utter_ask_quantity
* quantity
    - action_update_stakeholder
    - followup{"name": "utter_ask_name_plural"}
    - slot{"action_return": true}
    - utter_ask_name_plural
* name{"stakeholder": "the passengers"}
    - action_update_stakeholder
    - slot{"name": "the passengers"}
    - slot{"action_return": true}
    - utter_ask_identified_moralstatus
* correct
    - utter_next_stakeholder
* decider{"stakeholder": "one person"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": true}
    - utter_ask_name_singular
* name
    - action_update_stakeholder
    - slot{"decider": "Hauke"}
    - slot{"name": "Hauke"}
    - slot{"action_return": true}
    - utter_ask_moralstatus
* inform{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholdergroup{"stakeholder": "a large crowd of people"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 4}
    - slot{"action_return": false}
    - utter_ask_quantity
* quantity{"quantity": "10000"}
    - action_update_stakeholder
    - followup{"name": "utter_ask_name_plural"}
    - slot{"action_return": true}
    - utter_ask_name_plural
* dontknow
    - action_update_stakeholder
    - slot{"name": "the Hessians"}
    - slot{"action_return": true}
    - utter_ask_moralstatus
* inform{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* deny
    - utter_confirm_stakeholders
    - utter_confirm_decider
    - utter_ask_options

## Generated Story -2861374149554873227
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
* inform{"moralstatus": "animal"}
    - slot{"moralstatus": "animal"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_ask_moralstatus_weight
* quantity{"quantity": "5"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_ask_options

## Generated Story 3479221795695379615
* greeting
    - action_intro
* stakeholder{"name": "ken", "moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - slot{"name": "ken"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - action_check_identified_name
    - followup{"name": "utter_ask_identified_name"}
    - utter_ask_identified_name
* correct
    - action_update_stakeholder
    - slot{"name": "ken"}
    - slot{"action_return": true}
    - utter_ask_identified_moralstatus
* correct
    - utter_next_stakeholder
* stakeholder{"name": "ken", "moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - slot{"name": "ken"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": true}
    - action_check_identified_name
    - followup{"name": "utter_ask_name_singular"}
    - utter_ask_name_singular
* name{"name": "Simon"}
    - slot{"name": "Simon"}
    - action_update_stakeholder
    - slot{"name": "Simon"}
    - slot{"action_return": true}
    - utter_ask_identified_moralstatus
* correct
    - utter_next_stakeholder
* stakeholdergroup{"stakeholder": "a lot of people", "name": "ken", "moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - slot{"name": "ken"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": false}
    - utter_ask_quantity
* quantity{"quantity": "10"}
    - action_update_stakeholder
    - followup{"name": "utter_ask_name_plural"}
    - slot{"action_return": true}
    - utter_ask_name_plural
* name
    - action_update_stakeholder
    - slot{"name": "the Bavarians"}
    - slot{"action_return": true}
    - utter_ask_identified_moralstatus
* correct
    - utter_next_stakeholder

## Generated Story -6483728836843920675
* greeting
    - action_intro
* stakeholder{"name": "Ken", "stakeholder": "a doctor", "moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - slot{"name": "Ken"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - action_check_identified_name
    - followup{"name": "utter_ask_identified_name"}
    - utter_ask_identified_name
* correct
    - action_update_stakeholder
    - slot{"name": "Ken"}
    - slot{"action_return": true}
    - utter_ask_identified_moralstatus
* correct
    - utter_next_stakeholder
* stakeholder{"name": "Ken", "stakeholder": "a patient", "moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - slot{"name": "Ken"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": true}
    - action_check_identified_name
    - followup{"name": "utter_ask_name_singular"}
    - utter_ask_name_singular
* name{"name": "Tyrone"}
    - slot{"name": "Tyrone"}
    - action_update_stakeholder
    - slot{"name": "Tyrone"}
    - slot{"action_return": true}
    - utter_ask_identified_moralstatus
* wrong
    - utter_ask_moralstatus
* inform{"moralstatus": "animal"}
    - slot{"moralstatus": "animal"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_ask_moralstatus_weight
* quantity{"quantity": "1"}
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
* name{"name": "Jamal"}
    - slot{"name": "Jamal"}
    - action_update_stakeholder
    - slot{"decider": "Jamal"}
    - slot{"name": "Jamal"}
    - slot{"action_return": true}
    - utter_ask_moralstatus
* inform{"moralstatus": "animal"}
    - slot{"moralstatus": "animal"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_ask_moralstatus_weight
* quantity{"quantity": "3"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_ask_options

