## Generated Story -6703141282032847664
* greeting{"sentiment": "neu", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - action_intro
* stakeholder{"sentiment": "neu", "stakeholder": "a person", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - action_create_stakeholder
    - slot{"PERSON": "Samuel"}
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"sentiment": "neu", "stakeholder": "a large group of people", "plural": "unspecific_plural"}
    - slot{"plural": "unspecific_plural"}
    - slot{"sentiment": "neu"}
    - action_create_stakeholder
    - slot{"PERSON": "the Palatines"}
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": false}
    - utter_ask_quantity
* deny{"sentiment": "neu", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - utter_next_stakeholder
* decider
    - action_create_stakeholder
    - slot{"decider": "Amelie"}
    - slot{"PERSON": "Amelie"}
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": true}
    - utter_next_stakeholder
* deny{"sentiment": "neg", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neg"}
    - utter_confirm_stakeholders
    - utter_confirm_decider
    - utter_ask_options
* option{"sentiment": "neu", "deed": "help the injured person", "plural": "singular"}
    - slot{"deed": "help the injured person"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - action_create_option
    - slot{"deed": "interrupt the game"}
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
    - slot{"deed": "help the injured person"}
    - utter_ask_identified_deed
* correct
    - action_create_deed
    - slot{"action_return": true}
    - utter_ask_universalizable
* correct
    - action_update_deed
    - slot{"action_return": true}
    - slot{"deed": null}
    - utter_next_deed
* deny{"sentiment": "neu", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - utter_ask_consequences
* consequence{"sentiment": "neu", "PERSON": "samuel", "plural": "singular"}
    - slot{"PERSON": "samuel"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - action_create_consequence
    - slot{"action_return": false}
    - utter_ask_impact
* positive{"sentiment": "neu", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_impact_weight
* quantity{"sentiment": "neu", "quantity": "7", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence

## Generated Story 8081663772955935236
* greeting{"sentiment": "neu", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - action_intro
* stakeholder{"sentiment": "neu", "stakeholder": "a person", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - action_create_stakeholder
    - slot{"PERSON": "Nathan"}
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"sentiment": "neu", "stakeholder": "the person", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - action_create_stakeholder
    - slot{"PERSON": "Katharina"}
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"sentiment": "neu", "stakeholder": "the person", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - action_create_stakeholder
    - slot{"PERSON": "Uwe"}
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": true}
    - utter_next_stakeholder
* deny{"sentiment": "neg", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neg"}
    - utter_confirm_stakeholders
    - action_choose_decider
* decider{"PERSON": "Uwe"}
    - slot{"PERSON": "Uwe"}
    - action_update_stakeholder
    - slot{"decider": "Uwe"}
    - slot{"action_return": true}
    - utter_ask_options
* option{"sentiment": "neu", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - action_create_option
    - slot{"deed": null}
    - slot{"option": 4}
    - slot{"action_return": true}
    - utter_next_deed
* deed
    - action_create_deed
    - slot{"action_return": true}
    - utter_ask_universalizable
* wrong
    - action_update_deed

## Generated Story -1953137291995998686
* greeting{"sentiment": "neu", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - action_intro
* stakeholder{"sentiment": "neu", "stakeholder": "a group of people", "plural": "unspecific_plural"}
    - slot{"plural": "unspecific_plural"}
    - slot{"sentiment": "neu"}
    - action_create_stakeholder
    - slot{"PERSON": "the Palatines"}
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": false}
    - utter_ask_quantity
* quantity{"sentiment": "neu", "quantity": "13", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"sentiment": "neu", "stakeholder": "another person", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - action_create_stakeholder
    - slot{"PERSON": "Daniel"}
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": true}
    - utter_next_stakeholder
* deny{"sentiment": "neg", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neg"}
    - utter_confirm_stakeholders
    - action_choose_decider
* decider{"plural": "singular"}
    - slot{"plural": "singular"}
    - action_create_stakeholder
    - slot{"decider": "Samuel"}
    - slot{"PERSON": "Samuel"}
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": true}
    - utter_ask_options
* option{"sentiment": "neu", "deed": "flip a switch", "plural": "singular"}
    - slot{"deed": "flip a switch"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - action_create_option
    - slot{"deed": "flip a switch"}
    - slot{"option": 4}
    - slot{"action_return": true}
    - utter_ask_identified_deed
* wrong
    - action_update_option
    - slot{"action_return": true}

## Generated Story 260564188287088586
* greeting{"sentiment": "neu", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - action_intro
* stakeholder{"stakeholder": "a patient"}
    - action_create_stakeholder
    - slot{"PERSON": "Tanja"}
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - utter_next_stakeholder
* decider{"sentiment": "neu", "stakeholder": "a healthcare professional", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - action_create_stakeholder
    - slot{"decider": "Lars"}
    - slot{"PERSON": "Lars"}
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": true}
    - utter_next_stakeholder
* deny{"sentiment": "neg", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neg"}
    - utter_confirm_stakeholders
    - utter_confirm_decider
    - utter_ask_options
* option{"sentiment": "neu", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - action_create_option
    - slot{"deed": null}
    - slot{"option": 3}
    - slot{"action_return": true}
    - utter_next_deed
* deed{"deed": "saving the patients life"}
    - slot{"deed": "saving the patients life"}
    - action_create_deed
    - slot{"action_return": true}
    - utter_ask_universalizable
* correct
    - action_update_deed
    - utter_next_deed
* deny{"sentiment": "neu", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - utter_ask_consequences

## Generated Story 3386876226607047506
* greeting{"sentiment": "neu", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - action_intro
* stakeholder{"stakeholder": "a patient"}
    - action_create_stakeholder
    - slot{"PERSON": "Greta"}
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - utter_next_stakeholder
* decider{"sentiment": "neu", "stakeholder": "a healthcare professional", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - action_create_stakeholder
    - slot{"decider": "Viola"}
    - slot{"PERSON": "Viola"}
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": true}
    - utter_next_stakeholder
* deny{"sentiment": "neg", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neg"}
    - utter_confirm_stakeholders
    - utter_confirm_decider
    - utter_ask_options
* option{"sentiment": "neu", "deed": "try to change the patients", "plural": "singular"}
    - slot{"deed": "try to change the patients"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - action_create_option
    - slot{"deed": "try to change the patients"}
    - slot{"option": 3}
    - slot{"action_return": true}
    - utter_ask_identified_deed
* wrong
    - action_update_option
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deed{"deed": "prevent the"}
    - slot{"deed": "prevent the"}
    - action_create_deed
    - slot{"action_return": true}
    - utter_ask_universalizable
* correct
    - action_update_deed
    - slot{"action_return": true}
    - slot{"deed": null}
    - utter_next_deed
* deny{"sentiment": "neu", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - utter_ask_consequences
* consequence{"sentiment": "neu", "PERSON": "Greta", "plural": "singular"}
    - slot{"PERSON": "greta"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - action_create_consequence
    - slot{"action_return": false}
    - utter_ask_impact
* positive{"sentiment": "pos", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "pos"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_impact_weight
* quantity{"sentiment": "pos", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "pos"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* deny{"sentiment": "neu", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - utter_next_option
* option
    - action_create_option
    - slot{"deed": null}
    - slot{"option": 6}
    - slot{"action_return": true}
    - utter_next_deed
* deed{"deed": "prevent"}
    - slot{"deed": "prevent"}
    - action_create_deed
    - slot{"action_return": true}
    - utter_ask_universalizable
* wrong
    - action_update_deed
    - slot{"action_return": true}
    - slot{"deed": null}
    - utter_next_deed
* deed
    - action_create_deed
    - slot{"action_return": true}
    - utter_ask_universalizable
* correct
    - action_update_deed
    - utter_ask_consequences
* consequence{"sentiment": "neu", "PERSON": "greta", "plural": "singular"}
    - slot{"PERSON": "greta"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - action_create_consequence
    - slot{"action_return": false}
    - utter_ask_impact
* negative{"sentiment": "neg", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neg"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_impact_weight
* quantity{"sentiment": "neg", "quantity": "8", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neg"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* deny{"sentiment": "neg", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neg"}
    - utter_next_option
* deny{"sentiment": "neu", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - utter_got_everything
    - utter_ask_method
* deontology
    - action_evaluation_deontology
    - utter_next_method

## Generated Story 4739653710744036292
* greeting{"sentiment": "neu", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - action_intro
* stakeholder{"sentiment": "neu", "stakeholder": "a person", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - action_create_stakeholder
    - slot{"PERSON": "Viola"}
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"sentiment": "neu", "stakeholder": "a group of people", "plural": "unspecific_plural"}
    - slot{"plural": "unspecific_plural"}
    - slot{"sentiment": "neu"}
    - action_create_stakeholder
    - slot{"PERSON": "the Bavarians"}
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": false}
    - utter_ask_quantity
* quantity{"stakeholder": "46 persons"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* decider{"stakeholder": "a person"}
    - action_create_stakeholder
    - slot{"decider": "the Hessians"}
    - slot{"PERSON": "the Hessians"}
    - slot{"amount_stakeholders": 4}
    - slot{"action_return": false}
    - utter_next_stakeholder
* deny{"sentiment": "neg", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neg"}
    - utter_confirm_stakeholders
    - utter_confirm_decider
    - utter_ask_moral_question
* moralquestion{"stakeholder": "a person"}
    - action_update_context

## Generated Story 7305082844865428284
* greeting{"sentiment": "neu", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - action_intro
* stakeholder
    - action_create_stakeholder
    - slot{"PERSON": "Tanja"}
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"sentiment": "neu", "stakeholder": "a group of people", "plural": "unspecific_plural"}
    - slot{"plural": "unspecific_plural"}
    - slot{"sentiment": "neu"}
    - action_create_stakeholder
    - slot{"PERSON": "the Swabians"}
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": false}
    - utter_ask_quantity
* quantity{"sentiment": "neu", "stakeholder": "ten people", "plural": "specific_plural"}
    - slot{"plural": "specific_plural"}
    - slot{"sentiment": "neu"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"sentiment": "neu", "stakeholder": "another group of people", "plural": "unspecific_plural"}
    - slot{"plural": "unspecific_plural"}
    - slot{"sentiment": "neu"}
    - action_create_stakeholder
    - slot{"PERSON": "the Hessians"}
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": false}
    - utter_ask_quantity
* quantity{"sentiment": "neu", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* deny{"sentiment": "neu", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - utter_confirm_stakeholders
    - action_choose_decider
* decider{"name": "Tanja"}
    - slot{"PERSON": "Tanja"}
    - action_update_stakeholder
    - slot{"decider": "Tanja"}
    - slot{"action_return": true}
    - utter_ask_moral_question
* moralquestion
    - action_update_context
    - slot{"action_return": true}
    - utter_ask_options
* option{"sentiment": "neu", "plural": "unspecific_plural"}
    - slot{"plural": "unspecific_plural"}
    - slot{"sentiment": "neu"}
    - action_create_option
    - slot{"deed": null}
    - slot{"option": 5}
    - slot{"action_return": true}
    - utter_next_deed
* deed{"deed": "the act of rescuing people"}
    - slot{"deed": "the act of rescuing people"}
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
    - slot{"deed": "Also, leaving the group with fewer persons behind"}
    - slot{"action_return": true}
    - utter_ask_universalizable
* wrong
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deny{"sentiment": "neg", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neg"}
    - utter_ask_consequences
* consequence{"sentiment": "neu", "PERSON": "the swabians", "plural": "singular"}
    - slot{"PERSON": "the swabians"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - action_create_consequence
    - slot{"action_return": false}
    - utter_ask_impact
* positive{"sentiment": "neu", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_impact_weight
* quantity{"sentiment": "neu", "quantity": "9", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* consequence{"sentiment": "neu", "PERSON": "the hessians", "plural": "singular"}
    - slot{"PERSON": "the hessians"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - action_create_consequence
    - slot{"action_return": false}
    - utter_ask_impact
* negative
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_impact_weight
* quantity
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* deny{"sentiment": "neg", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neg"}
    - utter_next_option
* option{"sentiment": "neu", "plural": "unspecific_plural"}
    - slot{"plural": "unspecific_plural"}
    - slot{"sentiment": "neu"}
    - action_create_option
    - slot{"deed": null}
    - slot{"option": 10}
    - slot{"action_return": true}
    - utter_next_deed
* deed
    - action_create_deed
    - slot{"deed": "That would imply leaving the larger group behind"}
    - slot{"action_return": true}
    - utter_ask_universalizable
* wrong
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deed{"sentiment": "neu", "plural": "unspecific_plural"}
    - slot{"plural": "unspecific_plural"}
    - slot{"sentiment": "neu"}
    - action_create_deed
    - slot{"deed": "Saving the other group"}
    - slot{"action_return": true}
    - utter_ask_universalizable
* wrong
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deny{"sentiment": "neg", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neg"}
    - utter_ask_consequences
* consequence{"sentiment": "neu", "PERSON": "the hessians", "plural": "singular"}
    - slot{"PERSON": "the hessians"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - action_create_consequence
    - slot{"action_return": false}
    - utter_ask_impact
* positive{"sentiment": "pos", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "pos"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_impact_weight
* quantity{"sentiment": "neg", "quantity": "7", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neg"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* consequence{"sentiment": "neu", "PERSON": "the swabians", "plural": "singular"}
    - slot{"PERSON": "the swabians"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - action_create_consequence
    - slot{"action_return": false}
    - utter_ask_impact
* negative
    - action_update_consequence
    - slot{"action_return": true}
    - utter_ask_impact_weight
* quantity{"sentiment": "neg", "quantity": "9", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neg"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* deny{"sentiment": "neg", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neg"}
    - utter_next_option
* deny{"sentiment": "neu", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
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

## Generated Story -2501030225607528748
* greeting{"sentiment": "neu", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - action_intro
* stakeholder{"sentiment": "neu", "plural": "unspecific_plural"}
    - slot{"plural": "unspecific_plural"}
    - slot{"sentiment": "neu"}
    - action_create_stakeholder
    - slot{"PERSON": "the Hessians"}
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": false}
    - utter_ask_quantity
* quantity{"sentiment": "neu", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"sentiment": "neu", "stakeholder": "a group of people", "plural": "unspecific_plural"}
    - slot{"plural": "unspecific_plural"}
    - slot{"sentiment": "neu"}
    - action_create_stakeholder
    - slot{"PERSON": "the Bavarians"}
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": false}
    - utter_ask_quantity
* dontknow
    - utter_ask_guess_quantity
* quantity{"sentiment": "neu", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"sentiment": "neu", "plural": "unspecific_plural"}
    - slot{"plural": "unspecific_plural"}
    - slot{"sentiment": "neu"}
    - action_create_stakeholder
    - slot{"PERSON": "the Palatines"}
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": false}
    - utter_ask_quantity
* dontknow
    - utter_ask_guess_quantity
* quantity{"sentiment": "neu", "stakeholder": "ten people", "plural": "specific_plural"}
    - slot{"plural": "specific_plural"}
    - slot{"sentiment": "neu"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder

## Generated Story 3661097128600878043
* greeting{"sentiment": "neu", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - action_intro
* stakeholder{"sentiment": "neu", "stakeholder": "a group of people", "plural": "unspecific_plural"}
    - slot{"plural": "unspecific_plural"}
    - slot{"sentiment": "neu"}
    - action_create_stakeholder
    - slot{"PERSON": "the Rhinelanders"}
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": false}
    - utter_ask_quantity
* dontknow
    - utter_ask_guess_quantity
* dontknow
    - utter_too_bad
    - utter_next_stakeholder

## Generated Story -7621104021135621718
* greeting
    - action_intro
* stakeholder{"stakeholder": "a group of people", "plural": "unspecific_plural"}
    - slot{"plural": "unspecific_plural"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": false}
    - utter_ask_quantity
* quantity{"quantity": "5", "CARDINAL": "5"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_ask_name_plural
* dontknow
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"stakeholder": "a single person", "plural": "singular"}
    - slot{"plural": "singular"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": true}
    - utter_ask_name_singular
* name
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* decider{"stakeholder": "a person"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": true}
    - utter_ask_name_singular
* deny
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* deny
    - utter_confirm_stakeholders

## Generated Story 6199862161884845419
* greeting
    - action_intro
* stakeholder{"stakeholder": "a group of people", "plural": "unspecific_plural", "moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - slot{"plural": "unspecific_plural"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": false}
    - utter_ask_quantity
* quantity{"quantity": "7", "CARDINAL": "7"}
    - action_update_stakeholder
    - slot{"plural": "specific_plural"}
    - slot{"action_return": true}
    - utter_ask_name_plural
* dontknow
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"plural": "singular", "moralstatus": "animal"}
    - slot{"moralstatus": "animal"}
    - slot{"plural": "singular"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": true}
    - utter_ask_name_singular
* name
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus
    - utter_ask_moral_status_weight
* quantity{"quantity": "5", "CARDINAL": "5"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder

## Generated Story -7074071357169509213
* greeting
    - action_intro
* stakeholder{"PERSON": "Jones", "ORDINAL": "First", "PERSON": "Jones", "plural": "singular"}
    - slot{"PERSON": "Jones"}
    - slot{"plural": "singular"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 1}
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
* dontknow
    - utter_ask_guess_quantity
* quantity{"CARDINAL": "about 3 million"}
    - action_update_stakeholder
    - slot{"plural": "specific_plural"}
    - slot{"action_return": true}
    - utter_ask_name_plural
* name
    - action_update_stakeholder
    - slot{"PERSON": "Jones"}
    - slot{"action_return": true}
    - utter_next_stakeholder

## Generated Story 192684572851654829
* greeting
    - action_intro
* stakeholder{"PERSON": "David", "plural": "singular"}
    - slot{"plural": "singular"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - utter_ask_identified_name
* correct
    - action_update_stakeholder
    - slot{"PERSON": "Inga"}
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
* deny
    - utter_ask_guess_quantity
* quantity{"CARDINAL": "About 6 million"}
    - action_update_stakeholder
    - slot{"plural": "specific_plural"}
    - slot{"action_return": true}
    - utter_ask_name_plural
* deny{"CARDINAL": "one"}
    - action_update_stakeholder
    - slot{"PERSON": "the Saxons"}
    - slot{"action_return": true}
    - utter_next_stakeholder

## Generated Story 6540634725673596884
* greeting
    - action_intro
* stakeholder{"PERSON": "Jones", "ORDINAL": "First", "plural": "singular"}
    - slot{"PERSON": "Jones"}
    - slot{"plural": "singular"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - utter_ask_identified_name
* correct
    - action_update_stakeholder
    - slot{"PERSON": "Werner"}
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"stakeholder": "a large group of people", "plural": "unspecific_plural", "moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - slot{"plural": "unspecific_plural"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": false}
    - utter_ask_quantity
* quantity{"CARDINAL": "3 million"}
    - action_update_stakeholder
    - slot{"plural": "specific_plural"}
    - slot{"action_return": true}
    - utter_ask_name_plural
* dontknow
    - action_update_stakeholder
    - slot{"PERSON": "the Rhinelanders"}
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"plural": "singular", "moralstatus": "animal"}
    - slot{"moralstatus": "animal"}
    - slot{"plural": "singular"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": true}
    - utter_ask_name_singular
* name{"PERSON": "Fluffy"}
    - slot{"PERSON": "Fluffy"}
    - action_update_stakeholder
    - slot{"PERSON": "Fluffy"}
    - slot{"action_return": true}
    - utter_ask_moral_status_weight
* quantity{"CARDINAL": "8"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* decider{"stakeholder": "one person", "CARDINAL": "one"}

## Generated Story -7388436401191886344
* greeting
    - action_intro
* decider
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": false}

## Generated Story -4815676424493487830
* greeting
    - action_intro
* decider{"ORG": "Path A or Path B", "plural": "unspecific_plural"}
    - slot{"plural": "unspecific_plural"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": false}
    - utter_ask_quantity
* quantity
    - action_update_stakeholder
    - slot{"plural": "specific_plural"}
    - slot{"action_return": true}

## Generated Story -2308450246546178712
* greeting
    - action_intro
* decider{"ORG": "Path A or Path B", "plural": "unspecific_plural"}
    - slot{"plural": "unspecific_plural"}
    - action_create_stakeholder
    - slot{"moralstatus": null}
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
    - slot{"decider": "Carla"}
    - slot{"PERSON": "Carla"}
    - slot{"action_return": true}
    - utter_ask_moral_status
* moralstatus{"moralstatus": "machine"}
    - slot{"moralstatus": "machine"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"PERSON": "Carla", "plural": "unspecific_plural", "moralstatus": "human"}
    - slot{"PERSON": "Carla"}
    - slot{"moralstatus": "human"}
    - slot{"plural": "unspecific_plural"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": false}
    - utter_ask_quantity
* quantity{"CARDINAL": "7"}
    - action_update_stakeholder
    - slot{"plural": "specific_plural"}
    - slot{"action_return": true}
    - utter_ask_name_plural
* dontknow
    - action_update_stakeholder
    - slot{"PERSON": "the Hessians"}
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"stakeholder": "another group", "plural": "unspecific_plural", "moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - slot{"plural": "unspecific_plural"}
    - action_create_stakeholder
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": false}
    - utter_ask_quantity
* dontknow
    - utter_ask_guess_quantity
* quantity{"stakeholder": "ten people", "CARDINAL": "ten"}
    - action_update_stakeholder
    - slot{"plural": "specific_plural"}
    - slot{"action_return": true}
    - utter_ask_name_plural
* deny
    - action_update_stakeholder
    - slot{"PERSON": "the Palatines"}
    - slot{"action_return": true}
    - utter_next_stakeholder
* deny
    - utter_confirm_stakeholders
    - utter_confirm_decider
    - utter_ask_moral_question
* moralquestion
    - utter_ask_options
* option
    - action_create_option
    - slot{"deed": null}
    - slot{"option": 4}
    - slot{"action_return": true}
    - utter_ask_deed
* deed{"stakeholder": "ten people", "CARDINAL": "ten"}
    - action_create_deed
    - slot{"deed": "Rescuing ten people"}
    - slot{"action_return": true}
    - utter_ask_universalizable
* correct
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deed
    - action_create_deed
    - slot{"deed": "Leaving the other group behind."}
    - slot{"action_return": true}
    - utter_ask_universalizable
* wrong
    - action_update_deed
    - slot{"deed": null}
    - slot{"action_return": true}
    - utter_next_deed
* deny
    - utter_ask_consequences
* consequence{"ORG": "Palatines", "sentiment": "pos"}
    - slot{"sentiment": "pos"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_positive
* correct
    - utter_ask_impact_weight
* quantity{"CARDINAL": "8"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* consequence{"NORP": "Hessians", "sentiment": "neg"}
    - slot{"sentiment": "neg"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_negative
* correct
    - utter_ask_impact_weight
* quantity{"CARDINAL": "10"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* deny
    - utter_next_option
* option{"ORG": "Carla", "ORDINAL": "first", "NORP": "Hessians"}
    - action_create_option
    - slot{"deed": null}
    - slot{"option": 9}
    - slot{"action_return": true}

