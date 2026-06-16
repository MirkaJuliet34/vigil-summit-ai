from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.dependencies import get_db

from app.models.lead import Lead
from app.models.enriched_profile import EnrichedProfile
from app.models.interaction import Interaction

from app.schemas.lead import LeadCreate
from app.schemas.lead import LeadResponse

from app.services.enrichment_service import EnrichmentService
from app.services.scoring_service import ScoringService
from app.services.classification_service import ClassificationService
from app.services.action_service import ActionService


router = APIRouter()


@router.post(
    "/",
    response_model=LeadResponse
)
def create_lead(
    lead: LeadCreate,
    db: Session = Depends(get_db)
):

    # Cria lead
    new_lead = Lead(
        name=lead.name,
        email=lead.email,
        phone=lead.phone,
        company=lead.company,
        position=lead.position
    )

    db.add(new_lead)
    db.commit()
    db.refresh(new_lead)

    # Enriquecimento
    enriched = EnrichmentService.enrich_lead(
        new_lead
    )

    # Salva perfil enriquecido
    profile = EnrichedProfile(
        lead_id=new_lead.id,
        industry=enriched["industry"],
        company_size=enriched["company_size"],
        seniority=enriched["seniority"],
        interests=enriched["interests"],
        linkedin_url=enriched["linkedin_url"]
    )

    db.add(profile)

    # Registra interação
    interaction = Interaction(
        lead_id=new_lead.id,
        channel="system",
        interaction_type="lead_created",
        content="Lead entered the funnel",
        status="completed"
    )

    db.add(interaction)

    # Score
    score = ScoringService.calculate(
        position=new_lead.position,
        industry=enriched["industry"],
        company_size=enriched["company_size"]
    )

    # Classificação
    status = ClassificationService.classify(
        score
    )

    # Próxima ação
    next_action = ActionService.determine_action(
        status
    )

    # Atualiza lead
    new_lead.score = score
    new_lead.status = status
    new_lead.next_action = next_action

    db.commit()
    db.refresh(new_lead)

    return new_lead