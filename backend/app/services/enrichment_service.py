class EnrichmentService:

    @staticmethod
    def enrich_lead(lead):

        company = lead.company.lower()

        industry = "Technology"

        if "bank" in company:
            industry = "Financial"

        if "health" in company:
            industry = "Healthcare"

        company_size = "201-1000"

        seniority = "Decision Maker"

        interests = (
            "LGPD,SOC2,ISO27001"
        )

        linkedin_url = (
            f"https://linkedin.com/in/{lead.name}"
        )

        return {
            "industry": industry,
            "company_size": company_size,
            "seniority": seniority,
            "interests": interests,
            "linkedin_url": linkedin_url
        }