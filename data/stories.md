## Story Intro
* greeting
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - action_intro

## Generated Story 7710972032789188724
* greeting{"sentiment": "neu", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - action_intro
* stakeholder{"sentiment": "neu", "stakeholder": "a group of people", "plural": "unspecific_plural"}
    - slot{"plural": "unspecific_plural"}
    - slot{"sentiment": "neu"}
    - slot{"stakeholder": "a group of people"}
    - action_create_stakeholder
    - slot{"name": "the Bavarians"}
    - slot{"amount_stakeholders": 1}
    - utter_ask_quantity
* quantity{"sentiment": "neu", "quantity": "five", "plural": "specific_plural"}
    - slot{"plural": "specific_plural"}
    - slot{"sentiment": "neu"}
    - action_update_stakeholder
    - utter_next_stakeholder

## Generated Story 4445941042976493222
* greeting
    - action_intro
* stakeholder{"sentiment": "neu", "stakeholder": "a group of people", "plural": "unspecific_plural"}
    - slot{"plural": "unspecific_plural"}
    - slot{"sentiment": "neu"}
    - slot{"stakeholder": "a group of people"}
    - action_create_stakeholder
    - slot{"name": "the Bavarians"}
    - slot{"amount_stakeholders": 1}
    - utter_ask_quantity
* quantity{"sentiment": "neu", "stakeholder": "five people", "plural": "specific_plural"}
    - slot{"plural": "specific_plural"}
    - slot{"sentiment": "neu"}
    - slot{"stakeholder": "five people"}
    - action_update_stakeholder
    - utter_next_stakeholder
* stakeholder{"stakeholder": "one single person"}
    - slot{"stakeholder": "one single person"}
    - action_create_stakeholder
    - slot{"name": "Uwe"}
    - slot{"amount_stakeholders": 2}
    - utter_next_stakeholder
* stakeholder{"sentiment": "neu", "stakeholder": "a third person", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - slot{"stakeholder": "a third person"}
    - action_create_stakeholder
    - slot{"name": "Tanja"}
    - slot{"amount_stakeholders": 3}
    - utter_next_stakeholder
* deny{"sentiment": "neg", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neg"}
    - utter_confirm_stakeholders
    - action_choose_decider
* decider{"name": "Tanja"}
    - slot{"name": "Tanja"}
    - action_update_stakeholder
    - slot{"decider": "Tanja"}
    - utter_ask_options

## Generated Story 8378399737143779172
* greeting{"sentiment": "neu", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - action_intro
* stakeholder{"sentiment": "neu", "stakeholder": "a group of people", "plural": "unspecific_plural"}
    - slot{"plural": "unspecific_plural"}
    - slot{"sentiment": "neu"}
    - slot{"stakeholder": "a group of people"}
    - action_create_stakeholder
    - slot{"name": "the Swabians"}
    - slot{"amount_stakeholders": 1}
    - utter_ask_quantity
* quantity{"sentiment": "neu", "stakeholder": "five people", "plural": "specific_plural"}
    - slot{"plural": "specific_plural"}
    - slot{"sentiment": "neu"}
    - slot{"stakeholder": "five people"}
    - action_update_stakeholder
    - utter_next_stakeholder
* stakeholder{"sentiment": "neu", "stakeholder": "a single person", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - slot{"stakeholder": "a single person"}
    - action_create_stakeholder
    - slot{"name": "Viola"}
    - slot{"amount_stakeholders": 2}
    - utter_next_stakeholder
* decider{"sentiment": "neu", "stakeholder": "a third person", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - slot{"stakeholder": "a third person"}
    - action_create_stakeholder
    - slot{"name": "Roswitha"}
    - slot{"decider": "Roswitha"}
    - slot{"amount_stakeholders": 3}
    - utter_next_stakeholder
* deny{"sentiment": "neu", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - utter_confirm_stakeholders
    - utter_confirm_decider
    - utter_ask_options

## Generated Story 8450158913311303025
* greeting{"sentiment": "neu", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - action_intro
* stakeholder{"sentiment": "neu", "stakeholder": "a group of five people", "plural": "specific_plural"}
    - slot{"plural": "specific_plural"}
    - slot{"sentiment": "neu"}
    - slot{"stakeholder": "a group of five people"}
    - action_create_stakeholder
    - slot{"name": "the Swabians"}
    - slot{"amount_stakeholders": 1}
    - utter_next_stakeholder
* stakeholder{"stakeholder": "one single person"}
    - slot{"stakeholder": "one single person"}
    - action_create_stakeholder
    - slot{"name": "Uwe"}
    - slot{"amount_stakeholders": 2}
    - utter_next_stakeholder
* decider{"sentiment": "neu", "stakeholder": "a person", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - slot{"stakeholder": "a person"}
    - action_create_stakeholder
    - slot{"name": "Uwe"}
    - slot{"decider": "Uwe"}
    - slot{"amount_stakeholders": 3}
    - utter_next_stakeholder
* deny{"sentiment": "neu", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - utter_confirm_stakeholders
    - utter_confirm_decider
    - utter_ask_options

## Generated Story -3698605853821150458
* greeting{"sentiment": "neu", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - action_intro
* stakeholder{"sentiment": "neu", "stakeholder": "a person", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - slot{"stakeholder": "a person"}
    - action_create_stakeholder
    - slot{"name": "Harald"}
    - slot{"amount_stakeholders": 1}
    - utter_next_stakeholder
* stakeholder{"sentiment": "neu", "stakeholder": "a group of six people", "plural": "specific_plural"}
    - slot{"plural": "specific_plural"}
    - slot{"sentiment": "neu"}
    - slot{"stakeholder": "a group of six people"}
    - action_create_stakeholder
    - slot{"name": "the Saxons"}
    - slot{"amount_stakeholders": 2}
    - utter_next_stakeholder
* stakeholder{"sentiment": "neu", "stakeholder": "another person", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - slot{"stakeholder": "another person"}
    - action_create_stakeholder
    - slot{"name": "Nathan"}
    - slot{"amount_stakeholders": 3}
    - utter_next_stakeholder
* deny{"sentiment": "neg", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neg"}
    - utter_confirm_stakeholders
    - action_choose_decider
* decider{"name": "Harald"}
    - slot{"stakeholder": "Harald"}
    - action_update_stakeholder
    - slot{"decider": "Harald"}
    - utter_ask_options

## Generated Story 6293403335483464889
* greeting{"sentiment": "neu", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - action_intro
* decider{"sentiment": "neu", "stakeholder": "we", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - slot{"stakeholder": "we"}
    - action_create_stakeholder
    - slot{"name": "Werner"}
    - slot{"decider": "Werner"}
    - slot{"amount_stakeholders": 1}
    - utter_next_stakeholder
* stakeholder{"stakeholder": "one person"}
    - slot{"stakeholder": "one person"}
    - action_create_stakeholder
    - slot{"name": "Roswitha"}
    - slot{"amount_stakeholders": 2}
    - utter_next_stakeholder
* stakeholder{"sentiment": "neu", "stakeholder": "a group of seven people", "plural": "specific_plural"}
    - slot{"plural": "specific_plural"}
    - slot{"sentiment": "neu"}
    - slot{"stakeholder": "a group of seven people"}
    - action_create_stakeholder
    - slot{"name": "the Bavarians"}
    - slot{"amount_stakeholders": 3}
    - utter_next_stakeholder
* deny
    - utter_confirm_stakeholders
    - utter_confirm_decider
    - utter_ask_options

## Generated Story -2283667724973141271
* greeting{"sentiment": "neu", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - action_intro
* stakeholder{"sentiment": "neu", "stakeholder": "a group of people", "plural": "unspecific_plural"}
    - slot{"plural": "unspecific_plural"}
    - slot{"sentiment": "neu"}
    - slot{"stakeholder": "a group of people"}
    - action_create_stakeholder
    - slot{"name": "the Saxons"}
    - slot{"amount_stakeholders": 1}
    - utter_ask_quantity
* quantity{"stakeholder": "five people"}
    - slot{"stakeholder": "five people"}
    - action_update_stakeholder
    - utter_next_stakeholder
* stakeholder{"sentiment": "neu", "stakeholder": "a single person", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - slot{"stakeholder": "a single person"}
    - action_create_stakeholder
    - slot{"name": "Lars"}
    - slot{"amount_stakeholders": 2}
    - utter_next_stakeholder
* stakeholder{"sentiment": "neu", "stakeholder": "the last person", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - slot{"stakeholder": "the last person"}
    - action_create_stakeholder
    - slot{"name": "Esther"}
    - slot{"amount_stakeholders": 3}
    - utter_next_stakeholder
* deny{"sentiment": "neu", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - utter_confirm_stakeholders
    - action_choose_decider
* decider{"name": "Esther"}
    - slot{"name": "Esther"}
    - action_update_stakeholder
    - slot{"decider": "Esther"}
    - utter_ask_options

## Generated Story -1806134547250369189
* greeting{"sentiment": "neu", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - action_intro
* stakeholder{"stakeholder": "one person"}
    - slot{"stakeholder": "one person"}
    - action_create_stakeholder
    - slot{"name": "Lars"}
    - slot{"amount_stakeholders": 1}
    - utter_next_stakeholder
* stakeholder{"sentiment": "neu", "stakeholder": "three people", "plural": "specific_plural"}
    - slot{"plural": "specific_plural"}
    - slot{"sentiment": "neu"}
    - slot{"stakeholder": "three people"}
    - action_create_stakeholder
    - slot{"name": "the Swabians"}
    - slot{"amount_stakeholders": 2}
    - utter_next_stakeholder
* deny{"sentiment": "neu", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - utter_confirm_stakeholders
    - action_choose_decider
* decider{"plural": "singular"}
    - slot{"plural": "singular"}
    - action_create_stakeholder
    - slot{"name": "Nathan"}
    - slot{"decider": "Nathan"}
    - slot{"amount_stakeholders": 3}
    - utter_ask_options

## Generated Story 8737507611311984862
* greeting{"sentiment": "pos", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "pos"}
    - action_intro
* stakeholder{"sentiment": "neu", "stakeholder": "a group of eight people", "plural": "specific_plural"}
    - slot{"plural": "specific_plural"}
    - slot{"sentiment": "neu"}
    - slot{"stakeholder": "a group of eight people"}
    - action_create_stakeholder
    - slot{"name": "the Swabians"}
    - slot{"amount_stakeholders": 1}
    - utter_next_stakeholder
* stakeholder{"sentiment": "neu", "stakeholder": "another person", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - slot{"stakeholder": "another person"}
    - action_create_stakeholder
    - slot{"name": "Frank"}
    - slot{"amount_stakeholders": 2}
    - utter_next_stakeholder
* decider{"sentiment": "neu", "stakeholder": "the third person", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - slot{"stakeholder": "the third person"}
    - action_create_stakeholder
    - slot{"name": "Werner"}
    - slot{"decider": "Werner"}
    - slot{"amount_stakeholders": 3}
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
    - slot{"option": 4}
    - utter_ask_consequences
* consequence{"name": "Frank"}
    - slot{"name": "Frank"}
    - action_create_consequence
    - utter_ask_impact
* negative{"sentiment": "neu", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}

## Generated Story -7847444452878286009
* greeting{"sentiment": "neu", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - action_intro
* stakeholder{"stakeholder": "a person", "name": "jones"}
    - slot{"name": "jones"}
    - slot{"stakeholder": "a person"}
    - action_create_stakeholder
    - slot{"name": "Viola"}
    - slot{"amount_stakeholders": 1}
    - utter_next_stakeholder
* stakeholder{"sentiment": "neu", "stakeholder": "a lot of people", "plural": "unspecific_plural"}
    - slot{"plural": "unspecific_plural"}
    - slot{"sentiment": "neu"}
    - slot{"stakeholder": "a lot of people"}
    - action_create_stakeholder
    - slot{"name": "the Saxons"}
    - slot{"amount_stakeholders": 2}
    - utter_ask_quantity
* deny{"stakeholder": "i"}
    - slot{"stakeholder": "i"}
    - utter_next_stakeholder
* decider{"sentiment": "neu", "stakeholder": "we", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - slot{"stakeholder": "we"}
    - action_create_stakeholder
    - slot{"name": "Samuel"}
    - slot{"decider": "Samuel"}
    - slot{"amount_stakeholders": 3}
    - utter_next_stakeholder
* deny{"stakeholder": "no other persons"}
    - slot{"stakeholder": "no other persons"}
    - utter_confirm_stakeholders
    - utter_confirm_decider
    - utter_ask_options
* option{"sentiment": "neu", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - action_create_option
    - slot{"option": 4}
    - utter_ask_consequences

## Generated Story -2967399477046604769
* greeting{"sentiment": "neu", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - action_intro
* stakeholder{"sentiment": "neu", "stakeholder": "a bunch of people", "plural": "unspecific_plural"}
    - slot{"plural": "unspecific_plural"}
    - slot{"sentiment": "neu"}
    - slot{"stakeholder": "a bunch of people"}
    - action_create_stakeholder
    - slot{"name": "the Saxons"}
    - slot{"amount_stakeholders": 1}
    - utter_ask_quantity
* quantity{"stakeholder": "ten people"}
    - slot{"stakeholder": "ten people"}
    - action_update_stakeholder
    - utter_next_stakeholder
* stakeholder{"sentiment": "neu", "stakeholder": "another person", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - slot{"stakeholder": "another person"}
    - action_create_stakeholder
    - slot{"name": "Nathan"}
    - slot{"amount_stakeholders": 2}
    - utter_next_stakeholder
* deny{"sentiment": "neu", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - utter_confirm_stakeholders
    - action_choose_decider
* decider{"plural": "singular"}
    - slot{"plural": "singular"}
    - action_create_stakeholder
    - slot{"name": "Zoe"}
    - slot{"decider": "Zoe"}
    - slot{"amount_stakeholders": 3}
    - utter_ask_options
* option{"sentiment": "neu", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - action_create_option
    - slot{"option": 4}
    - utter_ask_consequences
* consequence{"name": "Nathan"}
    - slot{"name": "Nathan"}
    - action_create_consequence

## Generated Story 8014866812133259312
* greeting{"sentiment": "neu", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - action_intro
* stakeholder{"name": "Jones"}
    - slot{"name": "Jones"}
    - action_create_stakeholder
    - slot{"name": "Patrick"}
    - slot{"amount_stakeholders": 1}
    - utter_next_stakeholder
* stakeholder{"sentiment": "neu", "stakeholder": "a lot of people", "plural": "unspecific_plural"}
    - slot{"plural": "unspecific_plural"}
    - slot{"sentiment": "neu"}
    - slot{"stakeholder": "a lot of people"}
    - action_create_stakeholder
    - slot{"name": "the Bavarians"}
    - slot{"amount_stakeholders": 2}
    - utter_ask_quantity
* deny
    - utter_next_stakeholder
* decider{"sentiment": "neu", "stakeholder": "we", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - slot{"stakeholder": "we"}
    - action_create_stakeholder
    - slot{"name": "Samuel"}
    - slot{"decider": "Samuel"}
    - slot{"amount_stakeholders": 5}
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
    - slot{"option": 6}
    - utter_ask_consequences
* consequence{"name": "Patrick"}
    - slot{"name": "Patrick"}
    - action_create_consequence
    - utter_ask_impact
* positive{"sentiment": "neu", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - action_update_consequence

## Generated Story -5633725736702802821
* greeting{"sentiment": "neu", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - action_intro
* stakeholder{"sentiment": "neu", "stakeholder": "someone", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - slot{"stakeholder": "someone"}
    - action_create_stakeholder
    - slot{"name": "Werner"}
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"stakeholder": "the person who chases Werner"}
    - slot{"stakeholder": "the person who chases Werner"}
    - action_create_stakeholder
    - slot{"name": "Esther"}
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"sentiment": "neu", "stakeholder": "the next person", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - slot{"stakeholder": "the next person"}
    - action_create_stakeholder
    - slot{"name": "Katharina"}
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": true}
    - utter_next_stakeholder
* deny{"sentiment": "neu", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - utter_confirm_stakeholders
    - action_choose_decider
* decider{"name": "Katharina"}
    - slot{"name": "Katharina"}
    - action_update_stakeholder
    - slot{"decider": "Katharina"}
    - slot{"action_return": true}
    - utter_ask_options
* option{"name": "Werner"}
    - slot{"name": "Werner"}
    - action_create_option
    - slot{"option": 4}
    - slot{"action_return": true}
    - utter_ask_consequences
* consequence{"name": "Esther"}
    - slot{"name": "Esther"}
    - action_create_consequence

## Generated Story -4361855438106255996
* greeting
    - action_intro
* stakeholder{"sentiment": "neu", "stakeholder": "a person", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - slot{"stakeholder": "a person"}
    - action_create_stakeholder
    - slot{"name": "Olga"}
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"sentiment": "neu", "stakeholder": "a large group of people", "plural": "unspecific_plural"}
    - slot{"plural": "unspecific_plural"}
    - slot{"sentiment": "neu"}
    - slot{"stakeholder": "a large group of people"}
    - action_create_stakeholder
    - utter_ask_quantity

## Generated Story -2925079327335999785
* greeting{"sentiment": "neu", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - action_intro
* stakeholder{"sentiment": "neu", "stakeholder": "a person", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - slot{"stakeholder": "a person"}
    - action_create_stakeholder
    - slot{"name": "Olga"}
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"sentiment": "neu", "stakeholder": "a lot of people", "plural": "unspecific_plural"}
    - slot{"plural": "unspecific_plural"}
    - slot{"sentiment": "neu"}
    - slot{"stakeholder": "a lot of people"}
    - action_create_stakeholder
    - utter_ask_quantity

## Generated Story -9199669015521274313
* greeting
    - action_intro
* stakeholder{"sentiment": "neu", "stakeholder": "a group of people", "plural": "unspecific_plural"}
    - slot{"plural": "unspecific_plural"}
    - slot{"sentiment": "neu"}
    - slot{"stakeholder": "a group of people"}
    - action_create_stakeholder
    - slot{"name": "the Hessians"}
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": false}
    - utter_ask_quantity
* quantity{"sentiment": "neu", "stakeholder": "five people", "plural": "specific_plural"}
    - slot{"plural": "specific_plural"}
    - slot{"sentiment": "neu"}
    - slot{"stakeholder": "five people"}
    - action_update_stakeholder
    - utter_next_stakeholder

## Generated Story 3354551786536361783
* greeting{"sentiment": "neu", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - action_intro
* stakeholder{"sentiment": "neu", "stakeholder": "a group of people", "plural": "unspecific_plural"}
    - slot{"plural": "unspecific_plural"}
    - slot{"sentiment": "neu"}
    - slot{"stakeholder": "a group of people"}
    - action_create_stakeholder
    - slot{"name": "the Rhinelanders"}
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": false}
    - utter_ask_quantity
* quantity{"sentiment": "neg", "quantity": "5", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neg"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"sentiment": "neu", "stakeholder": "another person", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - slot{"stakeholder": "another person"}
    - action_create_stakeholder
    - slot{"name": "Nathan"}
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": true}
    - utter_next_stakeholder
* deny{"sentiment": "neu", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - utter_confirm_stakeholders
    - action_choose_decider
* decider{"plural": "singular"}
    - slot{"plural": "singular"}
    - action_create_stakeholder
    - slot{"decider": "Katharina"}
    - slot{"name": "Katharina"}
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": true}
    - utter_ask_options
* option{"sentiment": "neu", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - action_create_option
    - slot{"option": 4}
    - slot{"action_return": true}
    - utter_ask_consequences
* consequence{"name": "The Rhinelanders"}
    - slot{"name": "The Rhinelanders"}

## Generated Story -2408831251863862597
* greeting{"sentiment": "neu", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - action_intro
* stakeholder{"sentiment": "neu", "stakeholder": "a group consisting of five people", "plural": "specific_plural"}
    - slot{"plural": "specific_plural"}
    - slot{"sentiment": "neu"}
    - slot{"stakeholder": "a group consisting of five people"}
    - action_create_stakeholder
    - slot{"name": "the Rhinelanders"}
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"sentiment": "neu", "stakeholder": "another person", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - slot{"stakeholder": "another person"}
    - action_create_stakeholder
    - slot{"name": "Benjamin"}
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": true}
    - utter_next_stakeholder
* decider{"sentiment": "neu", "stakeholder": "a third person", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - slot{"stakeholder": "a third person"}
    - action_create_stakeholder
    - slot{"decider": "Nathan"}
    - slot{"name": "Nathan"}
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": true}
    - utter_next_stakeholder
* deny{"sentiment": "neu", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - utter_confirm_stakeholders
    - utter_confirm_decider
    - utter_ask_options
* option{"sentiment": "neu", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - action_create_option
    - slot{"option": 4}
    - slot{"action_return": true}
    - utter_ask_consequences
* consequence{"name": "Benjamin"}
    - slot{"name": "Benjamin"}
    - action_create_consequence
    - slot{"action_return": false}
    - utter_ask_impact
* negative{"name": "Benjamin"}
    - slot{"name": "Benjamin"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* consequence{"name": "the Rhinelanders"}
    - slot{"name": "the Rhinelanders"}
    - action_create_consequence
    - slot{"action_return": false}
    - utter_ask_impact
* positive{"name": "the Rhinelanders"}
    - slot{"name": "the Rhinelanders"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* deny{"sentiment": "neg", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neg"}
    - utter_next_option
* option{"name": "Nathan"}
    - slot{"name": "Nathan"}
    - action_create_option
    - slot{"option": 7}
    - slot{"action_return": true}
    - utter_ask_consequences
* consequence{"name": "the Rhinelanders"}
    - slot{"name": "the Rhinelanders"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_negative
* affirm
    - utter_next_consequence
* consequence{"name": "Benjamin"}
    - slot{"name": "Benjamin"}
    - action_create_consequence
    - slot{"action_return": true}
    - utter_ask_impact_negative
* positive{"sentiment": "neu", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* deny{"sentiment": "neu", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}

## Generated Story 7039822916780604550
* greeting{"sentiment": "neu", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - action_intro

## Generated Story 397795911753488933
* greeting{"sentiment": "neu", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - action_intro
* stakeholder{"name": "jones"}
    - slot{"name": "jones"}
    - action_create_stakeholder
    - slot{"name": "Daniel"}
    - slot{"amount_stakeholders": 1}
    - slot{"action_return": true}
    - utter_next_stakeholder
* stakeholder{"sentiment": "neu", "stakeholder": "a large group of people", "plural": "unspecific_plural"}
    - slot{"plural": "unspecific_plural"}
    - slot{"sentiment": "neu"}
    - slot{"stakeholder": "a large group of people"}
    - action_create_stakeholder
    - slot{"name": "the Saxons"}
    - slot{"amount_stakeholders": 2}
    - slot{"action_return": false}
    - utter_ask_quantity
* deny{"sentiment": "neu", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - utter_next_stakeholder
* deny{"sentiment": "neu", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - utter_confirm_stakeholders
    - action_choose_decider
* decider{"plural": "singular"}
    - slot{"plural": "singular"}
    - action_create_stakeholder
    - slot{"decider": "Carla"}
    - slot{"name": "Carla"}
    - slot{"amount_stakeholders": 3}
    - slot{"action_return": true}
    - utter_ask_options
* option{"name": "Daniel"}
    - slot{"name": "Daniel"}
    - action_create_option
    - slot{"option": 4}
    - slot{"action_return": true}
    - utter_ask_consequences
* consequence{"sentiment": "neu", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - action_create_consequence
    - slot{"action_return": false}
    - utter_ask_impact
* positive{"name": "Daniel"}
    - slot{"name": "Daniel"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* consequence{"name": "The Saxons"}
    - slot{"name": "The Saxons"}
    - action_create_consequence
    - slot{"action_return": false}
    - utter_ask_impact
* negative{"name": "the Saxons"}
    - slot{"name": "the Saxons"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* deny{"sentiment": "neu", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - utter_next_option
* option{"sentiment": "neu", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - action_create_option
    - slot{"option": 7}
    - slot{"action_return": true}
    - utter_ask_consequences
* consequence{"name": "Daniel"}
    - slot{"name": "Daniel"}
    - action_create_consequence
    - slot{"action_return": false}
    - utter_ask_impact
* negative{"sentiment": "neu", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* consequence{"name": "the Saxons"}
    - slot{"name": "the Saxons"}
    - action_create_consequence
    - slot{"action_return": false}
    - utter_ask_impact
* positive{"sentiment": "neu", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - action_update_consequence
    - slot{"action_return": true}
    - utter_next_consequence
* deny{"sentiment": "neu", "plural": "singular"}
    - slot{"plural": "singular"}
    - slot{"sentiment": "neu"}
    - utter_next_option
* deny

