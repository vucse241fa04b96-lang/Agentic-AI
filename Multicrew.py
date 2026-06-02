# Multi-Agent AI Research System using CrewAI
# pip install crewai

import os
from crewai import Agent, Task, Crew, LLM, Process

# SET API KEY
os.environ["GEMINI_API_KEY"] = "AIzaSyB2BeopG3jnTWsmlGwv6BPYqCGX-cZLw0Y"


# LLM CONFIGURATION
llm = LLM(
    model="google/gemini-2.5-flash",
    temperature=0.4
)


# USER INPUT
topic = "Artificial Intelligence in Healthcare"

# AGENT 1 : RESEARCH AGENT
research_agent = Agent(
    role="Research Specialist",
    goal="Collect accurate and detailed information about the given topic.",
    backstory="""
    You are an expert researcher with strong knowledge in gathering
    factual, updated, and structured information from reliable sources.
    You specialize in finding trends, technologies, statistics, and key insights.
    """,
    verbose=True,
    llm=llm
)


# AGENT 2 : ANALYSIS AGENT
analysis_agent = Agent(
    role="Data Analyst",
    goal="Analyze the collected research data and generate meaningful insights.",
    backstory="""
    You are a skilled analyst capable of studying research findings,
    identifying patterns, advantages, disadvantages, opportunities,
    challenges, and future scope.
    """,
    verbose=True,
    llm=llm
)


# AGENT 3 : REVIEW AGENT
review_agent = Agent(
    role="Review Expert",
    goal="Review and improve the final report for quality, accuracy, and clarity.",
    backstory="""
    You are a professional content reviewer and editor.
    Your expertise is in checking reports for correctness,
    readability, grammar, and professional presentation.
    """,
    verbose=True,
    llm=llm
)


# TASK 1 : RESEARCH TASK
research_task = Task(
    description=f"""
    Conduct detailed research on the topic:
    "{topic}"

    Include:
    1. Introduction
    2. Latest trends
    3. Major applications
    4. Advantages
    5. Challenges
    6. Real-world examples
    7. Future scope
    
    Provide well-structured research findings.
    """,

    expected_output="""
    A detailed research report containing accurate information,
    trends, applications, advantages, challenges, and future scope.
    """,

    agent=research_agent
)


# TASK 2 : ANALYSIS TASK
analysis_task = Task(
    description=f"""
    Analyze the research findings on:
    "{topic}"

    Perform:
    1. Trend analysis
    2. SWOT analysis
    3. Risk analysis
    4. Market impact analysis
    5. Future growth predictions

    Generate meaningful insights and conclusions.
    """,

    expected_output="""
    A comprehensive analytical report with insights,
    comparisons, risks, opportunities, and conclusions.
    """,

    agent=analysis_agent
)


# TASK 3 : REVIEW TASK
review_task = Task(
    description=f"""
    Review the complete research and analysis report on:
    "{topic}"

    Check for:
    1. Accuracy
    2. Clarity
    3. Grammar
    4. Professional formatting
    5. Completeness

    Improve the final report and provide a polished version.
    """,

    expected_output="""
    A final polished and professionally reviewed report
    with improved readability and accuracy.
    """,

    agent=review_agent
)


# CREATE CREW
crew = Crew(
    agents=[
        research_agent,
        analysis_agent,
        review_agent
    ],

    tasks=[
        research_task,
        analysis_task,
        review_task
    ],

    name="AI Research Crew",

    process=Process.sequential,

    verbose=True
)


# RUN CREW
print("Starting AI Research Crew...\n")

result = crew.kickoff()

print("\nCrew Execution Completed!\n")
print("Final Result:\n")
print(result)