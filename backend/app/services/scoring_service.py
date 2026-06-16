class ScoringService:

    @staticmethod
    def calculate(
        position,
        industry,
        company_size
    ):

        score = 0

        if position.upper() == "CISO":
            score += 40

        elif position.upper() == "CTO":
            score += 35

        if industry == "Financial":
            score += 20

        if industry == "Healthcare":
            score += 20

        if company_size == "1000+":
            score += 20

        return score