class ClassificationService:

    @staticmethod
    def classify(score: int):

        if score >= 70:
            return "hot"

        if score >= 40:
            return "warm"

        return "cold"