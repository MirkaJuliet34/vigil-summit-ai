class ActionService:

    @staticmethod
    def determine_action(status):

        if status == "hot":
            return "invite_vip"

        if status == "warm":
            return "send_confirmation"

        return "send_nurturing"