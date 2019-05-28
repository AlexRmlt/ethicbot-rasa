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
    - utter_ask_moral_status
* moralstatus{"moralstatus": "human"}
    - slot{"moralstatus": "human"}
    - action_update_stakeholder
    - slot{"action_return": true}
    - utter_next_stakeholder
* deny
    - utter_confirm_stakeholders
    - action_choose_decider

