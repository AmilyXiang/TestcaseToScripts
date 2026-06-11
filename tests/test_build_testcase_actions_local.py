from build_testcase_actions_local import build_rows


def test_leading_setup_actions_become_preconditions_for_call_flow():
    payload = {
        "Worksheet": [
            {
                "case_id": "10172164",
                "title": "US002-09_02_Incoming_call_while_settings_menu_8262_SIP",
                "preconditions": "",
                "steps": [
                    {
                        "step_no": 1,
                        "action_substeps": [
                            "On the DUT (mono or multiline) go to the application menu screen, select the Settings menu.",
                            "Select and active the language menu.",
                            "In the same time the DUT receives an incoming call.",
                            "Check that incoming call is presented on the DUT.",
                        ],
                        "expected_checkpoints": [
                            "The DECT handset can display the incoming call screen and rings according to handset settings.",
                            "user can answer this incoming call by pressing answer keys.",
                        ],
                    }
                ],
            }
        ]
    }

    rows = build_rows(payload)

    assert len(rows) == 2

    assert rows[0]["action_text"] == "In the same time the DUT receives an incoming call."
    assert rows[0]["expected_text"] == "The DECT handset can display the incoming call screen and rings according to handset settings."
    assert rows[0]["precondition_required"] is True
    assert rows[0]["precondition_intent"] == "ui_context"
    assert rows[0]["action_intent"] == "receive_incoming_call"
    assert rows[0]["expected_intent"] == "assert_displayed_incoming_call"
    assert "select the Settings menu" in rows[0]["precondition_text"]
    assert "language menu" in rows[0]["precondition_text"]

    assert rows[1]["action_text"] == "Check that incoming call is presented on the DUT."
    assert rows[1]["expected_text"] == "user can answer this incoming call by pressing answer keys."
    assert rows[1]["action_intent"] == "check_call_presentation"
    assert rows[1]["expected_intent"] == "assert_call_established"
    assert rows[1]["precondition_required"] is False
