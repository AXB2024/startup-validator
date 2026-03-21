from langgraph.graph import StateGraph
from typing import TypedDict, List

from backend.workflows.nodes import (
    extract_keywords,
    competitor_search,
    analyze_competitors,
    generate_report
)

class StartupState(TypedDict):
    idea: str
    industry: str
    keywords: List[str]
    competitors: List[str]
    analysis: str
    report: str

def build_graph():
    graph = StateGraph(StartupState)

    graph.add_node("extract_keywords", extract_keywords)
    graph.add_node("competitor_search", competitor_search)
    graph.add_node("analyze_competitors", analyze_competitors)
    graph.add_node("generate_report", generate_report)

    graph.set_entry_point("extract_keywords")

    graph.add_edge("extract_keywords", "competitor_search")
    graph.add_edge("competitor_search", "analyze_competitors")
    graph.add_edge("analyze_competitors", "generate_report")

    graph.set_finish_point("generate_report")

    return graph.compile()

graph_app = build_graph()

def run_pipeline(idea: str):
    initial_state = {
        "idea": idea,
        "industry": "",
        "keywords": [],
        "competitors": [],
        "analysis": "",
        "report": ""
    }

    return graph_app.invoke(initial_state)