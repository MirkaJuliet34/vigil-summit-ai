def evaluate_lead(state):

    score = state["score"]

    if score >= 70:

        state["next_action"] = (
            "invite_vip"
        )

    elif score >= 40:

        state["next_action"] = (
            "send_confirmation"
        )

    else:

        state["next_action"] = (
            "send_nurturing"
        )

    return state