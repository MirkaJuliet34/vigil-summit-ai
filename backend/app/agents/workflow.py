from langgraph.graph import StateGraph

from app.agents.state import LeadState

from app.agents.nodes import evaluate_lead


builder = StateGraph(LeadState)

builder.add_node(
    "evaluate_lead",
    evaluate_lead
)

builder.set_entry_point(
    "evaluate_lead"
)

builder.set_finish_point(
    "evaluate_lead"
)

graph = builder.compile()