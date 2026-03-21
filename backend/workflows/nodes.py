def extract_keywords(state):
    idea = state["idea"]

    # simple placeholder logic
    return {
        "industry": "technology",
        "keywords": idea.lower().split()[:5]
    }


def competitor_search(state):
    keywords = state["keywords"]

    # mock competitors
    competitors = [f"{kw}_competitor" for kw in keywords]

    return {
        "competitors": competitors
    }


def analyze_competitors(state):
    competitors = state["competitors"]

    analysis = f"Found {len(competitors)} competitors in this space."

    return {
        "analysis": analysis
    }


def generate_report(state):
    return {
        "report": f"""
Idea: {state['idea']}
Industry: {state['industry']}
Competitors: {state['competitors']}
Analysis: {state['analysis']}
"""
    }