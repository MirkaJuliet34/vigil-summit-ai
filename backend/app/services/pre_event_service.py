from app.models.interaction import Interaction


class PreEventService:

    @staticmethod
    def generate_confirmation_message(
        lead,
        profile
    ):

        return (
            f"Olá {lead.name}, "
            f"como {lead.position} da empresa "
            f"{lead.company}, acreditamos que "
            f"o Vigil Summit terá conteúdos "
            f"relevantes para seu contexto."
        )

    @staticmethod
    def generate_reminder_message(
        lead
    ):

        return (
            f"Olá {lead.name}, "
            f"faltam poucos dias para o "
            f"Vigil Summit. Esperamos você!"
        )

    @staticmethod
    def register_interaction(
        db,
        lead_id,
        interaction_type,
        content,
        status="sent"
    ):

        interaction = Interaction(
            lead_id=lead_id,
            channel="email",
            interaction_type=interaction_type,
            content=content,
            status=status
        )

        db.add(interaction)