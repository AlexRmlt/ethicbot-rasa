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
* decider{"PERSON": "Molly"}
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
* decider{"PERSON": "Ken"}
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
* decider{"PERSON": "Patrick"}
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
* decider{"PERSON": "Mary"}
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

## Generated Story 3846139624378699522
* greeting
    - action_intro
* stakeholder{"stakeholder": "the first person", "ORDINAL": "first", "PERSON": "Jane", "CARDINAL": "two", "plural": "unspecific_plural", "moralstatus": "human"}
    - slot{"PERSON": "Jane"}
    - slot{"moralstatus": "human"}
    - slot{"plural": "unspecific_plural"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - utter_ask_quantity
* quantity{"CARDINAL": "only one"}
    - action_update_stakeholder
    - slot{"plural": "singular"}
    - slot{"action_return": true}
    - utter_ask_identified_name
* correct
    - action_update_stakeholder
    - slot{"PERSON": "Jane"}
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"stakeholder": "a group of other people", "plural": "unspecific_plural", "moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - slot{"plural": "unspecific_plural"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": false}
    - utter_ask_quantity
* dontknow
    - utter_ask_guess_quantity
* quantity{"CARDINAL": "10"}
    - action_update_stakeholder
    - slot{"plural": "specific_plural"}
    - slot{"action_return": true}
    - utter_ask_name_plural
* name
    - action_update_stakeholder
    - slot{"PERSON": "the Swabians"}
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"PERSON": "Jane", "ORDINAL": "second", "plural": "singular"}
    - slot{"PERSON": "Jane"}
    - slot{"plural": "singular"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 3}
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
* stakeholder{"DATE": "the age of two", "plural": "unspecific_plural"}
    - slot{"plural": "unspecific_plural"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 4}
    - slot{"action_return": false}
    - utter_ask_quantity
* quantity{"CARDINAL": "about 5"}
    - action_update_stakeholder
    - slot{"plural": "specific_plural"}
    - slot{"action_return": true}
    - utter_ask_name_plural
* name
    - action_update_stakeholder
    - slot{"PERSON": "the Bavarians"}
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
* decider{"PERSON": "Jane"}
    - action_update_stakeholder
    - slot{"decider": "Jane"}
    - slot{"action_return": true}
    - utter_ask_options
* option{"PERSON": "Jane"}
    - slot{"PERSON": "Jane"}
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
* wrong
    - utter_ask_consequence_probability
* quantity{"PERCENT": "90 percent"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* consequence{"PERSON": "the swabians", "NORP": "Swabians", "sentiment": "neg"}
    - slot{"PERSON": "the swabians"}
    - slot{"sentiment": "neg"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_negative
* correct
    - utter_ask_impact_weight
* quantity{"CARDINAL": "Only 2"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* correct
    - utter_next_consequence
* consequence{"PERSON": "Jane", "sentiment": "neg"}
    - slot{"PERSON": "Jane"}
    - slot{"sentiment": "neg"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_negative
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
* consequence{"PERSON": "the swabians", "NORP": "Swabians", "sentiment": "neg"}
    - slot{"PERSON": "the swabians"}
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
* consequence{"PERSON": "Amelie", "DATE": "less than 2 years old", "CARDINAL": "2"}
    - slot{"PERSON": "Amelie"}
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
* consequence{"PERSON": "Jane", "sentiment": "neg"}
    - slot{"PERSON": "Jane"}
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
    
## Generated Story 1277434377440136980
* greeting
    - action_intro
* stakeholder{"PERSON": "mark", "stakeholder": "a crewperson", "ORG": "Mark", "plural": "singular", "moralstatus": "human"}
    - slot{"PERSON": "mark"}
    - slot{"moralstatus": "human"}
    - slot{"plural": "singular"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - utter_ask_identified_name
* correct
    - action_update_stakeholder
    - slot{"PERSON": "mark"}
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"stakeholder": "a group", "plural": "unspecific_plural"}
    - slot{"plural": "unspecific_plural"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": false}
    - utter_ask_quantity
* quantity{"CARDINAL": "6"}
    - action_update_stakeholder
    - slot{"plural": "specific_plural"}
    - slot{"action_return": true}
    - utter_ask_name_plural
* name
    - action_update_stakeholder
    - slot{"PERSON": "the Palatines"}
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"CARDINAL": "One", "plural": "singular"}
    - slot{"plural": "singular"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": true}
    - utter_ask_name_singular
* name
    - action_update_stakeholder
    - slot{"PERSON": "J\u00f6rg"}
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
* decider{"PERSON": "mark"}
    - action_update_stakeholder
    - slot{"decider": "mark"}
    - slot{"action_return": true}
    - utter_ask_options
* option{"PERSON": "mark"}
    - slot{"PERSON": "mark"}
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
* deed{"PERSON": "J\u00f6rg"}
    - slot{"PERSON": "J\u00f6rg"}
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
* consequence{"PERSON": "J\u00f6rg", "sentiment": "neg"}
    - slot{"PERSON": "J\u00f6rg"}
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
* consequence{"ORG": "Palatines", "sentiment": "neu"}
    - slot{"sentiment": "neu"}
    - action_create_consequence
    - slot{"PERSON": null}
    - slot{"action_return": false}
    - action_choose_affected_stakeholder
* consequence{"PERSON": "the Palatines"}
    - slot{"PERSON": "the Palatines"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact
* positive
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_impact_weight
* quantity{"CARDINAL": "8"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* correct
    - utter_next_consequence
* consequence{"PERSON": "mark", "ORG": "Mark", "sentiment": "neu"}
    - slot{"PERSON": "mark"}
    - slot{"sentiment": "neu"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact
* positive
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
* option{"PERSON": "J\u00f6rg", "deed": "refrain from", "ORG": "Mark"}
    - slot{"PERSON": "J\u00f6rg"}
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
* consequence{"PERSON": "J\u00f6rg", "sentiment": "neu"}
    - slot{"PERSON": "J\u00f6rg"}
    - slot{"sentiment": "neu"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact
* positive{"PERSON": "J\u00f6rg"}
    - slot{"PERSON": "J\u00f6rg"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_impact_weight
* quantity{"CARDINAL": "7"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* wrong
    - utter_ask_consequence_probability
* quantity{"PERCENT": "most 80%"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* consequence{"ORG": "Palatines", "sentiment": "neg"}
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
    - utter_ask_impact_weight
* quantity{"CARDINAL": "10"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* correct
    - utter_next_consequence
* consequence{"PERSON": "mark", "ORG": "Mark", "sentiment": "pos"}
    - slot{"PERSON": "mark"}
    - slot{"sentiment": "pos"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_positive
* wrong
    - action_update_consequence
    - slot{"action_return": true}
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
    
## Generated Story 5601750309873569494
* greeting
    - action_intro
* stakeholder{"CARDINAL": "5", "plural": "unspecific_plural", "moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - slot{"plural": "unspecific_plural"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": true}
    - utter_ask_quantity
* quantity{"CARDINAL": "5"}
    - action_update_stakeholder
    - slot{"plural": "specific_plural"}
    - slot{"action_return": true}
    - utter_ask_name_plural
* name
    - action_update_stakeholder
    - slot{"PERSON": "the Swabians"}
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"PERSON": "molly", "ORG": "Molly", "CARDINAL": "5", "plural": "unspecific_plural", "moralstatus": "human"}
    - slot{"PERSON": "molly"}
    - slot{"moralstatus": "human"}
    - slot{"plural": "unspecific_plural"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": true}
    - utter_ask_quantity
* quantity{"CARDINAL": "only one"}
    - action_update_stakeholder
    - slot{"plural": "singular"}
    - slot{"action_return": true}
    - utter_ask_identified_name
* correct
    - action_update_stakeholder
    - slot{"PERSON": "molly"}
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"plural": "singular"}
    - slot{"plural": "singular"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 4}
    - slot{"action_return": true}
    - utter_ask_name_singular
* deny
    - action_update_stakeholder
    - slot{"PERSON": "Tanja"}
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
* stakeholder{"CARDINAL": "5", "plural": "unspecific_plural", "moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - slot{"plural": "unspecific_plural"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - utter_ask_quantity
* quantity{"stakeholder": "five persons", "CARDINAL": "5"}
    - action_update_stakeholder
    - slot{"plural": "specific_plural"}
    - slot{"action_return": true}
    - utter_ask_name_plural
* name
    - action_update_stakeholder
    - slot{"PERSON": "the Palatines"}
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"PERSON": "molly", "ORG": "Molly", "plural": "singular"}
    - slot{"PERSON": "molly"}
    - slot{"plural": "singular"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": true}
    - utter_ask_identified_name
* correct
    - action_update_stakeholder
    - slot{"PERSON": "molly"}
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"plural": "singular"}
    - slot{"plural": "singular"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": true}
    - utter_ask_name_singular
* deny
    - action_update_stakeholder
    - slot{"PERSON": "Katharina"}
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
* decider{"PERSON": "molly"}
    - action_update_stakeholder
    - slot{"decider": "molly"}
    - slot{"action_return": true}
    - utter_ask_options
* option{"ORG": "Katharina"}
    - action_create_option
    - slot{"deed": null}
    - slot{"option": 4}
    - slot{"action_return": true}
    - utter_ask_deed
* deed{"LOC": "Katharina"}
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
* consequence{"ORG": "Katharina", "sentiment": "neg"}
    - slot{"sentiment": "neg"}
    - action_create_consequence
    - slot{"PERSON": null}
    - slot{"action_return": false}
    - action_choose_affected_stakeholder
* consequence{"PERSON": "Katharina"}
    - slot{"PERSON": "Katharina"}
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
* consequence{"ORG": "Palatines", "sentiment": "neu"}
    - slot{"sentiment": "neu"}
    - action_create_consequence
    - slot{"PERSON": null}
    - slot{"action_return": false}
    - action_choose_affected_stakeholder
* consequence{"PERSON": "the Palatines"}
    - slot{"PERSON": "the Palatines"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact
* positive
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
* option{"deed": "refrain from pushing", "LOC": "Katharina"}
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
* consequence{"ORG": "Palatines", "sentiment": "neg"}
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
    - utter_ask_impact_weight
* quantity{"CARDINAL": "10"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* correct
    - utter_next_consequence
* consequence{"ORG": "Katharina", "sentiment": "neu"}
    - slot{"sentiment": "neu"}
    - action_create_consequence
    - slot{"PERSON": null}
    - slot{"action_return": false}
    - action_choose_affected_stakeholder
* consequence{"PERSON": "Katharina"}
    - slot{"PERSON": "Katharina"}
    - action_create_consequence
    - slot{"action_return": true}
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

## Generated Story 5900225719431929188
* greeting
    - action_intro
* stakeholder{"PERSON": "heather", "ORG": "Heather", "CARDINAL": "four", "plural": "singular", "moralstatus": "human"}
    - slot{"PERSON": "heather"}
    - slot{"moralstatus": "human"}
    - slot{"plural": "singular"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - utter_ask_identified_name
* correct
    - action_update_stakeholder
    - slot{"PERSON": "heather"}
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"CARDINAL": "two", "plural": "singular"}
    - slot{"plural": "singular"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": true}
    - utter_ask_name_singular
* dontknow
    - action_update_stakeholder
    - slot{"PERSON": "Zoe"}
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"CARDINAL": "One", "plural": "singular"}
    - slot{"plural": "singular"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": true}
    - utter_ask_name_singular
* name{"PERSON": "Herbert"}
    - slot{"PERSON": "Herbert"}
    - action_update_stakeholder
    - slot{"PERSON": "Herbert"}
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
* decider{"PERSON": "heather"}
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
* consequence{"PERSON": "Herbert", "sentiment": "neg"}
    - slot{"PERSON": "Herbert"}
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
* consequence{"PERSON": "zoe", "sentiment": "neu"}
    - slot{"PERSON": "zoe"}
    - slot{"sentiment": "neu"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact
* positive
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_impact_weight
* quantity{"CARDINAL": "6"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* correct
    - utter_next_consequence
* consequence{"PERSON": "heather", "ORG": "Heather", "sentiment": "neu"}
    - slot{"PERSON": "heather"}
    - slot{"sentiment": "neu"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact
* positive
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
* option{"ORG": "Heather", "PERSON": "Herbert"}
    - slot{"PERSON": "Herbert"}
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
* consequence{"PERSON": "Herbert", "sentiment": "neu"}
    - slot{"PERSON": "Herbert"}
    - slot{"sentiment": "neu"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact
* positive
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_impact_weight
* quantity{"CARDINAL": "6"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* correct
    - utter_next_consequence
* consequence{"PERSON": "heather", "ORG": "Heather", "sentiment": "neg"}
    - slot{"PERSON": "heather"}
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

## Generated Story -5279776952862841305
* greeting
    - action_intro
* stakeholder{"PERSON": "Doug", "plural": "singular"}
    - slot{"PERSON": "Doug"}
    - slot{"plural": "singular"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - utter_ask_identified_name
* correct
    - action_update_stakeholder
    - slot{"PERSON": "Doug"}
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"plural": "unspecific_plural", "moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - slot{"plural": "unspecific_plural"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": false}
    - utter_ask_quantity
* quantity{"CARDINAL": "About 20"}
    - action_update_stakeholder
    - slot{"plural": "specific_plural"}
    - slot{"action_return": true}
    - utter_ask_name_plural
* dontknow
    - action_update_stakeholder
    - slot{"PERSON": "the Hessians"}
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"stakeholder": "a group of old people", "PERSON": "Doug"}
    - slot{"PERSON": "Doug"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": false}
    - utter_ask_identified_name
* wrong
    - action_update_stakeholder
    - slot{"PERSON": "the Rhinelanders"}
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
* decider{"PERSON": "Doug"}
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
* wrong
    - utter_ask_consequence_probability
* quantity{"PERCENT": "90", "CARDINAL": "90"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* consequence{"NORP": "Hessians", "sentiment": "neu"}
    - slot{"sentiment": "neu"}
    - action_create_consequence
    - slot{"PERSON": null}
    - slot{"action_return": false}
    - action_choose_affected_stakeholder
* consequence{"PERSON": "the Hessians"}
    - slot{"PERSON": "the Hessians"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact
* positive
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_impact_weight
* quantity{"CARDINAL": "8"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* wrong
    - utter_ask_consequence_probability
* quantity{"PERCENT": "50%"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* consequence{"PERSON": "Doug", "sentiment": "neu"}
    - slot{"PERSON": "Doug"}
    - slot{"sentiment": "neu"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact
* positive
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_impact_weight
* quantity{"CARDINAL": "7"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* wrong
    - utter_ask_consequence_probability
* quantity{"PERCENT": "50%"}
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
* consequence{"PERSON": "the Rhinelanders", "sentiment": "neu"}
    - slot{"PERSON": "the Rhinelanders"}
    - slot{"sentiment": "neu"}
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
* wrong
    - utter_ask_consequence_probability
* quantity{"PERCENT": "30%"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* consequence{"NORP": "Hessians", "sentiment": "neg"}
    - slot{"sentiment": "neg"}
    - action_create_consequence
    - slot{"PERSON": null}
    - slot{"action_return": false}
    - action_choose_affected_stakeholder
* consequence{"PERSON": "the Hessians"}
    - slot{"PERSON": "the Hessians"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_negative
* correct
    - utter_ask_impact_weight
* quantity{"CARDINAL": "6"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* wrong
    - utter_ask_consequence_probability
* quantity{"PERCENT": "80 %"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* consequence{"PERSON": "Doug", "ORG": "Doug", "sentiment": "neg"}
    - slot{"PERSON": "Doug"}
    - slot{"sentiment": "neg"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_negative
* correct
    - utter_ask_impact_weight
* quantity{"CARDINAL": "3"}
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
* deny
    - utter_goodbye
* thanks
    - utter_thanks

## Generated Story 7321710744913522518
* greeting
    - action_intro
* stakeholder{"ORG": "Carrie", "plural": "singular"}
    - slot{"plural": "singular"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - utter_ask_name_singular
* name{"PERSON": "Carrie"}
    - slot{"PERSON": "Carrie"}
    - action_update_stakeholder
    - slot{"PERSON": "Carrie"}
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"stakeholder": "four of her patients", "deed": "kill the four", "CARDINAL": "four", "plural": "specific_plural"}
    - slot{"deed": "kill the four"}
    - slot{"plural": "specific_plural"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": true}
    - utter_ask_name_plural
* deny
    - action_update_stakeholder
    - slot{"PERSON": "the Hessians"}
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"CARDINAL": "one", "plural": "singular"}
    - slot{"plural": "singular"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": true}
    - utter_ask_name_singular
* name{"PERSON": "frank"}
    - slot{"PERSON": "frank"}
    - action_update_stakeholder
    - slot{"PERSON": "frank"}
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
* decider{"PERSON": "Carrie"}
    - action_update_stakeholder
    - slot{"decider": "Carrie"}
    - slot{"action_return": true}
    - utter_ask_options
* option{"CARDINAL": "four"}
    - action_create_option
    - slot{"deed": null}
    - slot{"option": 4}
    - slot{"action_return": true}
    - utter_ask_deed
* deed{"CARDINAL": "four"}
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
* consequence{"PERSON": "frank", "deed": "kill him", "sentiment": "neg"}
    - slot{"PERSON": "frank"}
    - slot{"deed": "kill him"}
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
* consequence{"NORP": "hessians", "sentiment": "neu"}
    - slot{"sentiment": "neu"}
    - action_create_consequence
    - slot{"PERSON": null}
    - slot{"action_return": false}
    - action_choose_affected_stakeholder
* consequence{"PERSON": "the Hessians"}
    - slot{"PERSON": "the Hessians"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact
* positive
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
* option{"deed": "do nothing", "stakeholder": "four people", "CARDINAL": "four"}
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
* consequence{"NORP": "hessians", "sentiment": "neg"}
    - slot{"sentiment": "neg"}
    - action_create_consequence
    - slot{"PERSON": null}
    - slot{"action_return": false}
    - action_choose_affected_stakeholder
* consequence{"PERSON": "the Hessians"}
    - slot{"PERSON": "the Hessians"}
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
* consequence{"PERSON": "frank", "sentiment": "neu"}
    - slot{"PERSON": "frank"}
    - slot{"sentiment": "neu"}
    - action_create_consequence
    - slot{"action_return": true}
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
* deny
    - utter_got_everything
    - utter_ask_method
* utilitarism
    - action_evaluation_utilitarism
    - utter_next_method
* deny
    - utter_goodbye
* thanks
    - utter_thanks

## Generated Story -8888859435742633065
* greeting
    - action_intro
* stakeholder{"plural": "singular"}
    - slot{"plural": "singular"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - utter_ask_name_singular
* dontknow
    - action_update_stakeholder
    - slot{"PERSON": "Inga"}
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"PERSON": "inga", "GPE": "Inga", "plural": "singular"}
    - slot{"PERSON": "inga"}
    - slot{"plural": "singular"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": true}
    - utter_ask_identified_name
* wrong
    - action_update_stakeholder
    - slot{"PERSON": "Carla"}
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"PERSON": "Carla", "GPE": "Inga", "plural": "singular"}
    - slot{"PERSON": "Carla"}
    - slot{"plural": "singular"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": true}
    - utter_ask_identified_name
* wrong
    - action_update_stakeholder
    - slot{"PERSON": "Viola"}
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
* decider{"PERSON": "Inga"}
    - slot{"PERSON": "Inga"}
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
* consequence{"PERSON": "Carla", "sentiment": "neg"}
    - slot{"PERSON": "Carla"}
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
* consequence{"PERSON": "inga", "GPE": "Inga", "sentiment": "neg"}
    - slot{"PERSON": "inga"}
    - slot{"sentiment": "neg"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_negative
* correct
    - utter_ask_impact_weight
* quantity{"CARDINAL": "9"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* correct
    - utter_next_consequence
* consequence{"sentiment": "pos"}
    - slot{"sentiment": "pos"}
    - action_create_consequence
    - slot{"PERSON": null}
    - slot{"action_return": false}
    - action_choose_affected_stakeholder
* consequence{"PERSON": "Viola"}
    - slot{"PERSON": "Viola"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_positive
* correct
    - utter_ask_impact_weight
* quantity{"CARDINAL": "7"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* correct
    - utter_next_consequence
* deny
    - utter_next_option
* option{"PERSON": "inga"}
    - slot{"PERSON": "inga"}
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
* consequence{"PERSON": "Carla", "sentiment": "neg"}
    - slot{"PERSON": "Carla"}
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
* consequence{"sentiment": "neg"}
    - slot{"sentiment": "neg"}
    - action_create_consequence
    - slot{"PERSON": null}
    - slot{"action_return": false}
    - action_choose_affected_stakeholder
* consequence{"PERSON": "Viola"}
    - slot{"PERSON": "Viola"}
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
* deontology
    - action_evaluation_deontology
    - utter_next_method
* deny
    - utter_goodbye
* thanks
    - utter_thanks

## Generated Story 7740751080933251549
* greeting
    - action_intro
* stakeholder{"plural": "singular"}
    - slot{"plural": "singular"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - utter_ask_name_singular
* dontknow
    - action_update_stakeholder
    - slot{"PERSON": "Inga"}
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"plural": "singular"}
    - slot{"plural": "singular"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": true}
    - utter_ask_name_singular
* deny
    - action_update_stakeholder
    - slot{"PERSON": "Roswitha"}
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"stakeholder": "a man", "plural": "singular", "moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - slot{"plural": "singular"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": true}
    - utter_ask_name_singular
* name
    - action_update_stakeholder
    - slot{"PERSON": "Michelle"}
    - slot{"action_return": true}
    - utter_next_stakeholder
* deny
    - utter_confirm_stakeholders
    - action_choose_decider
* decider{"PERSON": "Inga"}
    - slot{"PERSON": "Inga"}
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
* deed{"PERSON": "Ignoring Michelle"}
    - slot{"PERSON": "Ignoring Michelle"}
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
* consequence{"PERSON": "inga", "sentiment": "pos"}
    - slot{"PERSON": "inga"}
    - slot{"sentiment": "pos"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_positive
* correct
    - utter_ask_impact_weight
* quantity{"CARDINAL": "8"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* wrong
    - utter_ask_consequence_probability
* dontknow
    - utter_ask_guess_quantity
* quantity{"PERCENT": "20%"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* consequence{"PERSON": "Michelle"}
    - slot{"PERSON": "Michelle"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_positive
* wrong
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_impact_weight
* quantity{"CARDINAL": "10"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* wrong
    - utter_ask_consequence_probability
* quantity{"PERCENT": "90%"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* deny
    - utter_next_option
* option{"PERSON": "Michelle", "ORDINAL": "first"}
    - slot{"PERSON": "Michelle"}
    - action_create_option
    - slot{"deed": null}
    - slot{"option": 9}
    - slot{"action_return": true}
    - utter_ask_deed
* deed{"deed": "saving the life", "PERSON": "Michelle"}
    - slot{"PERSON": "Michelle"}
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
* consequence{"PERSON": "Roswitha", "sentiment": "neg"}
    - slot{"PERSON": "Roswitha"}
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
* consequence{"PERSON": "Michelle", "sentiment": "neg"}
    - slot{"PERSON": "Michelle"}
    - slot{"sentiment": "neg"}
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
    - action_evaluation_deontology
    - utter_next_method
* deny
    - utter_goodbye
* thanks
    - utter_thanks
    
## Generated Story 1978581040960796565
* greeting
    - action_intro
* stakeholder{"plural": "singular", "moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - slot{"plural": "singular"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - utter_ask_name_singular
* name{"PERSON": "mark"}
    - slot{"PERSON": "mark"}
    - action_update_stakeholder
    - slot{"PERSON": "mark"}
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"PERSON": "mark", "plural": "singular"}
    - slot{"PERSON": "mark"}
    - slot{"plural": "singular"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": true}
    - utter_ask_identified_name
* wrong
    - action_update_stakeholder
    - slot{"PERSON": "Viola"}
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"PERSON": "mark", "ORG": "mark", "plural": "singular"}
    - slot{"PERSON": "mark"}
    - slot{"plural": "singular"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": true}
    - utter_ask_identified_name
* wrong
    - action_update_stakeholder
    - slot{"PERSON": "Zoe"}
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
* decider{"PERSON": "mark"}
    - slot{"PERSON": "mark"}
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
* consequence{"PERSON": "mark"}
    - slot{"PERSON": "mark"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact
* negative
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_impact_weight
* quantity{"CARDINAL": "5"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* wrong
    - utter_ask_consequence_probability
* quantity{"PERCENT": "95 percent"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* consequence{"sentiment": "neu"}
    - slot{"sentiment": "neu"}
    - action_create_consequence
    - slot{"PERSON": null}
    - slot{"action_return": false}
    - action_choose_affected_stakeholder
* consequence{"PERSON": "Viola"}
    - slot{"PERSON": "Viola"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact
* negative
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_impact_weight
* quantity{"CARDINAL": "4"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* correct
    - utter_next_consequence
* consequence{"PERSON": "zoe"}
    - slot{"PERSON": "zoe"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact
* neutral
    - utter_next_consequence
* deny
    - utter_next_option
* option{"PERSON": "mark", "ORG": "mark"}
    - slot{"PERSON": "mark"}
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
    - action_evaluation_utilitarism
    - utter_next_method

## Generated Story -7493447606517739501
* greeting
    - action_intro
* stakeholder{"stakeholder": "a group of five people", "CARDINAL": "5", "plural": "specific_plural", "moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - slot{"plural": "specific_plural"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - utter_ask_name_plural
* deny
    - action_update_stakeholder
    - slot{"PERSON": "the Rhinelanders"}
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"plural": "unspecific_plural", "moralstatus": "human"}
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
    - utter_ask_name_singular
* name{"PERSON": "carla"}
    - slot{"PERSON": "carla"}
    - action_update_stakeholder
    - slot{"PERSON": "carla"}
    - slot{"action_return": true}
    - utter_next_stakeholder
* deny
    - utter_confirm_stakeholders
    - action_choose_decider
* decider{"PERSON": "the Rhinelanders"}
    - slot{"PERSON": "the Rhinelanders"}
    - action_update_stakeholder
    - slot{"decider": "the Rhinelanders"}
    - slot{"action_return": true}
    - utter_ask_options
* stakeholder{"CARDINAL": "one", "plural": "singular"}
    - slot{"plural": "singular"}
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
* consequence{"PERSON": "carla", "ORG": "carla", "sentiment": "neg"}
    - slot{"PERSON": "carla"}
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
* wrong
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
* option
    - action_create_option
    - slot{"deed": null}
    - slot{"option": 7}
    - slot{"action_return": true}
    - utter_ask_deed
* dontknow
    - utter_ask_consequences
* consequence{"PERSON": "carla", "sentiment": "neu"}
    - slot{"PERSON": "carla"}
    - slot{"sentiment": "neu"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact
* positive
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_impact_weight
* quantity{"CARDINAL": "8"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* wrong
    - utter_ask_consequence_probability
* quantity{"PERCENT": "90 %"}
    - action_update_consequence
    - slot{"action_return": true}
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

## Generated Story 599148369303593516
* greeting
    - action_intro
* stakeholder{"stakeholder": "a person", "DATE": "the weekend", "plural": "unspecific_plural", "moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - slot{"plural": "unspecific_plural"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": false}
    - utter_ask_quantity
* quantity{"CARDINAL": "one"}
    - action_update_stakeholder
    - slot{"plural": "singular"}
    - slot{"action_return": true}
    - utter_ask_name_singular
* deny
    - action_update_stakeholder
    - slot{"PERSON": "Inga"}
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"CARDINAL": "7", "DATE": "7 years old", "plural": "singular"}
    - slot{"plural": "singular"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": true}
    - utter_ask_name_singular
* dontknow
    - action_update_stakeholder
    - slot{"PERSON": "Werner"}
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"CARDINAL": "7", "DATE": "7 years old", "plural": "singular"}
    - slot{"plural": "singular"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": true}
    - utter_ask_name_singular
* dontknow
    - action_update_stakeholder
    - slot{"PERSON": "Carla"}
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
* decider{"PERSON": "Inga"}
    - slot{"PERSON": "Inga"}
    - action_update_stakeholder
    - slot{"decider": "Inga"}
    - slot{"action_return": true}
    - utter_ask_options
* option{"ORDINAL": "first"}
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
* consequence{"PERSON": "Werner", "ORG": "Werner", "sentiment": "pos"}
    - slot{"PERSON": "Werner"}
    - slot{"sentiment": "pos"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_positive
* correct
    - utter_ask_impact_weight
* quantity{"CARDINAL": "6"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* correct
    - utter_next_consequence
* consequence{"PERSON": "carla"}
    - slot{"PERSON": "carla"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_positive
* wrong
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_impact_weight
* quantity{"CARDINAL": "10"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* wrong
    - utter_ask_consequence_probability
* quantity{"PERCENT": "90 %"}
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
* consequence{"PERSON": "Werner", "PERCENT": "50%", "ORG": "Werner", "sentiment": "neg"}
    - slot{"PERSON": "Werner"}
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
* wrong
    - utter_ask_consequence_probability
* quantity{"PERCENT": "50%"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* consequence{"PERSON": "carla", "sentiment": "pos"}
    - slot{"PERSON": "carla"}
    - slot{"sentiment": "pos"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_positive
* correct
    - utter_ask_impact_weight
* quantity{"CARDINAL": "8"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* correct
    - utter_next_consequence
* deny
    - utter_next_option
* deny{"ORDINAL": "third"}
    - utter_got_everything
    - utter_ask_method
* utilitarism
    - action_evaluation_utilitarism
    - utter_next_method
* deny
    - utter_goodbye

## Generated Story -2022503381031583469
* greeting
    - action_intro
* stakeholder{"GPE": "Bali", "plural": "unspecific_plural"}
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
    - utter_ask_name_singular
* name{"PERSON": "Carl"}
    - slot{"PERSON": "Carl"}
    - action_update_stakeholder
    - slot{"PERSON": "Carl"}
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
    - slot{"PERSON": "Esther"}
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"DATE": "18 years old", "plural": "singular", "moralstatus": "animal"}
    - slot{"moralstatus": "animal"}
    - slot{"plural": "singular"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": true}
    - utter_ask_name_singular
* dontknow
    - action_update_stakeholder
    - slot{"PERSON": "Patrick"}
    - slot{"action_return": true}
    - utter_next_stakeholder
* deny
    - utter_confirm_stakeholders
    - action_choose_decider
* decider{"PERSON": "Carl"}
    - slot{"PERSON": "Carl"}
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
* consequence{"PERSON": "Carl", "deed": "lead to a life"}
    - slot{"PERSON": "Carl"}
    - slot{"deed": "lead to a life"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact
* negative
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_impact_weight
* quantity{"CARDINAL": "9"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* wrong
    - utter_ask_consequence_probability
* quantity{"CARDINAL": "only 70"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* consequence{"sentiment": "pos"}
    - slot{"sentiment": "pos"}
    - action_create_consequence
    - slot{"PERSON": null}
    - slot{"action_return": false}
    - action_choose_affected_stakeholder
* consequence{"PERSON": "Patrick"}
    - slot{"PERSON": "Patrick"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_positive
* correct
    - utter_ask_impact_weight
* quantity{"CARDINAL": "7"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* wrong
    - utter_ask_consequence_probability
* quantity{"PERCENT": "90 %"}
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
* consequence{"PERSON": "esther"}
    - slot{"PERSON": "esther"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_positive
* wrong
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_impact_weight
* quantity{"CARDINAL": "9"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* wrong
    - utter_ask_consequence_probability
* quantity{"PERCENT": "80 %"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* consequence{"PERSON": "Patrick", "ORG": "Patrick", "sentiment": "pos"}
    - slot{"PERSON": "Patrick"}
    - slot{"sentiment": "pos"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_positive
* correct
    - utter_ask_impact_weight
* quantity{"CARDINAL": "5"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* correct
    - utter_next_consequence
* consequence{"PERSON": "Carl", "sentiment": "pos"}
    - slot{"PERSON": "Carl"}
    - slot{"sentiment": "pos"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_positive
* correct
    - utter_ask_impact_weight
* quantity{"CARDINAL": "8"}
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
* stakeholder{"ORDINAL": "First", "plural": "unspecific_plural", "moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - slot{"plural": "unspecific_plural"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": false}
    - utter_ask_quantity
* quantity{"stakeholder": "one person", "CARDINAL": "one"}
    - action_update_stakeholder
    - slot{"plural": "singular"}
    - slot{"action_return": true}
    - utter_ask_name_singular
* deny
    - action_update_stakeholder
    - slot{"PERSON": "Olga"}
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"CARDINAL": "Hundreds", "plural": "unspecific_plural", "moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - slot{"plural": "unspecific_plural"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": false}
    - utter_ask_quantity
* dontknow
    - utter_ask_guess_quantity
* quantity{"CARDINAL": "500"}
    - action_update_stakeholder
    - slot{"plural": "specific_plural"}
    - slot{"action_return": true}
    - utter_ask_name_plural
* deny
    - action_update_stakeholder
    - slot{"PERSON": "the Swabians"}
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
    - slot{"PERSON": "the Saxons"}
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
* decider{"plural": "singular"}
    - slot{"plural": "singular"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 4}
    - slot{"action_return": true}
    - utter_ask_name_singular
* dontknow
    - action_update_stakeholder
    - slot{"decider": "Roswitha"}
    - slot{"PERSON": "Roswitha"}
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
* consequence{"PERSON": "the saxons", "ORG": "Saxons", "sentiment": "neg"}
    - slot{"PERSON": "the saxons"}
    - slot{"sentiment": "neg"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_negative
* correct
    - utter_ask_impact_weight
* quantity{"CARDINAL": "9"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* correct
    - utter_next_consequence
* consequence{"PERSON": "Olga", "sentiment": "neg"}
    - slot{"PERSON": "Olga"}
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
* correct
    - utter_next_consequence
* consequence{"PERSON": "Olga"}
    - slot{"PERSON": "Olga"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_negative
* wrong
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_impact_weight
* quantity{"CARDINAL": "10"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_consequence_definite
* wrong
    - utter_ask_consequence_probability
* quantity{"PERCENT": "50 %"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* deny
    - utter_next_option
* option{"PERSON": "Olga"}
    - slot{"PERSON": "Olga"}
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
* consequence{"NORP": "Swabians", "sentiment": "neg"}
    - slot{"sentiment": "neg"}
    - action_create_consequence
    - slot{"PERSON": null}
    - slot{"action_return": false}
    - action_choose_affected_stakeholder

