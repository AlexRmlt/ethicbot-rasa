## Generated Story 4250896942926339107
* greeting
    - action_intro
* stakeholder{"stakeholder": "five workmen", "CARDINAL": "5", "plural": "specific_plural", "moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - slot{"plural": "specific_plural"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - utter_ask_name_plural
* deny
    - action_update_stakeholder
    - slot{"PERSON": "the Palatines"}
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"PERSON": "Molly", "CARDINAL": "5", "plural": "singular", "moralstatus": "human"}
    - slot{"PERSON": "Molly"}
    - slot{"moralstatus": "human"}
    - slot{"plural": "singular"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": true}
    - utter_ask_identified_name
* correct
    - action_update_stakeholder
    - slot{"PERSON": "Molly"}
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"ORG": "Molly", "plural": "singular"}
    - slot{"plural": "singular"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": true}
    - utter_ask_identified_name
* wrong
    - action_update_stakeholder
    - slot{"PERSON": "Nathan"}
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
* consequence{"stakeholder": "the five workmen", "CARDINAL": "5", "sentiment": "neg"}
    - slot{"sentiment": "neg"}
    - action_create_consequence
    - slot{"PERSON": null}
    - slot{"action_return": false}
    - action_choose_affected_stakeholder
* consequence{"PERSON": "the Palatines"}
    - slot{"PERSON": "the Palatines"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_negative
* correct
    - action_update_consequence
    - slot{"action_return": false}
    - utter_ask_impact_weight
* quantity{"CARDINAL": "10"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* correct
    - utter_next_consequence
* consequence{"PERSON": "Nathan"}
    - slot{"PERSON": "Nathan"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_negative
* wrong
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_impact_weight
* quantity{"CARDINAL": "8"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* correct
    - utter_next_consequence
* deny
    - utter_next_option
* option{"ORG": "Molly", "LAW": "Nathan off the"}
    - action_create_option
    - slot{"deed": null}
    - slot{"option": 8}
    - slot{"action_return": true}
    - utter_ask_deed
* deed{"ORG": "Killing Nathan"}
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
* deed{"deed": "saving the lives", "CARDINAL": "5"}
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
* consequence{"PERSON": "Nathan", "ORG": "Nathan", "sentiment": "neg"}
    - slot{"PERSON": "Nathan"}
    - slot{"sentiment": "neg"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_negative
* correct
    - utter_ask_impact_weight
* quantity{"CARDINAL": "10"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* correct
    - utter_next_consequence
* consequence{"ORG": "Palatines", "sentiment": "pos"}
    - slot{"sentiment": "pos"}
    - action_create_consequence
    - slot{"PERSON": null}
    - slot{"action_return": false}
    - action_choose_affected_stakeholder
* consequence{"PERSON": "the Palatines"}
    - slot{"PERSON": "the Palatines"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_positive
* correct
    - utter_ask_impact_weight
* quantity{"CARDINAL": "9"}
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
    - action_evaluation_utilitarism
    - utter_next_method
* affirm
    - utter_ask_method
* deontology
    - action_evaluation_deontology
    - utter_next_method
* deny
    - utter_goodbye

## Generated Story 7358352807131470407
* greeting
    - action_intro
* stakeholder{"ORDINAL": "First", "PERSON": "Ken", "plural": "singular"}
    - slot{"PERSON": "Ken"}
    - slot{"plural": "singular"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - utter_ask_identified_name
* correct
    - action_update_stakeholder
    - slot{"PERSON": "Ken"}
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"stakeholder": "a patient", "PERSON": "Ken", "NORP": " ", "plural": "unspecific_plural", "moralstatus": "human"}
    - slot{"PERSON": "Ken"}
    - slot{"moralstatus": "human"}
    - slot{"plural": "unspecific_plural"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": false}
    - utter_ask_quantity
* quantity{"CARDINAL": "only one"}
    - action_update_stakeholder
    - slot{"plural": "singular"}
    - slot{"action_return": true}
    - utter_ask_identified_name
* wrong
    - action_update_stakeholder
    - slot{"PERSON": "Inga"}
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"GPE": "Inga", "plural": "unspecific_plural", "moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - slot{"plural": "unspecific_plural"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": false}
    - utter_ask_quantity
* dontknow
    - utter_ask_guess_quantity
* quantity
    - action_update_stakeholder
    - slot{"plural": "specific_plural"}
    - slot{"action_return": true}
    - utter_ask_name_plural
* name
    - action_update_stakeholder
    - slot{"PERSON": "Inga"}
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
* option{"PERSON": "Ken"}
    - slot{"PERSON": "Ken"}
    - action_create_option
    - slot{"deed": null}
    - slot{"option": 4}
    - slot{"action_return": true}
    - utter_ask_deed
* deed{"PERSON": "Inga"}
    - slot{"PERSON": "Inga"}
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
* consequence{"PERSON": "Inga"}
    - slot{"PERSON": "Inga"}
    - action_create_consequence
    - slot{"action_return": false}
    - utter_ask_impact
* negative{"ORG": "Propably"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_impact_weight
* quantity{"CARDINAL": "ten"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* correct
    - utter_next_consequence
* consequence{"PERSON": "the saxons", "ORG": "Saxons", "sentiment": "neu"}
    - slot{"PERSON": "the saxons"}
    - slot{"sentiment": "neu"}
    - action_create_consequence
    - slot{"action_return": false}
    - utter_ask_impact
* positive
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_impact_weight
* quantity{"CARDINAL": "7"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* correct
    - utter_next_consequence
* deny
    - utter_next_option
* option{"PERSON": "Inga"}
    - slot{"PERSON": "Inga"}
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
* consequence{"PERSON": "the saxons", "ORG": "Saxons", "sentiment": "neg"}
    - slot{"PERSON": "the saxons"}
    - slot{"sentiment": "neg"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_negative
* correct
    - utter_ask_impact_weight
* quantity{"CARDINAL": "8"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* wrong
    - utter_ask_consequence_probability
* quantity{"PERCENT": "80 percent"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* consequence{"GPE": "Inga", "sentiment": "neu"}
    - slot{"sentiment": "neu"}
    - action_create_consequence
    - slot{"PERSON": null}
    - slot{"action_return": false}
    - action_choose_affected_stakeholder
* consequence{"PERSON": "Inga"}
    - slot{"PERSON": "Inga"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact
* positive
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_impact_weight
* quantity{"CARDINAL": "9"}
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
    - action_evaluation_deontology
    - utter_next_method
* affirm
    - utter_ask_method
* utilitarism
    - action_evaluation_utilitarism
    - utter_next_method
* deny
    - utter_goodbye

## Generated Story -6025756364314501582
* greeting
    - action_intro
* stakeholder{"PERSON": "Tom", "plural": "unspecific_plural"}
    - slot{"PERSON": "Tom"}
    - slot{"plural": "unspecific_plural"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": false}
    - utter_ask_quantity
* quantity{"CARDINAL": "only one"}
    - action_update_stakeholder
    - slot{"plural": "singular"}
    - slot{"action_return": true}
    - utter_ask_identified_name
* correct
    - action_update_stakeholder
    - slot{"PERSON": "Patrick"}
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"CARDINAL": "8", "plural": "unspecific_plural", "moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - slot{"plural": "unspecific_plural"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": true}
    - utter_ask_quantity
* quantity{"CARDINAL": "8"}
    - action_update_stakeholder
    - slot{"plural": "specific_plural"}
    - slot{"action_return": true}
    - utter_ask_name_plural
* name{"CARDINAL": "eight"}
    - action_update_stakeholder
    - slot{"PERSON": "the Rhinelanders"}
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"plural": "unspecific_plural"}
    - slot{"plural": "unspecific_plural"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": false}
    - utter_ask_quantity
* dontknow
    - utter_ask_guess_quantity
* dontknow
    - utter_too_bad
    - utter_ask_name_plural
* name
    - action_update_stakeholder
    - slot{"PERSON": "the Saxons"}
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"CARDINAL": "One", "PERSON": "Tom", "deed": "kill him", "TIME": "the following morning"}
    - slot{"PERSON": "Tom"}
    - slot{"deed": "kill him"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 4}
    - slot{"action_return": true}
    - utter_ask_quantity
* quantity{"CARDINAL": "only one"}
    - action_update_stakeholder
    - slot{"plural": "singular"}
    - slot{"action_return": true}
    - utter_ask_identified_name
* wrong
    - action_update_stakeholder
    - slot{"PERSON": "Esther"}
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"deed": "kill", "PERSON": "Tom", "plural": "singular"}
    - slot{"PERSON": "Tom"}
    - slot{"deed": "kill"}
    - slot{"plural": "singular"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 5}
    - slot{"action_return": true}
    - utter_ask_identified_name
* wrong
    - action_update_stakeholder
    - slot{"PERSON": "Amelie"}
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
* option{"deed": "kill one", "PERSON": "Tom", "CARDINAL": "one"}
    - slot{"PERSON": "Tom"}
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
* deed{"deed": "saving", "CARDINAL": "eight"}
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
* consequence{"PERSON": "Amelie", "sentiment": "neg"}
    - slot{"PERSON": "Amelie"}
    - slot{"sentiment": "neg"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_negative
* correct
    - utter_ask_impact_weight
* quantity{"CARDINAL": "10"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* correct
    - utter_next_consequence
* consequence{"PERSON": "Tom", "CARDINAL": "eight", "sentiment": "pos"}
    - slot{"PERSON": "Tom"}
    - slot{"sentiment": "pos"}
    - action_create_consequence
    - slot{"PERSON": null}
    - slot{"action_return": false}
    - action_choose_affected_stakeholder
* consequence{"PERSON": "the Rhinelanders"}
    - slot{"PERSON": "the Rhinelanders"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_positive
* correct
    - utter_ask_impact_weight
* quantity{"CARDINAL": "9"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* correct
    - utter_next_consequence
* consequence{"PERSON": "the saxons", "ORG": "Saxons", "sentiment": "neg"}
    - slot{"PERSON": "the saxons"}
    - slot{"sentiment": "neg"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_negative
* correct
    - utter_ask_impact_weight
* quantity{"CARDINAL": "10"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* correct
    - utter_next_consequence
* deny
    - utter_next_option
* option{"deed": "kill one", "CARDINAL": "one"}
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
* consequence{"PERSON": "the saxons", "ORG": "Saxons", "sentiment": "neg"}
    - slot{"PERSON": "the saxons"}
    - slot{"sentiment": "neg"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_negative
* correct
    - utter_ask_impact_weight
* quantity{"CARDINAL": "10"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* correct
    - utter_next_consequence
* consequence{"PERSON": "Patrick", "ORG": "Patrick", "sentiment": "neg"}
    - slot{"PERSON": "Patrick"}
    - slot{"sentiment": "neg"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_negative
* correct
    - utter_ask_impact_weight
* quantity{"CARDINAL": "10"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* correct
    - utter_next_consequence
* consequence{"PERSON": "the Rhinelanders", "sentiment": "neg"}
    - slot{"PERSON": "the Rhinelanders"}
    - slot{"sentiment": "neg"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_negative
* correct
    - utter_ask_impact_weight
* quantity{"CARDINAL": "10"}
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
    - action_evaluation_utilitarism
    - utter_next_method
* affirm
    - utter_ask_method
* deontology
    - action_evaluation_deontology
    - utter_next_method
* deny
    - utter_goodbye

## Generated Story -5384821882511551639
* greeting
    - action_intro
* stakeholder{"PERSON": "Mary", "plural": "singular"}
    - slot{"PERSON": "Mary"}
    - slot{"plural": "singular"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - utter_ask_identified_name
* correct
    - action_update_stakeholder
    - slot{"PERSON": "Mary"}
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"stakeholder": "a", "PERSON": "Mary", "TIME": "midnight", "plural": "singular", "moralstatus": "human"}
    - slot{"PERSON": "Mary"}
    - slot{"moralstatus": "human"}
    - slot{"plural": "singular"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": true}
    - utter_ask_identified_name
* wrong
    - action_update_stakeholder
    - slot{"PERSON": "Samuel"}
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"PERSON": "Samuels", "plural": "singular"}
    - slot{"PERSON": "Samuels"}
    - slot{"plural": "singular"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": true}
    - utter_ask_identified_name
* wrong
    - action_update_stakeholder
    - slot{"PERSON": "Greta"}
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"CARDINAL": "7", "ORG": "Samuels", "DATE": "the next 7 days", "plural": "singular"}
    - slot{"plural": "singular"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 4}
    - slot{"action_return": true}
    - utter_ask_name_singular
* name
    - action_update_stakeholder
    - slot{"PERSON": "Amelie"}
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
* option{"PERSON": "samuel"}
    - slot{"PERSON": "samuel"}
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
* deed{"PERSON": "Samuels"}
    - slot{"PERSON": "Samuels"}
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
* consequence{"PERSON": "Amelie", "sentiment": "neg"}
    - slot{"PERSON": "Amelie"}
    - slot{"sentiment": "neg"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_negative
* correct
    - utter_ask_impact_weight
* quantity{"CARDINAL": "1"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* correct
    - utter_next_consequence
* consequence{"PERSON": "greta", "DATE": "Greta"}
    - slot{"PERSON": "greta"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_negative
* wrong
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_impact_weight
* quantity{"CARDINAL": "7"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* wrong
    - utter_ask_consequence_probability
* quantity{"PERCENT": "90%"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* consequence{"PERSON": "samuel"}
    - slot{"PERSON": "samuel"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_negative
* wrong
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_impact_weight
* quantity{"CARDINAL": "5"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* wrong
    - utter_ask_consequence_probability
* quantity{"PERCENT": "80%"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* deny
    - utter_next_option
* option{"deed": "refrain from killing", "PERSON": "samuel"}
    - slot{"PERSON": "samuel"}
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
* consequence{"PERSON": "Amelie", "sentiment": "neu"}
    - slot{"PERSON": "Amelie"}
    - slot{"sentiment": "neu"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact
* positive
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_impact_weight
* quantity{"CARDINAL": "2"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* wrong
    - utter_ask_consequence_probability
* quantity{"CARDINAL": "75"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* consequence{"PERSON": "samuel"}
    - slot{"PERSON": "samuel"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact
* negative
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_impact_weight
* quantity{"CARDINAL": "6"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* correct
    - utter_next_consequence
* consequence{"PERSON": "greta", "DATE": "Greta", "sentiment": "neu"}
    - slot{"PERSON": "greta"}
    - slot{"sentiment": "neu"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact
* negative
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_impact_weight
* quantity{"CARDINAL": "6"}
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
    - action_evaluation_utilitarism
    - utter_next_method
* affirm
    - utter_ask_method
* deontology
    - action_evaluation_deontology
    - utter_next_method
* deny
    - utter_goodbye

