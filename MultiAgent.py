#Crewai with multi agent with llm
#pip install crewai


import os
from crewai import Agent, Task,Crew,LLM,Process

#gemini ai api key
# GEMINI_API_KEY="AIzaSyB2BeopG3jnTWsmlGwv6BPYqCGX-cZLw0Y"

os.environ["GEMINI_API_KEY"] = "AIzaSyB2BeopG3jnTWsmlGwv6BPYqCGX-cZLw0Y"

#Gemini Ai LLM
llm=LLM(
    model="google/gemini-2.5-flash",
    temperature=0.4
)

#user input for the task
#Agent 1 Event Planner

plannerAgent1=Agent(
    role="Wedding Planner",
    goal="Write a wedding plan for 100 guests with a budget of $30,000",
    backstory="wedding planner with 10 years of experience in planning weddings. You have a keen eye for detail and a passion for creating unforgettable wedding experiences. Your expertise includes venue selection, catering, decoration, and entertainment coordination.",
    verbose=True,
    llm=llm
)



event_name="destination wedding"
guests=100
date="2026-05-25"
budget=30000
venue="royal plaza hotel"

PlanningTask1=Task(
    description=f"""
Plan event:
{event_name}
Guests:{guests}
Date:{date}
Venue:{venue}
Budget:{budget}


Give:
1.Theme suggestions
2.Activity ideas
3.Food recommendations
4.venue decoration ideas
5.Entertainment suggestions
6. Wedding favors ideas
7. Timeline for the wedding day
""",
expected_output="Graceful and elegant wedding plan with theme, activities, food, and decoration ideas.",
agent=plannerAgent1
)

#crew pipline
crew=Crew(
    agents=[plannerAgent1],
    tasks=[PlanningTask1],
    name="Wedding Planning Crew",
    process=Process.sequential,
    verbose=True
)

#run the crew
print("Starting the crew...")
results=crew.kickoff()
print("Crew completed. Results:")
print(results)