## Generated Story 4250896942926339107
* greeting
    - action_intro
* stakeholdergroup{"stakeholder": "five workmen", "quantity": "5", "moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - utter_ask_name_plural
* deny
    - action_update_stakeholder
    - slot{"name": "the Palatines"}
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"name": "Molly", "quantity": "5", "moralstatus": "human"}
    - slot{"name": "Molly"}
    - slot{"moralstatus": "human"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": true}
    - action_check_identified_name
    - slot{"action_return": false}
    - utter_ask_identified_name
* correct
    - action_update_stakeholder
    - slot{"name": "Molly"}
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"name": "Molly"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": true}
    - action_check_identified_name
    - slot{"action_return": false}
    - utter_ask_identified_name
* wrong
    - action_update_stakeholder
    - slot{"name": "Nathan"}
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* deny
    - utter_confirm_stakeholders
    - action_choose_decider
* decider{"name": "Molly"}
    - action_update_stakeholder
    - slot{"decider": "Molly"}
    - slot{"action_return": true}
    - utter_ask_options
* option{"deed": "do nothing"}
    - slot{"deed": "do nothing"}
    - action_create_option
    - slot{"deed": "do nothing"}
    - slot{"option": 4}
    - slot{"action_return": true}
    - utter_ask_identified_deed
* correct
    - action_create_deed
    - slot{"action_return": true}
    - utter_ask_universalizable
* wrong
    - action_update_deed
    - slot{"action_return": true}
    - utter_ask_inherent_evil
* affirm
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deny
    - utter_ask_consequences
* consequence{"stakeholder": "the five workmen", "quantity": "5", "sentiment": "neg"}
    - slot{"sentiment": "neg"}
    - action_create_consequence
    - slot{"name": null}
    - slot{"action_return": false}
    - action_choose_affected_stakeholder
* consequence{"name": "the Palatines"}
    - slot{"name": "the Palatines"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_negative
* correct
    - action_update_consequence
    - slot{"action_return": false}
    - utter_ask_impact_weight
* quantity{"quantity": "10"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* correct
    - utter_next_consequence
* consequence{"name": "Nathan"}
    - slot{"name": "Nathan"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_negative
* wrong
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_impact_weight
* quantity{"quantity": "8"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* correct
    - utter_next_consequence
* deny
    - utter_next_option
* option
    - action_create_option
    - slot{"deed": null}
    - slot{"option": 8}
    - slot{"action_return": true}
    - utter_ask_deed
* deed{"deed": "Killing Nathan"}
    - action_create_deed
    - slot{"deed": "Killing Nathan by pushing him off the bridge"}
    - slot{"action_return": true}
    - utter_ask_universalizable
* wrong
    - action_update_deed
    - slot{"action_return": true}
    - utter_ask_inherent_evil
* affirm
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deed{"deed": "saving the lives", "quantity": "5"}
    - slot{"deed": "saving the lives"}
    - action_create_deed
    - slot{"action_return": true}
    - utter_ask_universalizable
* correct
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deny
    - utter_ask_consequences
* consequence{"name": "Nathan", "sentiment": "neg"}
    - slot{"name": "Nathan"}
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
* consequence{"name": "the Palatines", "sentiment": "pos"}
    - slot{"sentiment": "pos"}
    - action_create_consequence
    - slot{"name": null}
    - slot{"action_return": false}
    - action_choose_affected_stakeholder
* consequence{"name": "the Palatines"}
    - slot{"name": "the Palatines"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_positive
* correct
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
    - slot{"image": "url"}
    - utter_report_image
    - utter_next_method
* affirm
    - utter_ask_method
* deontology
    - utter_starting_evaluation_1
    - utter_starting_evaluation_2
    - action_evaluation_deontology
    - slot{"action_return": true}
    - slot{"image": "url"}
    - utter_report_image
    - utter_next_method
* deny
    - utter_goodbye

## Generated Story 7358352807131470407
* greeting
    - action_intro
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
    - utter_ask_moral_status
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholdergroup{"stakeholder": "a patient", "name": "Ken", "moralstatus": "human"}
    - slot{"name": "Ken"}
    - slot{"moralstatus": "human"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": false}
    - utter_ask_quantity
* quantity{"quantity": "only one"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - action_check_identified_name
    - slot{"action_return": false}
    - utter_ask_identified_name
* wrong
    - action_update_stakeholder
    - slot{"name": "Inga"}
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholdergroup{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": false}
    - utter_ask_quantity
* dontknow
    - utter_ask_guess_quantity
* quantity
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_ask_name_plural
* name
    - action_update_stakeholder
    - slot{"name": "Inga"}
    - slot{"action_return": true}
    - utter_next_stakeholder
* deny
    - utter_confirm_stakeholders
    - action_choose_decider
* decider{"name": "Ken"}
    - action_update_stakeholder
    - slot{"decider": "Ken"}
    - slot{"action_return": true}
    - utter_ask_options
* option{"name": "Ken"}
    - slot{"name": "Ken"}
    - action_create_option
    - slot{"deed": null}
    - slot{"option": 4}
    - slot{"action_return": true}
    - utter_ask_deed
* deed{"name": "Inga"}
    - slot{"name": "Inga"}
    - action_create_deed
    - slot{"deed": "This would imply actively killing Inga."}
    - slot{"action_return": true}
    - utter_ask_universalizable
* wrong
    - action_update_deed
    - slot{"action_return": true}
    - utter_ask_inherent_evil
* affirm
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deed{"deed": "saving the lives"}
    - slot{"deed": "saving the lives"}
    - action_create_deed
    - slot{"action_return": true}
    - utter_ask_universalizable
* correct
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deny
    - utter_ask_consequences
* consequence{"name": "Inga"}
    - slot{"name": "Inga"}
    - action_create_consequence
    - slot{"action_return": false}
    - utter_ask_impact
* negative
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_impact_weight
* quantity{"quantity": "ten"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* correct
    - utter_next_consequence
* consequence{"name": "the saxons", "name": "the Saxons", "sentiment": "neu"}
    - slot{"name": "the saxons"}
    - slot{"sentiment": "neu"}
    - action_create_consequence
    - slot{"action_return": false}
    - utter_ask_impact
* positive
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_impact_weight
* quantity{"quantity": "7"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* correct
    - utter_next_consequence
* deny
    - utter_next_option
* option{"name": "Inga"}
    - slot{"name": "Inga"}
    - action_create_option
    - slot{"deed": null}
    - slot{"option": 9}
    - slot{"action_return": true}
    - utter_ask_deed
* deed
    - action_create_deed
    - slot{"deed": "Refraining from abusing the patient-doctor mutual trust would be a morally relevant action"}
    - slot{"action_return": true}
    - utter_ask_universalizable
* correct
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deed
    - action_create_deed
    - slot{"deed": "One must also consider the action of not saving many people from the threat of being infected with HIV."}
    - slot{"action_return": true}
    - utter_ask_universalizable
* wrong
    - action_update_deed
    - slot{"action_return": true}
    - utter_ask_inherent_evil
* affirm
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deny
    - utter_ask_consequences
* consequence{"name": "the saxons", "sentiment": "neg"}
    - slot{"name": "the saxons"}
    - slot{"sentiment": "neg"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_negative
* correct
    - utter_ask_impact_weight
* quantity{"quantity": "8"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* wrong
    - utter_ask_consequence_probability
* quantity
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* consequence{"sentiment": "neu"}
    - slot{"sentiment": "neu"}
    - action_create_consequence
    - slot{"name": null}
    - slot{"action_return": false}
    - action_choose_affected_stakeholder
* consequence{"name": "Inga"}
    - slot{"name": "Inga"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact
* positive
    - action_update_consequence
    - slot{"action_return": true}
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
* deontology
    - utter_starting_evaluation_1
    - utter_starting_evaluation_2
    - action_evaluation_deontology
    - slot{"action_return": true}
    - slot{"image": "url"}
    - utter_report_image
    - utter_next_method
* affirm
    - utter_ask_method
* utilitarism
    - utter_starting_evaluation_1
    - utter_starting_evaluation_2
    - action_evaluation_utilitarism
    - slot{"action_return": true}
    - slot{"image": "url"}
    - utter_report_image
    - utter_next_method
* deny
    - utter_goodbye

## Generated Story -6025756364314501582
* greeting
    - action_intro
* stakeholdergroup{"name": "Tom"}
    - slot{"name": "Tom"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": false}
    - utter_ask_quantity
* quantity{"quantity": "only one"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - action_check_identified_name
    - slot{"action_return": false}
    - utter_ask_identified_name
* correct
    - action_update_stakeholder
    - slot{"name": "Patrick"}
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholdergroup{"quantity": "8", "moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": true}
    - utter_ask_quantity
* quantity{"quantity": "8"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_ask_name_plural
* name{"quantity": "eight"}
    - action_update_stakeholder
    - slot{"name": "the Rhinelanders"}
    - slot{"action_return": true}
    - utter_next_stakeholder
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
* name
    - action_update_stakeholder
    - slot{"name": "the Saxons"}
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholdergroup{"quantity": "One", "name": "Tom", "deed": "kill him"}
    - slot{"name": "Tom"}
    - slot{"deed": "kill him"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 4}
    - slot{"action_return": true}
    - utter_ask_quantity
* quantity{"quantity": "only one"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - action_check_identified_name
    - slot{"action_return": false}
    - utter_ask_identified_name
* wrong
    - action_update_stakeholder
    - slot{"name": "Esther"}
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"deed": "kill", "name": "Tom"}
    - slot{"name": "Tom"}
    - slot{"deed": "kill"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 5}
    - slot{"action_return": true}
    - action_check_identified_name
    - slot{"action_return": false}
    - utter_ask_identified_name
* wrong
    - action_update_stakeholder
    - slot{"name": "Amelie"}
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* deny
    - utter_confirm_stakeholders
    - action_choose_decider
* decider{"name": "Patrick"}
    - action_update_stakeholder
    - slot{"decider": "Patrick"}
    - slot{"action_return": true}
    - utter_ask_options
* option{"deed": "kill one", "name": "Tom", "quantity": "one"}
    - slot{"name": "Tom"}
    - slot{"deed": "kill one"}
    - action_create_option
    - slot{"deed": "kill one"}
    - slot{"option": 6}
    - slot{"action_return": true}
    - utter_ask_identified_deed
* correct
    - action_create_deed
    - slot{"action_return": true}
    - utter_ask_universalizable
* wrong
    - action_update_deed
    - slot{"action_return": true}
    - utter_ask_inherent_evil
* affirm
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deed
    - action_create_deed
    - slot{"deed": "Torturing his fellow hostage"}
    - slot{"action_return": true}
    - utter_ask_universalizable
* wrong
    - action_update_deed
    - slot{"action_return": true}
    - utter_ask_inherent_evil
* affirm
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deed{"deed": "saving", "quantity": "eight"}
    - slot{"deed": "saving"}
    - action_create_deed
    - slot{"action_return": true}
    - utter_ask_universalizable
* correct
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deny
    - utter_ask_consequences
* consequence{"name": "Amelie", "sentiment": "neg"}
    - slot{"name": "Amelie"}
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
* consequence{"name": "Tom", "quantity": "eight", "sentiment": "pos"}
    - slot{"name": "Tom"}
    - slot{"sentiment": "pos"}
    - action_create_consequence
    - slot{"name": null}
    - slot{"action_return": false}
    - action_choose_affected_stakeholder
* consequence{"name": "the Rhinelanders"}
    - slot{"name": "the Rhinelanders"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_positive
* correct
    - utter_ask_impact_weight
* quantity{"quantity": "9"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* correct
    - utter_next_consequence
* consequence{"name": "the Saxons", "sentiment": "neg"}
    - slot{"name": "the saxons"}
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
* deny
    - utter_next_option
* option{"deed": "kill one", "quantity": "one"}
    - slot{"deed": "kill one"}
    - action_create_option
    - slot{"deed": "kill one"}
    - slot{"option": 13}
    - slot{"action_return": true}
    - utter_ask_identified_deed
* wrong
    - action_update_option
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deed
    - action_create_deed
    - slot{"deed": "It would mean refraining from saving himself and the children"}
    - slot{"action_return": true}
    - utter_ask_universalizable
* wrong
    - action_update_deed
    - slot{"action_return": true}
    - utter_ask_inherent_evil
* deny
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deny
    - utter_ask_consequences
* consequence{"name": "the Saxons", "sentiment": "neg"}
    - slot{"name": "the saxons"}
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
* consequence{"name": "Patrick", "sentiment": "neg"}
    - slot{"name": "Patrick"}
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
* consequence{"name": "the Rhinelanders", "sentiment": "neg"}
    - slot{"name": "the Rhinelanders"}
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
    - slot{"image": "url"}
    - utter_report_image
    - utter_next_method
* affirm
    - utter_ask_method
* deontology
    - utter_starting_evaluation_1
    - utter_starting_evaluation_2
    - action_evaluation_deontology
    - slot{"action_return": true}
    - slot{"image": "url"}
    - utter_report_image
    - utter_next_method
* deny
    - utter_goodbye

## Generated Story -5384821882511551639
* greeting
    - action_intro
* stakeholder{"name": "Mary"}
    - slot{"name": "Mary"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - action_check_identified_name
    - slot{"action_return": false}
    - utter_ask_identified_name
* correct
    - action_update_stakeholder
    - slot{"name": "Mary"}
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"stakeholder": "a", "name": "Mary", "moralstatus": "human"}
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
* stakeholder{"name": "Samuels"}
    - slot{"name": "Samuels"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": true}
    - action_check_identified_name
    - slot{"action_return": false}
    - utter_ask_identified_name
* wrong
    - action_update_stakeholder
    - slot{"name": "Greta"}
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"quantity": "7", "name": "Samuel"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 4}
    - slot{"action_return": true}
    - utter_ask_name_singular
* name
    - action_update_stakeholder
    - slot{"name": "Amelie"}
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* deny
    - utter_confirm_stakeholders
    - action_choose_decider
* decider{"name": "Mary"}
    - action_update_stakeholder
    - slot{"decider": "Mary"}
    - slot{"action_return": true}
    - utter_ask_options
* option{"name": "samuel"}
    - slot{"name": "samuel"}
    - action_create_option
    - slot{"deed": null}
    - slot{"option": 5}
    - slot{"action_return": true}
    - utter_ask_deed
* deed
    - action_create_deed
    - slot{"deed": "This implies killing a person"}
    - slot{"action_return": true}
    - utter_ask_universalizable
* wrong
    - action_update_deed
    - slot{"action_return": true}
    - utter_ask_inherent_evil
* affirm
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deed{"name": "Samuels"}
    - slot{"name": "Samuels"}
    - action_create_deed
    - slot{"deed": "It also means helping Samuels family"}
    - slot{"action_return": true}
    - utter_ask_universalizable
* wrong
    - action_update_deed
    - slot{"action_return": true}
    - utter_ask_inherent_evil
* deny
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deny
    - utter_ask_consequences
* consequence{"name": "Amelie", "sentiment": "neg"}
    - slot{"name": "Amelie"}
    - slot{"sentiment": "neg"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_negative
* correct
    - utter_ask_impact_weight
* quantity{"quantity": "1"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* correct
    - utter_next_consequence
* consequence{"name": "Greta"}
    - slot{"name": "Greta"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_negative
* wrong
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_impact_weight
* quantity{"quantity": "7"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* wrong
    - utter_ask_consequence_probability
* quantity
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* consequence{"name": "samuel"}
    - slot{"name": "samuel"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_negative
* wrong
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_impact_weight
* quantity{"quantity": "5"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* wrong
    - utter_ask_consequence_probability
* quantity
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* deny
    - utter_next_option
* option{"deed": "refrain from killing", "name": "samuel"}
    - slot{"name": "samuel"}
    - slot{"deed": "refrain from killing"}
    - action_create_option
    - slot{"deed": "refrain from killing"}
    - slot{"option": 11}
    - slot{"action_return": true}
    - utter_ask_identified_deed
* correct
    - action_create_deed
    - slot{"action_return": true}
    - utter_ask_universalizable
* correct
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deny
    - utter_ask_consequences
* consequence{"name": "Amelie", "sentiment": "neu"}
    - slot{"name": "Amelie"}
    - slot{"sentiment": "neu"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact
* positive
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_impact_weight
* quantity{"quantity": "2"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* wrong
    - utter_ask_consequence_probability
* quantity{"quantity": "75"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* consequence{"name": "samuel"}
    - slot{"name": "samuel"}
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
* consequence{"name": "Greta", "sentiment": "neu"}
    - slot{"name": "Greta"}
    - slot{"sentiment": "neu"}
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
* deny
    - utter_got_everything
    - utter_ask_method
* utilitarism
    - utter_starting_evaluation_1
    - utter_starting_evaluation_2
    - action_evaluation_utilitarism
    - slot{"action_return": true}
    - slot{"image": "url"}
    - utter_report_image
    - utter_next_method
* affirm
    - utter_ask_method
* deontology
    - utter_starting_evaluation_1
    - utter_starting_evaluation_2
    - action_evaluation_deontology
    - slot{"action_return": true}
    - slot{"image": "url"}
    - utter_report_image
    - utter_next_method
* deny
    - utter_goodbye

## Generated Story 3846139624378699522
* greeting
    - action_intro
* stakeholdergroup{"stakeholder": "the first person", "name": "Jane", "quantity": "two", "moralstatus": "human"}
    - slot{"name": "Jane"}
    - slot{"moralstatus": "human"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - utter_ask_quantity
* quantity{"quantity": "only one"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - action_check_identified_name
    - slot{"action_return": false}
    - utter_ask_identified_name
* correct
    - action_update_stakeholder
    - slot{"name": "Jane"}
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholdergroup{"stakeholder": "a group of other people", "moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": false}
    - utter_ask_quantity
* dontknow
    - utter_ask_guess_quantity
* quantity{"quantity": "10"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_ask_name_plural
* name
    - action_update_stakeholder
    - slot{"name": "the Swabians"}
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"name": "Jane"}
    - slot{"name": "Jane"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": true}
    - action_check_identified_name
    - slot{"action_return": false}
    - utter_ask_identified_name
* wrong
    - action_update_stakeholder
    - slot{"name": "Amelie"}
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholdergroup
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 4}
    - slot{"action_return": false}
    - utter_ask_quantity
* quantity{"quantity": "about 5"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_ask_name_plural
* name
    - action_update_stakeholder
    - slot{"name": "the Bavarians"}
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* deny
    - utter_confirm_stakeholders
    - action_choose_decider
* decider{"name": "Jane"}
    - action_update_stakeholder
    - slot{"decider": "Jane"}
    - slot{"action_return": true}
    - utter_ask_options
* option{"name": "Jane"}
    - slot{"name": "Jane"}
    - action_create_option
    - slot{"deed": null}
    - slot{"option": 5}
    - slot{"action_return": true}
    - utter_ask_deed
* deed
    - action_create_deed
    - slot{"deed": "It would mean killing her baby because the heat of the furnace would overheat the child."}
    - slot{"action_return": true}
    - utter_ask_universalizable
* wrong
    - action_update_deed
    - slot{"action_return": true}
    - utter_ask_inherent_evil
* affirm
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deed
    - action_create_deed
    - slot{"deed": "There is also the action of saving her and the others life."}
    - slot{"action_return": true}
    - utter_ask_universalizable
* correct
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deny
    - utter_ask_consequences
* consequence{"name": "Amelie", "sentiment": "neg"}
    - slot{"name": "Amelie"}
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
* quantity
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* consequence{"name": "the swabians", "sentiment": "neg"}
    - slot{"name": "the swabians"}
    - slot{"sentiment": "neg"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_negative
* correct
    - utter_ask_impact_weight
* quantity{"quantity": "Only 2"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* correct
    - utter_next_consequence
* consequence{"name": "Jane", "sentiment": "neg"}
    - slot{"name": "Jane"}
    - slot{"sentiment": "neg"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_negative
* correct
    - utter_ask_impact_weight
* quantity{"quantity": "9"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* correct
    - utter_next_consequence
* deny
    - utter_next_option
* option{"deed": "do nothing"}
    - slot{"deed": "do nothing"}
    - action_create_option
    - slot{"deed": "do nothing"}
    - slot{"option": 11}
    - slot{"action_return": true}
    - utter_ask_identified_deed
* correct
    - action_create_deed
    - slot{"action_return": true}
    - utter_ask_universalizable
* wrong
    - action_update_deed
    - slot{"action_return": true}
    - utter_ask_inherent_evil
* deny
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deny
    - utter_ask_consequences
* consequence{"name": "the swabians", "sentiment": "neg"}
    - slot{"name": "the swabians"}
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
* consequence{"name": "Amelie", "quantity": "2"}
    - slot{"name": "Amelie"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_negative
* wrong
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_impact_weight
* quantity{"quantity": "8"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* correct
    - utter_next_consequence
* consequence{"name": "Jane", "sentiment": "neg"}
    - slot{"name": "Jane"}
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
    - slot{"image": "url"}
    - utter_report_image
    - utter_next_method
* affirm
    - utter_ask_method
* deontology
    - utter_starting_evaluation_1
    - utter_starting_evaluation_2
    - action_evaluation_deontology
    - slot{"action_return": true}
    - slot{"image": "url"}
    - utter_report_image
    - utter_next_method
* deny
    - utter_goodbye
    
## Generated Story 1277434377440136980
* greeting
    - action_intro
* stakeholder{"name": "Mark", "stakeholder": "a crewperson", "moralstatus": "human"}
    - slot{"name": "mark"}
    - slot{"moralstatus": "human"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - action_check_identified_name
    - slot{"action_return": false}
    - utter_ask_identified_name
* correct
    - action_update_stakeholder
    - slot{"name": "mark"}
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholdergroup{"stakeholder": "a group"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": false}
    - utter_ask_quantity
* quantity{"quantity": "6"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_ask_name_plural
* name
    - action_update_stakeholder
    - slot{"name": "the Palatines"}
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"quantity": "One"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": true}
    - utter_ask_name_singular
* name
    - action_update_stakeholder
    - slot{"name": "J\u00f6rg"}
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* deny
    - utter_confirm_stakeholders
    - action_choose_decider
* decider{"name": "mark"}
    - action_update_stakeholder
    - slot{"decider": "mark"}
    - slot{"action_return": true}
    - utter_ask_options
* option{"name": "mark"}
    - slot{"name": "mark"}
    - action_create_option
    - slot{"deed": null}
    - slot{"option": 4}
    - slot{"action_return": true}
    - utter_ask_deed
* deed{"deed": "saving the lives"}
    - slot{"deed": "saving the lives"}
    - action_create_deed
    - slot{"action_return": true}
    - utter_ask_universalizable
* correct
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deed{"name": "J\u00f6rg"}
    - slot{"name": "J\u00f6rg"}
    - action_create_deed
    - slot{"deed": "It would also mean killing J\u00f6rg because his body would get crushed by the emergency access hatch."}
    - slot{"action_return": true}
    - utter_ask_universalizable
* wrong
    - action_update_deed
    - slot{"action_return": true}
    - utter_ask_inherent_evil
* affirm
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deny
    - utter_ask_consequences
* consequence{"name": "J\u00f6rg", "sentiment": "neg"}
    - slot{"name": "J\u00f6rg"}
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
* consequence{"name": "the Palatines", "sentiment": "neu"}
    - slot{"sentiment": "neu"}
    - action_create_consequence
    - slot{"name": null}
    - slot{"action_return": false}
    - action_choose_affected_stakeholder
* consequence{"name": "the Palatines"}
    - slot{"name": "the Palatines"}
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
* consequence{"name": "Mark", "sentiment": "neu"}
    - slot{"name": "Mark"}
    - slot{"sentiment": "neu"}
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
* deny
    - utter_next_option
* option{"name": "J\u00f6rg", "deed": "refrain from"}
    - slot{"name": "J\u00f6rg"}
    - slot{"deed": "refrain from"}
    - action_create_option
    - slot{"deed": "refrain from"}
    - slot{"option": 10}
    - slot{"action_return": true}
    - utter_ask_identified_deed
* wrong
    - action_update_option
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deed
    - action_create_deed
    - slot{"deed": "The option implies letting his crew and himself die by lack of oxygen."}
    - slot{"action_return": true}
    - utter_ask_universalizable
* wrong
    - action_update_deed
    - slot{"action_return": true}
    - utter_ask_inherent_evil
* affirm
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deny
    - utter_ask_consequences
* consequence{"name": "J\u00f6rg", "sentiment": "neu"}
    - slot{"name": "J\u00f6rg"}
    - slot{"sentiment": "neu"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact
* positive{"name": "J\u00f6rg"}
    - slot{"name": "J\u00f6rg"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_impact_weight
* quantity{"quantity": "7"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* wrong
    - utter_ask_consequence_probability
* quantity
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* consequence{"name": "the Palatines", "sentiment": "neg"}
    - slot{"sentiment": "neg"}
    - action_create_consequence
    - slot{"name": null}
    - slot{"action_return": false}
    - action_choose_affected_stakeholder
* consequence{"name": "the Palatines"}
    - slot{"name": "the Palatines"}
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
* consequence{"name": "Mark", "sentiment": "pos"}
    - slot{"name": "mark"}
    - slot{"sentiment": "pos"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_positive
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
    - slot{"image": "url"}
    - utter_report_image
    - utter_next_method
* affirm
    - utter_ask_method
* utilitarism
    - utter_starting_evaluation_1
    - utter_starting_evaluation_2
    - action_evaluation_utilitarism
    - slot{"action_return": true}
    - slot{"image": "url"}
    - utter_report_image
    - utter_next_method
* deny
    - utter_goodbye
    
## Generated Story 5601750309873569494
* greeting
    - action_intro
* stakeholdergroup{"quantity": "5", "moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": true}
    - utter_ask_quantity
* quantity{"quantity": "5"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_ask_name_plural
* name
    - action_update_stakeholder
    - slot{"name": "the Swabians"}
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholdergroup{"name": "Molly", "quantity": "5", "moralstatus": "human"}
    - slot{"name": "molly"}
    - slot{"moralstatus": "human"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": true}
    - utter_ask_quantity
* quantity{"quantity": "only one"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - action_check_identified_name
    - slot{"action_return": false}
    - utter_ask_identified_name
* correct
    - action_update_stakeholder
    - slot{"name": "molly"}
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 4}
    - slot{"action_return": true}
    - utter_ask_name_singular
* deny
    - action_update_stakeholder
    - slot{"name": "Tanja"}
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* deny
    - utter_confirm_stakeholders
    - action_choose_decider

## Generated Story -8606621332840856950
* greeting
    - action_intro
* stakeholdergroup{"quantity": "5", "moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - utter_ask_quantity
* quantity{"stakeholder": "five persons", "quantity": "5"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_ask_name_plural
* name
    - action_update_stakeholder
    - slot{"name": "the Palatines"}
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"name": "Molly"}
    - slot{"name": "molly"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": true}
    - action_check_identified_name
    - slot{"action_return": false}
    - utter_ask_identified_name
* correct
    - action_update_stakeholder
    - slot{"name": "molly"}
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": true}
    - utter_ask_name_singular
* deny
    - action_update_stakeholder
    - slot{"name": "Katharina"}
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* deny
    - utter_confirm_stakeholders
    - action_choose_decider
* decider{"name": "molly"}
    - action_update_stakeholder
    - slot{"decider": "molly"}
    - slot{"action_return": true}
    - utter_ask_options
* option
    - action_create_option
    - slot{"deed": null}
    - slot{"option": 4}
    - slot{"action_return": true}
    - utter_ask_deed
* deed
    - action_create_deed
    - slot{"deed": "It would imply killing Katharina."}
    - slot{"action_return": true}
    - utter_ask_universalizable
* wrong
    - action_update_deed
    - slot{"action_return": true}
    - utter_ask_inherent_evil
* affirm
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deed{"deed": "saving the lives"}
    - slot{"deed": "saving the lives"}
    - utter_ask_identified_deed
* correct
    - action_create_deed
    - slot{"action_return": true}
    - utter_ask_universalizable
* correct
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deny
    - utter_ask_consequences
* consequence{"name": "Katharina", "sentiment": "neg"}
    - slot{"sentiment": "neg"}
    - action_create_consequence
    - slot{"name": null}
    - slot{"action_return": false}
    - action_choose_affected_stakeholder
* consequence{"name": "Katharina"}
    - slot{"name": "Katharina"}
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
* consequence{"name": "the Palatines", "sentiment": "neu"}
    - slot{"sentiment": "neu"}
    - action_create_consequence
    - slot{"name": null}
    - slot{"action_return": false}
    - action_choose_affected_stakeholder
* consequence{"name": "the Palatines"}
    - slot{"name": "the Palatines"}
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
* deny
    - utter_next_option
* option{"deed": "refrain from pushing"}
    - slot{"deed": "refrain from pushing"}
    - action_create_option
    - slot{"deed": "refrain from pushing"}
    - slot{"option": 9}
    - slot{"action_return": true}
    - utter_ask_identified_deed
* correct
    - action_create_deed
    - slot{"action_return": true}
    - utter_ask_universalizable
* correct
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deed
    - action_create_deed
    - slot{"deed": "Also it would imply letting the workmen die."}
    - slot{"action_return": true}
    - utter_ask_universalizable
* wrong
    - action_update_deed
    - slot{"action_return": true}
    - utter_ask_inherent_evil
* affirm
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deny
    - utter_ask_consequences
* consequence{"name": "the Palatines", "sentiment": "neg"}
    - slot{"sentiment": "neg"}
    - action_create_consequence
    - slot{"name": null}
    - slot{"action_return": false}
    - action_choose_affected_stakeholder
* consequence{"name": "the Palatines"}
    - slot{"name": "the Palatines"}
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
* consequence{"name": "Katharina", "sentiment": "neu"}
    - slot{"sentiment": "neu"}
    - action_create_consequence
    - slot{"name": null}
    - slot{"action_return": false}
    - action_choose_affected_stakeholder
* consequence{"name": "Katharina"}
    - slot{"name": "Katharina"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact
* positive
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_impact_weight
* quantity{"quantity": "7"}
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
* deontology
    - utter_starting_evaluation_1
    - utter_starting_evaluation_2
    - action_evaluation_deontology
    - slot{"action_return": true}
    - slot{"image": "url"}
    - utter_report_image
    - utter_next_method
* affirm
    - utter_ask_method
* utilitarism
    - utter_starting_evaluation_1
    - utter_starting_evaluation_2
    - action_evaluation_utilitarism
    - slot{"action_return": true}
    - slot{"image": "url"}
    - utter_report_image
    - utter_next_method
* deny
    - utter_goodbye

## Generated Story 5900225719431929188
* greeting
    - action_intro
* stakeholder{"name": "Heather", "quantity": "four", "moralstatus": "human"}
    - slot{"name": "heather"}
    - slot{"moralstatus": "human"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - action_check_identified_name
    - slot{"action_return": false}
    - utter_ask_identified_name
* correct
    - action_update_stakeholder
    - slot{"name": "heather"}
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"quantity": "two"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": true}
    - utter_ask_name_singular
* dontknow
    - action_update_stakeholder
    - slot{"name": "Zoe"}
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"quantity": "One"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": true}
    - utter_ask_name_singular
* name{"name": "Herbert"}
    - slot{"name": "Herbert"}
    - action_update_stakeholder
    - slot{"name": "Herbert"}
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* deny
    - utter_confirm_stakeholders
    - action_choose_decider
* decider{"name": "heather"}
    - action_update_stakeholder
    - slot{"decider": "heather"}
    - slot{"action_return": true}
    - utter_ask_options
* option{"deed": "refuse to"}
    - slot{"deed": "refuse to"}
    - action_create_option
    - slot{"deed": "refuse to"}
    - slot{"option": 4}
    - slot{"action_return": true}
    - utter_ask_identified_deed
* wrong
    - action_update_option
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deed
    - action_create_deed
    - slot{"deed": "Letting the crewmember die is for sure an action of moral relevance."}
    - slot{"action_return": true}
    - utter_ask_universalizable
* wrong
    - action_update_deed
    - slot{"action_return": true}
    - utter_ask_inherent_evil
* affirm
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deed{"deed": "saving"}
    - slot{"deed": "saving"}
    - action_create_deed
    - slot{"action_return": true}
    - utter_ask_universalizable
* correct
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deny
    - utter_ask_consequences
* consequence{"name": "Herbert", "sentiment": "neg"}
    - slot{"name": "Herbert"}
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
* consequence{"name": "zoe", "sentiment": "neu"}
    - slot{"name": "zoe"}
    - slot{"sentiment": "neu"}
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
* consequence{"name": "Heather", "sentiment": "neu"}
    - slot{"name": "heather"}
    - slot{"sentiment": "neu"}
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
* deny
    - utter_next_option
* option
    - slot{"name": "Herbert"}
    - action_create_option
    - slot{"deed": null}
    - slot{"option": 10}
    - slot{"action_return": true}
    - utter_ask_deed
* deed{"deed": "saving the life"}
    - slot{"deed": "saving the life"}
    - action_create_deed
    - slot{"action_return": true}
    - utter_ask_universalizable
* wrong
    - action_update_deed
    - slot{"action_return": true}
    - utter_ask_inherent_evil
* deny
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deny
    - utter_ask_consequences
* consequence{"name": "Herbert", "sentiment": "neu"}
    - slot{"name": "Herbert"}
    - slot{"sentiment": "neu"}
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
* consequence{"name": "Heather", "sentiment": "neg"}
    - slot{"name": "heather"}
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
    - slot{"image": "url"}
    - utter_report_image
    - utter_next_method
* affirm
    - utter_ask_method
* deontology
    - utter_starting_evaluation_1
    - utter_starting_evaluation_2
    - action_evaluation_deontology
    - slot{"action_return": true}
    - slot{"image": "url"}
    - utter_report_image
    - utter_next_method
* deny
    - utter_goodbye

## Generated Story -5279776952862841305
* greeting
    - action_intro
* stakeholder{"name": "Doug"}
    - slot{"name": "Doug"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - action_check_identified_name
    - slot{"action_return": false}
    - utter_ask_identified_name
* correct
    - action_update_stakeholder
    - slot{"name": "Doug"}
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholdergroup{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": false}
    - utter_ask_quantity
* quantity{"quantity": "About 20"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_ask_name_plural
* dontknow
    - action_update_stakeholder
    - slot{"name": "the Hessians"}
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"stakeholder": "a group of old people", "name": "Doug"}
    - slot{"name": "Doug"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": false}
    - action_check_identified_name
    - slot{"action_return": false}
    - utter_ask_identified_name
* wrong
    - action_update_stakeholder
    - slot{"name": "the Rhinelanders"}
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* deny
    - utter_confirm_stakeholders
    - action_choose_decider
* decider{"name": "Doug"}
    - action_update_stakeholder
    - slot{"decider": "Doug"}
    - slot{"action_return": true}
    - utter_ask_options
* option{"deed": "refuse"}
    - slot{"deed": "refuse"}
    - action_create_option
    - slot{"deed": "refuse"}
    - slot{"option": 8}
    - slot{"action_return": true}
    - utter_ask_identified_deed
* correct
    - action_create_deed
    - slot{"action_return": true}
    - utter_ask_universalizable
* wrong
    - action_update_deed
    - slot{"action_return": true}
    - utter_ask_inherent_evil
* affirm
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deed{"deed": "saving his life"}
    - slot{"deed": "saving his life"}
    - action_create_deed
    - slot{"action_return": true}
    - utter_ask_universalizable
* correct
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deny
    - utter_ask_consequences
* consequence{"name": "the Rhinelanders", "sentiment": "neg"}
    - slot{"name": "the Rhinelanders"}
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
* quantity{"quantity": "90"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* consequence{"sentiment": "neu"}
    - slot{"sentiment": "neu"}
    - action_create_consequence
    - slot{"name": null}
    - slot{"action_return": false}
    - action_choose_affected_stakeholder
* consequence{"name": "the Hessians"}
    - slot{"name": "the Hessians"}
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
* wrong
    - utter_ask_consequence_probability
* quantity
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* consequence{"name": "Doug", "sentiment": "neu"}
    - slot{"name": "Doug"}
    - slot{"sentiment": "neu"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact
* positive
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_impact_weight
* quantity{"quantity": "7"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* wrong
    - utter_ask_consequence_probability
* quantity
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* deny
    - utter_next_option
* option
    - action_create_option
    - slot{"deed": null}
    - slot{"option": 14}
    - slot{"action_return": true}
    - utter_ask_deed
* deed{"deed": "saving"}
    - slot{"deed": "saving"}
    - action_create_deed
    - slot{"action_return": true}
    - utter_ask_universalizable
* correct
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deed
    - action_create_deed
    - slot{"deed": "It also implies bringing the lives of all passengers in the lifeboat in danger."}
    - slot{"action_return": true}
    - utter_ask_universalizable
* wrong
    - action_update_deed
    - slot{"action_return": true}
    - utter_ask_inherent_evil
* affirm
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deny
    - utter_ask_consequences
* consequence{"name": "the Rhinelanders", "sentiment": "neu"}
    - slot{"name": "the Rhinelanders"}
    - slot{"sentiment": "neu"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact
* positive
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_impact_weight
* quantity{"quantity": "9"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* wrong
    - utter_ask_consequence_probability
* quantity
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* consequence{"sentiment": "neg"}
    - slot{"sentiment": "neg"}
    - action_create_consequence
    - slot{"name": null}
    - slot{"action_return": false}
    - action_choose_affected_stakeholder
* consequence{"name": "the Hessians"}
    - slot{"name": "the Hessians"}
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
* quantity
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* consequence{"name": "Doug", "sentiment": "neg"}
    - slot{"name": "Doug"}
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
    - slot{"image": "url"}
    - utter_report_image
    - utter_next_method
* deny
    - utter_goodbye
* thanks
    - utter_thanks

## Generated Story 7321710744913522518
* greeting
    - action_intro
* stakeholder{"name": "Carrie"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - utter_ask_name_singular
* name{"name": "Carrie"}
    - slot{"name": "Carrie"}
    - action_update_stakeholder
    - slot{"name": "Carrie"}
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholdergroup{"stakeholder": "four of her patients", "deed": "kill the four", "quantity": "four"}
    - slot{"deed": "kill the four"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": true}
    - utter_ask_name_plural
* deny
    - action_update_stakeholder
    - slot{"name": "the Hessians"}
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"quantity": "one"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": true}
    - utter_ask_name_singular
* name{"name": "frank"}
    - slot{"name": "frank"}
    - action_update_stakeholder
    - slot{"name": "frank"}
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* deny
    - utter_confirm_stakeholders
    - action_choose_decider
* decider{"name": "Carrie"}
    - action_update_stakeholder
    - slot{"decider": "Carrie"}
    - slot{"action_return": true}
    - utter_ask_options
* option{"quantity": "four"}
    - action_create_option
    - slot{"deed": null}
    - slot{"option": 4}
    - slot{"action_return": true}
    - utter_ask_deed
* deed{"quantity": "four"}
    - action_create_deed
    - slot{"deed": "It means avoiding the death of the four patients."}
    - slot{"action_return": true}
    - utter_ask_universalizable
* correct
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deed
    - action_create_deed
    - slot{"deed": "It also means killing the single person in the other room."}
    - slot{"action_return": true}
    - utter_ask_universalizable
* wrong
    - action_update_deed
    - slot{"action_return": true}
    - utter_ask_inherent_evil
* affirm
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deny
    - utter_ask_consequences
* consequence{"name": "frank", "deed": "kill him", "sentiment": "neg"}
    - slot{"name": "frank"}
    - slot{"deed": "kill him"}
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
* consequence{"sentiment": "neu"}
    - slot{"sentiment": "neu"}
    - action_create_consequence
    - slot{"name": null}
    - slot{"action_return": false}
    - action_choose_affected_stakeholder
* consequence{"name": "the Hessians"}
    - slot{"name": "the Hessians"}
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
* deny
    - utter_next_option
* option{"deed": "do nothing", "stakeholder": "four people", "quantity": "four"}
    - slot{"deed": "do nothing"}
    - action_create_option
    - slot{"deed": "do nothing"}
    - slot{"option": 9}
    - slot{"action_return": true}
    - utter_ask_identified_deed
* correct
    - action_create_deed
    - slot{"action_return": true}
    - utter_ask_universalizable
* wrong
    - action_update_deed
    - slot{"action_return": true}
    - utter_ask_inherent_evil
* deny
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deny
    - utter_ask_consequences
* consequence{"sentiment": "neg"}
    - slot{"sentiment": "neg"}
    - action_create_consequence
    - slot{"name": null}
    - slot{"action_return": false}
    - action_choose_affected_stakeholder
* consequence{"name": "the Hessians"}
    - slot{"name": "the Hessians"}
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
* consequence{"name": "frank", "sentiment": "neu"}
    - slot{"name": "frank"}
    - slot{"sentiment": "neu"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact
* positive
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_impact_weight
* quantity{"quantity": "7"}
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
    - slot{"image": "url"}
    - utter_report_image
    - utter_next_method
* deny
    - utter_goodbye
* thanks
    - utter_thanks

## Generated Story -8888859435742633065
* greeting
    - action_intro
* stakeholder
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - utter_ask_name_singular
* dontknow
    - action_update_stakeholder
    - slot{"name": "Inga"}
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"name": "Inga"}
    - slot{"name": "Inga"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": true}
    - action_check_identified_name
    - slot{"action_return": false}
    - utter_ask_identified_name
* wrong
    - action_update_stakeholder
    - slot{"name": "Carla"}
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"name": "Carla"}
    - slot{"name": "Carla"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": true}
    - action_check_identified_name
    - slot{"action_return": false}
    - utter_ask_identified_name
* wrong
    - action_update_stakeholder
    - slot{"name": "Viola"}
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* deny
    - utter_confirm_stakeholders
    - action_choose_decider
* decider{"name": "Inga"}
    - slot{"name": "Inga"}
    - action_update_stakeholder
    - slot{"decider": "Inga"}
    - slot{"action_return": true}
    - utter_ask_options
* option
    - action_create_option
    - slot{"deed": null}
    - slot{"option": 4}
    - slot{"action_return": true}
    - utter_ask_deed
* deed
    - action_create_deed
    - slot{"deed": "Killing her own son"}
    - slot{"action_return": true}
    - utter_ask_universalizable
* wrong
    - action_update_deed
    - slot{"action_return": true}
    - utter_ask_inherent_evil
* affirm
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deed
    - action_create_deed
    - slot{"deed": "Saving an innocent persons life."}
    - slot{"action_return": true}
    - utter_ask_universalizable
* correct
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deny
    - utter_ask_consequences
* consequence{"name": "Carla", "sentiment": "neg"}
    - slot{"name": "Carla"}
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
* consequence{"name": "inga", "sentiment": "neg"}
    - slot{"name": "inga"}
    - slot{"sentiment": "neg"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_negative
* correct
    - utter_ask_impact_weight
* quantity{"quantity": "9"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* correct
    - utter_next_consequence
* consequence{"sentiment": "pos"}
    - slot{"sentiment": "pos"}
    - action_create_consequence
    - slot{"name": null}
    - slot{"action_return": false}
    - action_choose_affected_stakeholder
* consequence{"name": "Viola"}
    - slot{"name": "Viola"}
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
* deny
    - utter_next_option
* option{"name": "inga"}
    - slot{"name": "inga"}
    - action_create_option
    - slot{"deed": null}
    - slot{"option": 10}
    - slot{"action_return": true}
    - utter_ask_deed
* deed
    - action_create_deed
    - slot{"deed": "It would mean letting an innocent person get killed"}
    - slot{"action_return": true}
    - utter_ask_universalizable
* wrong
    - action_update_deed
    - slot{"action_return": true}
    - utter_ask_inherent_evil
* affirm
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deny
    - utter_ask_consequences
* consequence{"name": "Carla", "sentiment": "neg"}
    - slot{"name": "Carla"}
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
* consequence{"sentiment": "neg"}
    - slot{"sentiment": "neg"}
    - action_create_consequence
    - slot{"name": null}
    - slot{"action_return": false}
    - action_choose_affected_stakeholder
* consequence{"name": "Viola"}
    - slot{"name": "Viola"}
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
* deny
    - utter_got_everything
    - utter_ask_method
* deontology
    - utter_starting_evaluation_1
    - utter_starting_evaluation_2
    - action_evaluation_deontology
    - slot{"action_return": true}
    - slot{"image": "url"}
    - utter_report_image
    - utter_next_method
* deny
    - utter_goodbye
* thanks
    - utter_thanks

## Generated Story 7740751080933251549
* greeting
    - action_intro
* stakeholder
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - utter_ask_name_singular
* dontknow
    - action_update_stakeholder
    - slot{"name": "Inga"}
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": true}
    - utter_ask_name_singular
* deny
    - action_update_stakeholder
    - slot{"name": "Roswitha"}
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"stakeholder": "a man", "moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": true}
    - utter_ask_name_singular
* name
    - action_update_stakeholder
    - slot{"name": "Michelle"}
    - slot{"action_return": true}
    - utter_next_stakeholder
* deny
    - utter_confirm_stakeholders
    - action_choose_decider
* decider{"name": "Inga"}
    - slot{"name": "Inga"}
    - action_update_stakeholder
    - slot{"decider": "Inga"}
    - slot{"action_return": true}
    - utter_ask_options
* option
    - action_create_option
    - slot{"deed": null}
    - slot{"option": 4}
    - slot{"action_return": true}
    - utter_ask_deed
* deed{"deed": "saving her life"}
    - slot{"deed": "saving her life"}
    - action_create_deed
    - slot{"action_return": true}
    - utter_ask_universalizable
* correct
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deed{"name": "Ignoring Michelle"}
    - slot{"name": "Ignoring Michelle"}
    - action_create_deed
    - slot{"deed": "Ignoring Michelle could be a morally condemnable action as she needs also medical attention"}
    - slot{"action_return": true}
    - utter_ask_universalizable
* wrong
    - action_update_deed
    - slot{"action_return": true}
    - utter_ask_inherent_evil
* affirm
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deny
    - utter_ask_consequences
* consequence{"name": "inga", "sentiment": "pos"}
    - slot{"name": "inga"}
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
* dontknow
    - utter_ask_guess_quantity
* quantity
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* consequence{"name": "Michelle"}
    - slot{"name": "Michelle"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_positive
* wrong
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_impact_weight
* quantity{"quantity": "10"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* wrong
    - utter_ask_consequence_probability
* quantity
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* deny
    - utter_next_option
* option{"name": "Michelle"}
    - slot{"name": "Michelle"}
    - action_create_option
    - slot{"deed": null}
    - slot{"option": 9}
    - slot{"action_return": true}
    - utter_ask_deed
* deed{"deed": "saving the life", "name": "Michelle"}
    - slot{"name": "Michelle"}
    - slot{"deed": "saving the life"}
    - action_create_deed
    - slot{"action_return": true}
    - utter_ask_universalizable
* correct
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deny
    - utter_ask_consequences
* consequence{"name": "Roswitha", "sentiment": "neg"}
    - slot{"name": "Roswitha"}
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
* consequence{"name": "Michelle", "sentiment": "neg"}
    - slot{"name": "Michelle"}
    - slot{"sentiment": "neg"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_negative
* wrong
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_impact_weight
* quantity{"quantity": "8"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* wrong
    - utter_ask_consequence_probability
* dontknow
    - utter_ask_guess_quantity
* dontknow
    - utter_too_bad
    - utter_next_consequence
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
    - slot{"image": "url"}
    - utter_report_image
    - utter_next_method
* deny
    - utter_goodbye
* thanks
    - utter_thanks
    
## Generated Story 1978581040960796565
* greeting
    - action_intro
* stakeholder{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - utter_ask_name_singular
* name{"name": "mark"}
    - slot{"name": "mark"}
    - action_update_stakeholder
    - slot{"name": "mark"}
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"name": "mark"}
    - slot{"name": "mark"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": true}
    - action_check_identified_name
    - slot{"action_return": false}
    - utter_ask_identified_name
* wrong
    - action_update_stakeholder
    - slot{"name": "Viola"}
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"name": "Mark"}
    - slot{"name": "Mark"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": true}
    - action_check_identified_name
    - slot{"action_return": false}
    - utter_ask_identified_name
* wrong
    - action_update_stakeholder
    - slot{"name": "Zoe"}
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* deny
    - utter_confirm_stakeholders
    - action_choose_decider
* decider{"name": "mark"}
    - slot{"name": "mark"}
    - action_update_stakeholder
    - slot{"decider": "mark"}
    - slot{"action_return": true}
    - utter_ask_options
* option{"deed": "tell his friend"}
    - slot{"deed": "tell his friend"}
    - action_create_option
    - slot{"deed": "tell his friend"}
    - slot{"option": 4}
    - slot{"action_return": true}
    - utter_ask_identified_deed
* correct
    - action_create_deed
    - slot{"action_return": true}
    - utter_ask_universalizable
* wrong
    - action_update_deed
    - slot{"action_return": true}
    - utter_ask_inherent_evil
* deny
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deed
    - action_create_deed
    - slot{"deed": "Violating the companies policy of information security"}
    - slot{"action_return": true}
    - utter_ask_universalizable
* wrong
    - action_update_deed
    - slot{"action_return": true}
    - utter_ask_inherent_evil
* affirm
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deny
    - utter_ask_consequences
* consequence{"name": "mark"}
    - slot{"name": "mark"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact
* negative
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_impact_weight
* quantity{"quantity": "5"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* wrong
    - utter_ask_consequence_probability
* quantity
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* consequence{"sentiment": "neu"}
    - slot{"sentiment": "neu"}
    - action_create_consequence
    - slot{"name": null}
    - slot{"action_return": false}
    - action_choose_affected_stakeholder
* consequence{"name": "Viola"}
    - slot{"name": "Viola"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact
* negative
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_impact_weight
* quantity{"quantity": "4"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* correct
    - utter_next_consequence
* consequence{"name": "zoe"}
    - slot{"name": "zoe"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact
* neutral
    - utter_next_consequence
* deny
    - utter_next_option
* option{"name": "Mark"}
    - slot{"name": "Mark"}
    - action_create_option
    - slot{"deed": null}
    - slot{"option": 10}
    - slot{"action_return": true}
    - utter_ask_deed
* deed
    - action_create_deed
    - slot{"deed": "Complying to the companies laws"}
    - slot{"action_return": true}
    - utter_ask_universalizable
* correct
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deed
    - action_create_deed
    - slot{"deed": "Hiding information from a good friend"}
    - slot{"action_return": true}
    - utter_ask_universalizable
* wrong
    - action_update_deed
    - slot{"action_return": true}
    - utter_ask_inherent_evil
* affirm
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deny
    - utter_ask_consequences
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
    - slot{"image": "url"}
    - utter_report_image
    - utter_next_method

## Generated Story -7493447606517739501
* greeting
    - action_intro
* stakeholdergroup{"stakeholder": "a group of five people", "quantity": "5", "moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - utter_ask_name_plural
* deny
    - action_update_stakeholder
    - slot{"name": "the Rhinelanders"}
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholdergroup{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": false}
    - utter_ask_quantity
* quantity{"quantity": "only one"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_ask_name_singular
* name{"name": "carla"}
    - slot{"name": "carla"}
    - action_update_stakeholder
    - slot{"name": "carla"}
    - slot{"action_return": true}
    - utter_next_stakeholder
* deny
    - utter_confirm_stakeholders
    - action_choose_decider
* decider{"name": "the Rhinelanders"}
    - slot{"name": "the Rhinelanders"}
    - action_update_stakeholder
    - slot{"decider": "the Rhinelanders"}
    - slot{"action_return": true}
    - utter_ask_options
* stakeholder{"quantity": "one"}
    - action_create_option
    - slot{"deed": null}
    - slot{"option": 3}
    - slot{"action_return": true}
    - utter_ask_deed
* deed
    - action_create_deed
    - slot{"deed": "Using the dynamite means killing the pregnant woman"}
    - slot{"action_return": true}
    - utter_ask_universalizable
* wrong
    - action_update_deed
    - slot{"action_return": true}
    - utter_ask_inherent_evil
* affirm
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deny
    - utter_ask_consequences
* consequence{"name": "Carla", "sentiment": "neg"}
    - slot{"name": "Carla"}
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
* consequence{"name": "the Rhinelanders", "sentiment": "neg"}
    - slot{"name": "the Rhinelanders"}
    - slot{"sentiment": "neg"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_negative
* wrong
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_impact_weight
* quantity{"quantity": "7"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* correct
    - utter_next_consequence
* deny
    - utter_next_option
* option
    - action_create_option
    - slot{"deed": null}
    - slot{"option": 7}
    - slot{"action_return": true}
    - utter_ask_deed
* dontknow
    - utter_ask_consequences
* consequence{"name": "carla", "sentiment": "neu"}
    - slot{"name": "carla"}
    - slot{"sentiment": "neu"}
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
* wrong
    - utter_ask_consequence_probability
* quantity
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* consequence{"name": "the Rhinelanders", "sentiment": "neg"}
    - slot{"name": "the Rhinelanders"}
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
    - slot{"image": "url"}
    - utter_report_image
    - utter_next_method
* affirm
    - utter_ask_method
* deontology
    - utter_starting_evaluation_1
    - utter_starting_evaluation_2
    - action_evaluation_deontology
    - slot{"action_return": true}
    - slot{"image": "url"}
    - utter_report_image
    - utter_next_method
* deny
    - utter_goodbye

## Generated Story 599148369303593516
* greeting
    - action_intro
* stakeholdergroup{"stakeholder": "a person", "moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": false}
    - utter_ask_quantity
* quantity{"quantity": "one"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_ask_name_singular
* deny
    - action_update_stakeholder
    - slot{"name": "Inga"}
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"quantity": "7"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": true}
    - utter_ask_name_singular
* dontknow
    - action_update_stakeholder
    - slot{"name": "Werner"}
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"quantity": "7"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": true}
    - utter_ask_name_singular
* dontknow
    - action_update_stakeholder
    - slot{"name": "Carla"}
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* deny
    - utter_confirm_stakeholders
    - action_choose_decider
* decider{"name": "Inga"}
    - slot{"name": "Inga"}
    - action_update_stakeholder
    - slot{"decider": "Inga"}
    - slot{"action_return": true}
    - utter_ask_options
* option
    - action_create_option
    - slot{"deed": null}
    - slot{"option": 4}
    - slot{"action_return": true}
    - utter_ask_deed
* deed{"deed": "rescuing"}
    - slot{"deed": "rescuing"}
    - action_create_deed
    - slot{"action_return": true}
    - utter_ask_universalizable
* correct
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* dontknow
    - utter_ask_consequences
* consequence{"name": "Werner", "sentiment": "pos"}
    - slot{"name": "Werner"}
    - slot{"sentiment": "pos"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_positive
* correct
    - utter_ask_impact_weight
* quantity{"quantity": "6"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* correct
    - utter_next_consequence
* consequence{"name": "carla"}
    - slot{"name": "carla"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_positive
* wrong
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_impact_weight
* quantity{"quantity": "10"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* wrong
    - utter_ask_consequence_probability
* quantity
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* deny
    - utter_next_option
* option
    - action_create_option
    - slot{"deed": null}
    - slot{"option": 8}
    - slot{"action_return": true}
    - utter_ask_deed
* deed{"deed": "rescuing"}
    - slot{"deed": "rescuing"}
    - action_create_deed
    - slot{"action_return": true}
    - utter_ask_universalizable
* correct
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deny
    - utter_ask_consequences
* consequence{"name": "Werner", "sentiment": "neg"}
    - slot{"name": "Werner"}
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
* quantity
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* consequence{"name": "carla", "sentiment": "pos"}
    - slot{"name": "carla"}
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
    - slot{"image": "url"}
    - utter_report_image
    - utter_next_method
* deny
    - utter_goodbye

## Generated Story -2022503381031583469
* greeting
    - action_intro
* stakeholdergroup
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": false}
    - utter_ask_quantity
* quantity{"quantity": "only one"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_ask_name_singular
* name{"name": "Carl"}
    - slot{"name": "Carl"}
    - action_update_stakeholder
    - slot{"name": "Carl"}
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": true}
    - utter_ask_name_singular
* name
    - action_update_stakeholder
    - slot{"name": "Esther"}
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"moralstatus": "animal"}
    - slot{"moralstatus": "animal"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": true}
    - utter_ask_name_singular
* dontknow
    - action_update_stakeholder
    - slot{"name": "Patrick"}
    - slot{"action_return": true}
    - utter_next_stakeholder
* deny
    - utter_confirm_stakeholders
    - action_choose_decider
* decider{"name": "Carl"}
    - slot{"name": "Carl"}
    - action_update_stakeholder
    - slot{"decider": "Carl"}
    - slot{"action_return": true}
    - utter_ask_options
* option
    - action_create_option
    - slot{"deed": null}
    - slot{"option": 4}
    - slot{"action_return": true}
    - utter_ask_deed
* deed
    - action_create_deed
    - slot{"deed": "Protecting his son"}
    - slot{"action_return": true}
    - utter_ask_universalizable
* correct
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deed
    - action_create_deed
    - slot{"deed": "This would also mean lying to the police"}
    - slot{"action_return": true}
    - utter_ask_universalizable
* wrong
    - action_update_deed
    - slot{"action_return": true}
    - utter_ask_inherent_evil
* affirm
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deny
    - utter_ask_consequences
* consequence{"name": "Carl", "deed": "lead to a life"}
    - slot{"name": "Carl"}
    - slot{"deed": "lead to a life"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact
* negative
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_impact_weight
* quantity{"quantity": "9"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* wrong
    - utter_ask_consequence_probability
* quantity{"quantity": "only 70"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* consequence{"sentiment": "pos"}
    - slot{"sentiment": "pos"}
    - action_create_consequence
    - slot{"name": null}
    - slot{"action_return": false}
    - action_choose_affected_stakeholder
* consequence{"name": "Patrick"}
    - slot{"name": "Patrick"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_positive
* correct
    - utter_ask_impact_weight
* quantity{"quantity": "7"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* wrong
    - utter_ask_consequence_probability
* quantity
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* dontknow
    - utter_next_option
* option{"deed": "remain silent"}
    - slot{"deed": "remain silent"}
    - action_create_option
    - slot{"deed": "remain silent"}
    - slot{"option": 9}
    - slot{"action_return": true}
    - utter_ask_identified_deed
* correct
    - action_create_deed
    - slot{"action_return": true}
    - utter_ask_universalizable
* wrong
    - action_update_deed
    - slot{"action_return": true}
    - utter_ask_inherent_evil
* deny
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* dontknow
    - utter_ask_consequences
* consequence{"name": "esther"}
    - slot{"name": "esther"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_positive
* wrong
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_impact_weight
* quantity{"quantity": "9"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* wrong
    - utter_ask_consequence_probability
* quantity
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* consequence{"name": "Patrick", "sentiment": "pos"}
    - slot{"name": "Patrick"}
    - slot{"sentiment": "pos"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_positive
* correct
    - utter_ask_impact_weight
* quantity{"quantity": "5"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* correct
    - utter_next_consequence
* consequence{"name": "Carl", "sentiment": "pos"}
    - slot{"name": "Carl"}
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
* correct
    - utter_next_consequence
* deny
    - utter_next_option
* deny
    - utter_got_everything
    - utter_ask_method

## Generated Story -8382762037602468367
* greeting
    - action_intro
* stakeholdergroup{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": false}
    - utter_ask_quantity
* quantity{"stakeholder": "one person", "quantity": "one"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_ask_name_singular
* deny
    - action_update_stakeholder
    - slot{"name": "Olga"}
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholdergroup{"quantity": "Hundreds", "moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": false}
    - utter_ask_quantity
* dontknow
    - utter_ask_guess_quantity
* quantity{"quantity": "500"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_ask_name_plural
* deny
    - action_update_stakeholder
    - slot{"name": "the Swabians"}
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": false}
    - utter_ask_name_singular
* name
    - action_update_stakeholder
    - slot{"name": "the Saxons"}
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus{"moralstatus": "human"}
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
* option
    - action_create_option
    - slot{"deed": null}
    - slot{"option": 6}
    - slot{"action_return": true}
    - utter_ask_deed
* deed
    - action_create_deed
    - slot{"deed": "Torturing"}
    - slot{"action_return": true}
    - utter_ask_universalizable
* wrong
    - action_update_deed
    - slot{"action_return": true}
    - utter_ask_inherent_evil
* affirm
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deed{"deed": "saving the lives"}
    - slot{"deed": "saving the lives"}
    - action_create_deed
    - slot{"action_return": true}
    - utter_ask_universalizable
* correct
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deny
    - utter_ask_consequences
* consequence{"name": "the Saxons", "sentiment": "neg"}
    - slot{"name": "the Saxons"}
    - slot{"sentiment": "neg"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_negative
* correct
    - utter_ask_impact_weight
* quantity{"quantity": "9"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* correct
    - utter_next_consequence
* consequence{"name": "Olga", "sentiment": "neg"}
    - slot{"name": "Olga"}
    - slot{"sentiment": "neg"}
    - action_create_consequence
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
* consequence{"name": "Olga"}
    - slot{"name": "Olga"}
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
* wrong
    - utter_ask_consequence_probability
* quantity
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* deny
    - utter_next_option
* option{"name": "Olga"}
    - slot{"name": "Olga"}
    - action_create_option
    - slot{"deed": null}
    - slot{"option": 12}
    - slot{"action_return": true}
    - utter_ask_deed
* deed
    - action_create_deed
    - slot{"deed": "Obeying the law"}
    - slot{"action_return": true}
    - utter_ask_universalizable
* correct
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deed
    - action_create_deed
    - slot{"deed": "On the other hand it would mean letting many innocent people die"}
    - slot{"action_return": true}
    - utter_ask_universalizable
* wrong
    - action_update_deed
    - slot{"action_return": true}
    - utter_ask_inherent_evil
* affirm
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deny
    - utter_ask_consequences
* consequence{"sentiment": "neg"}
    - slot{"sentiment": "neg"}
    - action_create_consequence
    - slot{"name": null}
    - slot{"action_return": false}
    - action_choose_affected_stakeholder

## Generated Story -7566024354162496183
* greeting
    - action_intro
* stakeholder{"stakeholder": "a person", "moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - utter_ask_name_singular
* dontknow
    - action_update_stakeholder
    - slot{"name": "Lars"}
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholdergroup{"stakeholder": "a group of passengers"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": false}
    - utter_ask_quantity
* quantity{"quantity": "9"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_ask_name_plural
* name{"stakeholder": "the passengers"}
    - action_update_stakeholder
    - slot{"name": "the passengers"}
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* deny
    - utter_confirm_stakeholders
    - action_choose_decider
* decider{"name": "Lars"}
    - slot{"name": "Lars"}
    - action_update_stakeholder
    - slot{"decider": "Lars"}
    - slot{"action_return": true}
    - utter_ask_options
* option
    - action_create_option
    - slot{"deed": null}
    - slot{"option": 3}
    - slot{"action_return": true}
    - utter_ask_deed
* deed{"deed": "leaving behind the other passengers"}
    - slot{"deed": "leaving behind the other passengers"}
    - action_create_deed
    - slot{"action_return": true}
    - utter_ask_universalizable
* wrong
    - action_update_deed
    - slot{"action_return": true}
    - utter_ask_inherent_evil
* affirm
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deny
    - utter_ask_consequences
* consequence{"name": "the passengers", "sentiment": "neu"}
    - slot{"name": "the passengers"}
    - slot{"sentiment": "neu"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact
* negative
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_impact_weight
* quantity{"quantity": "10"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* wrong
    - utter_ask_consequence_probability
* quantity
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* consequence{"sentiment": "pos"}
    - slot{"sentiment": "pos"}
    - action_create_consequence
    - slot{"name": null}
    - slot{"action_return": false}
    - action_choose_affected_stakeholder
* consequence{"name": "Lars"}
    - slot{"name": "Lars"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_positive
* correct
    - utter_ask_impact_weight
* quantity{"quantity": "6"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* correct
    - utter_next_consequence
* deny
    - utter_next_option
* option
    - action_create_option
    - slot{"deed": null}
    - slot{"option": 7}
    - slot{"action_return": true}
    - utter_ask_deed
* deed
    - action_create_deed
    - slot{"deed": "Being loyal to people relying on him"}
    - slot{"action_return": true}
    - utter_ask_universalizable
* correct
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deny
    - utter_ask_consequences
* consequence{"name": "the passengers", "sentiment": "pos"}
    - slot{"name": "the passengers"}
    - slot{"sentiment": "pos"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_positive
* correct
    - utter_ask_impact_weight
* quantity{"quantity": "9"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* wrong
    - utter_ask_consequence_probability
* quantity
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* consequence{"sentiment": "pos"}
    - slot{"sentiment": "pos"}
    - action_create_consequence
    - slot{"name": null}
    - slot{"action_return": false}
    - action_choose_affected_stakeholder
* consequence{"name": "Lars"}
    - slot{"name": "Lars"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_positive
* wrong
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_impact_weight
* quantity{"quantity": "8"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* wrong
    - utter_ask_consequence_probability
* quantity
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* deny
    - utter_next_option
* deny
    - utter_got_everything
    - utter_ask_method

## Generated Story -2566483661797900972
* greeting
    - action_intro
* decider{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": false}
    - utter_ask_quantity
* quantity{"quantity": "1"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_ask_name_singular
* name{"stakeholder": "the captain"}
    - action_update_stakeholder
    - slot{"decider": "the captain"}
    - slot{"name": "the captain"}
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholdergroup{"stakeholder": "30 people", "quantity": "7", "moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": true}
    - utter_ask_name_plural
* name{"stakeholder": "the passengers"}
    - action_update_stakeholder
    - slot{"name": "the passengers"}
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"stakeholder": "the weaker people"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 4}
    - slot{"action_return": false}
    - utter_ask_name_singular
* deny
    - action_update_stakeholder
    - slot{"name": "the Palatines"}
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* deny
    - utter_confirm_stakeholders
    - utter_confirm_decider
    - utter_ask_options
* option
    - action_create_option
    - slot{"deed": null}
    - slot{"option": 5}
    - slot{"action_return": true}
    - utter_ask_deed
* deed{"deed": "killing"}
    - slot{"deed": "killing"}
    - action_create_deed
    - slot{"action_return": true}
    - utter_ask_universalizable
* wrong
    - action_update_deed
    - slot{"action_return": true}
    - utter_ask_inherent_evil
* affirm
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deed{"deed": "saving the rest of the people"}
    - slot{"deed": "saving the rest of the people"}
    - action_create_deed
    - slot{"action_return": true}
    - utter_ask_universalizable
* correct
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deny
    - utter_ask_consequences
* consequence{"name": "the Palatines", "sentiment": "neg"}
    - slot{"name": "the Palatines"}
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
* consequence{"stakeholder": "the passengers", "sentiment": "pos"}
    - slot{"sentiment": "pos"}
    - action_create_consequence
    - slot{"name": null}
    - slot{"action_return": false}
    - action_choose_affected_stakeholder
* consequence{"name": "the passengers"}
    - slot{"name": "the passengers"}
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
* quantity{"quantity": "80"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* deny
    - utter_next_option
* option
    - action_create_option
    - slot{"deed": null}
    - slot{"option": 10}
    - slot{"action_return": true}
    - utter_ask_deed
* deny
    - utter_ask_consequences
* consequence{"stakeholder": "the passengers", "sentiment": "neg"}
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
* quantity{"quantity": "20"}
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
    - slot{"image": "url"}
    - utter_report_image
    - utter_next_method
* deny
    - utter_goodbye

## Generated Story -6641505184854451966
* greeting
    - action_intro
* stakeholder
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - utter_ask_name_singular
* name
    - action_update_stakeholder
    - slot{"name": "Nathan"}
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus{"moralstatus": "other"}
    - slot{"moralstatus": "other"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_ask_moral_status_weight
* dontknow
    - utter_too_bad
    - utter_next_stakeholder
* stakeholder
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": true}
    - utter_ask_name_singular
* deny
    - action_update_stakeholder
    - slot{"name": "Uwe"}
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholdergroup{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": false}
    - utter_ask_quantity
* quantity
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_ask_name_singular
* name{"stakeholder": "the child"}
    - action_update_stakeholder
    - slot{"name": "the child"}
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
* deny{"stakeholder": "the person"}
    - action_update_stakeholder
    - slot{"decider": "Werner"}
    - slot{"name": "Werner"}
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_ask_options
* option
    - action_create_option
    - slot{"deed": null}
    - slot{"option": 5}
    - slot{"action_return": true}
    - utter_ask_deed
* deed{"deed": "letting the child"}
    - slot{"deed": "letting the child"}
    - action_create_deed
    - slot{"action_return": true}
    - utter_ask_universalizable
* wrong
    - action_update_deed
    - slot{"action_return": true}
    - utter_ask_inherent_evil
* affirm
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deed{"deed": "saving"}
    - slot{"deed": "saving"}
    - action_create_deed
    - slot{"action_return": true}
    - utter_ask_universalizable
* correct
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deny
    - utter_ask_consequences
* consequence
    - action_create_consequence
    - slot{"name": null}
    - slot{"action_return": false}
    - action_choose_affected_stakeholder
* consequence{"name": "the child"}
    - slot{"name": "the child"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact
* negative
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_impact_weight
* quantity{"quantity": "10"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* correct
    - utter_next_consequence
* consequence
    - action_create_consequence
    - slot{"name": null}
    - slot{"action_return": false}
    - action_choose_affected_stakeholder
* consequence{"name": "Uwe"}
    - slot{"name": "Uwe"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact
* positive
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_impact_weight
* quantity{"quantity": "10"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* wrong
    - utter_ask_consequence_probability
* dontknow
    - utter_ask_guess_quantity
* quantity{"quantity": "80"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* deny
    - utter_next_option
* option
    - action_create_option
    - slot{"deed": null}
    - slot{"option": 10}
    - slot{"action_return": true}
    - utter_ask_deed
* deed{"deed": "protecting"}
    - slot{"deed": "protecting"}
    - action_create_deed
    - slot{"action_return": true}
    - utter_ask_universalizable
* correct
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deny
    - utter_ask_consequences
* consequence{"sentiment": "pos"}
    - slot{"sentiment": "pos"}
    - action_create_consequence
    - slot{"name": null}
    - slot{"action_return": false}
    - action_choose_affected_stakeholder
* consequence{"name": "the child"}
    - slot{"name": "the child"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_positive
* correct
    - utter_ask_impact_weight
* quantity{"quantity": "5"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* correct
    - utter_next_consequence
* consequence{"sentiment": "pos"}
    - slot{"sentiment": "pos"}
    - action_create_consequence
    - slot{"name": null}
    - slot{"action_return": false}
    - action_choose_affected_stakeholder
* consequence{"name": "Uwe"}
    - slot{"name": "Uwe"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_positive
* wrong
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_impact_weight
* quantity{"quantity": "1"}
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
    - slot{"image": "url"}
    - utter_report_image
    - utter_next_method
* affirm
    - utter_ask_method
* deontology
    - utter_starting_evaluation_1
    - utter_starting_evaluation_2
    - action_evaluation_deontology
    - slot{"action_return": true}
    - slot{"image": "url"}
    - utter_report_image
    - utter_next_method
* deny
    - utter_goodbye

## Generated Story -369197456957833744
* greeting
    - action_intro
* stakeholder{"stakeholder": "one person", "moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - utter_ask_name_singular
* dontknow
    - action_update_stakeholder
    - slot{"name": "Greta"}
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholdergroup{"quantity": "150", "moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": true}
    - utter_ask_quantity
* quantity{"quantity": "150"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_ask_name_plural
* name
    - action_update_stakeholder
    - slot{"name": "the Palatines"}
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholdergroup{"stakeholder": "a lot of people", "moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": false}
    - utter_ask_quantity
* dontknow
    - utter_ask_guess_quantity
* quantity{"quantity": "200"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_ask_name_plural
* deny
    - action_update_stakeholder
    - slot{"name": "the Swabians"}
    - slot{"action_return": true}
    - utter_next_stakeholder
* deny
    - utter_confirm_stakeholders
    - action_choose_decider
* decider{"name": "Greta"}
    - slot{"name": "Greta"}
    - action_update_stakeholder
    - slot{"decider": "Greta"}
    - slot{"action_return": true}
    - utter_ask_options
* option{"deed": "kill the attackers"}
    - slot{"deed": "kill the attackers"}
    - action_create_option
    - slot{"deed": "kill the attackers"}
    - slot{"option": 4}
    - slot{"action_return": true}
    - utter_ask_identified_deed
* correct
    - action_create_deed
    - slot{"action_return": true}
    - utter_ask_universalizable
* wrong
    - action_update_deed
    - slot{"action_return": true}
    - utter_ask_inherent_evil
* affirm
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deed
    - action_create_deed
    - slot{"deed": "Saving people on the ground who are possibly threatened can be considered a moral action"}
    - slot{"action_return": true}
    - utter_ask_universalizable
* correct
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deny
    - utter_ask_consequences
* consequence{"name": "the Palatines", "sentiment": "neg"}
    - slot{"name": "the Palatines"}
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
* quantity{"quantity": "90"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* deny
    - utter_next_option
* option
    - action_create_option
    - slot{"deed": null}
    - slot{"option": 8}
    - slot{"action_return": true}
    - utter_ask_deed
* deny
    - utter_ask_consequences
* consequence
    - action_create_consequence
    - slot{"name": null}
    - slot{"action_return": false}
    - action_choose_affected_stakeholder
* consequence{"name": "the Swabians"}
    - slot{"name": "the Swabians"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact
* negative
    - action_update_consequence
    - slot{"action_return": false}
    - utter_ask_impact_weight
* quantity{"quantity": "10"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* wrong
    - utter_ask_consequence_probability
* quantity{"quantity": "50"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* consequence{"name": "the Palatines", "sentiment": "neg"}
    - slot{"name": "the Palatines"}
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
* dontknow
    - utter_ask_guess_quantity
* quantity{"quantity": "75"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* deny
    - utter_next_option
* deny
    - utter_got_everything
    - utter_ask_method

## Generated Story 6080478534332002306
* greeting
    - action_intro
* stakeholder{"name": "tom"}
    - slot{"name": "tom"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": false}
    - action_check_identified_name
    - slot{"action_return": false}
    - utter_ask_identified_name
* correct
    - action_update_stakeholder
    - slot{"name": "tom"}
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"stakeholder": "tom's wife"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": true}
    - utter_ask_name_singular
* name{"name": "tom"}
    - slot{"name": "tom"}
    - action_update_stakeholder
    - slot{"name": "tom"}
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* deny
    - utter_confirm_stakeholders
    - action_choose_decider

## Generated Story -6408575720604844768
* greeting
    - action_intro
* stakeholder{"name": "jane"}
    - slot{"name": "jane"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - action_check_identified_name
    - slot{"action_return": false}
    - utter_ask_identified_name
* correct
    - action_update_stakeholder
    - slot{"name": "jane"}
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"name": "jane"}
    - slot{"name": "jane"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": true}
    - action_check_identified_name
    - slot{"action_return": true}
    - utter_ask_name_singular
* name{"name": "jane"}
    - slot{"name": "jane"}
    - action_update_stakeholder
    - slot{"name": "jane"}
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* deny
    - utter_confirm_stakeholders
    - action_choose_decider
* decider{"name": "jane"}
    - slot{"name": "jane"}
    - action_update_stakeholder
    - slot{"decider": "jane"}
    - slot{"action_return": true}
    - utter_ask_options
* option{"deed": "hand over the antidote"}
    - slot{"deed": "hand over the antidote"}
    - action_create_option
    - slot{"deed": "hand over the antidote"}
    - slot{"option": 3}
    - slot{"action_return": true}
    - utter_ask_identified_deed
* correct
    - action_create_deed
    - slot{"action_return": true}
    - utter_ask_universalizable
* wrong
    - action_update_deed
    - slot{"action_return": true}
    - utter_ask_inherent_evil
* deny
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* dontknow
    - utter_ask_consequences
* consequence{"sentiment": "pos"}
    - slot{"sentiment": "pos"}
    - action_create_consequence
    - slot{"name": null}
    - slot{"action_return": false}
    - action_choose_affected_stakeholder
* consequence{"name": "jane"}
    - slot{"name": "jane"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_positive
* correct
    - utter_ask_impact_weight
* quantity{"quantity": "8"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* correct
    - utter_next_consequence
* consequence{"name": "jane", "sentiment": "neu"}
    - slot{"name": "jane"}
    - slot{"sentiment": "neu"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact
* negative
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_impact_weight
* quantity{"quantity": "2"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* correct
    - utter_next_consequence
* deny
    - utter_next_option
* option{"deed": "refuse to give the antidote"}
    - slot{"deed": "refuse to give the antidote"}
    - action_create_option
    - slot{"deed": "refuse to give the antidote"}
    - slot{"option": 7}
    - slot{"action_return": true}
    - utter_ask_identified_deed
* correct
    - action_create_deed
    - slot{"action_return": true}
    - utter_ask_universalizable
* wrong
    - action_update_deed
    - slot{"action_return": true}
    - utter_ask_inherent_evil
* affirm
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deny
    - utter_ask_consequences
* consequence{"name": "jane"}
    - slot{"name": "jane"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact
* negative
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_impact_weight
* quantity{"quantity": "10"}
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
    - slot{"image": "url"}
    - utter_report_image
    - utter_next_method
* affirm
    - utter_ask_method
* deontology
    - utter_starting_evaluation_1
    - utter_starting_evaluation_2
    - action_evaluation_deontology
    - slot{"action_return": true}
    - slot{"image": "url"}
    - utter_report_image
    - utter_next_method

## Generated Story -4965336235294374691
* greeting
    - action_intro
* stakeholder
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - utter_ask_name_singular
* name
    - action_update_stakeholder
    - slot{"name": "Yves"}
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholdergroup{"stakeholder": "five patients"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": true}
    - utter_ask_name_plural
* name{"stakeholder": "the patients"}
    - action_update_stakeholder
    - slot{"name": "the patients"}
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"stakeholder": "a"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": true}
    - utter_ask_name_singular
* dontknow
    - action_update_stakeholder
    - slot{"name": "Glenn"}
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* deny
    - utter_confirm_stakeholders
    - action_choose_decider
* /decider
    - action_update_stakeholder
    - slot{"action_return": false}
    - utter_ask_options
* option{"quantity": "5"}
    - action_create_option
    - slot{"deed": null}
    - slot{"option": 4}
    - slot{"action_return": true}
    - utter_ask_deed
* deed{"deed": "letting glenn die"}
    - slot{"deed": "letting glenn die"}
    - action_create_deed
    - slot{"action_return": true}
    - utter_ask_universalizable
* wrong
    - action_update_deed
    - slot{"action_return": true}
    - utter_ask_inherent_evil
* affirm
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deed{"deed": "saving the lives", "quantity": "5"}
    - slot{"deed": "saving the lives"}
    - action_create_deed
    - slot{"action_return": true}
    - utter_ask_universalizable
* correct
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deny
    - utter_ask_consequences
* consequence{"sentiment": "pos"}
    - slot{"sentiment": "pos"}
    - action_create_consequence
    - slot{"name": null}
    - slot{"action_return": false}
    - action_choose_affected_stakeholder
* consequence{"name": "the patients"}
    - slot{"name": "the patients"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_positive
* correct
    - utter_ask_impact_weight
* quantity{"quantity": "8"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* correct
    - utter_next_consequence
* consequence{"sentiment": "neg"}
    - slot{"sentiment": "neg"}
    - action_create_consequence
    - slot{"name": null}
    - slot{"action_return": false}
    - action_choose_affected_stakeholder
* consequence{"name": "Glenn"}
    - slot{"name": "Glenn"}
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
* option
    - action_create_option
    - slot{"deed": null}
    - slot{"option": 9}
    - slot{"action_return": true}
    - utter_ask_deed
* dontknow
    - utter_ask_consequences
* consequence{"sentiment": "neu"}
    - slot{"sentiment": "neu"}
    - action_create_consequence
    - slot{"name": null}
    - slot{"action_return": false}
    - action_choose_affected_stakeholder
* consequence{"name": "Glenn"}
    - slot{"name": "Glenn"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact
* neutral
    - utter_next_consequence
* consequence{"stakeholder": "the patients", "sentiment": "neg"}
    - slot{"sentiment": "neg"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_negative
* correct
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
