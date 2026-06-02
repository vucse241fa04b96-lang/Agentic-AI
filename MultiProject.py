#Crewai with multi agent with llm
#pip install crewai


import os
from crewai import Agent, Task,Crew,LLM,Process

# gemini ai api key
GEMINI_API_KEY="AIzaSyB2BeopG3jnTWsmlGwv6BPYqCGX-cZLw0Y"

os.environ["GEMINI_API_KEY"] = "AIzaSyB2BeopG3jnTWsmlGwv6BPYqCGX-cZLw0Y"
# os.environ["GROQ_API_KEY"] = "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"
#Gemini Ai LLM
llm=LLM(
    model="google/gemini-2.5-flash",
    temperature=0.4
)

# #Groq Ai LLM
# llm=LLM(
#     model="groq 3.3-70b-versatile",
#     temperature=0.4
# )

#user input for the task
#Agent 1 Event Planner

plannerAgent1=Agent(
    role="Event Planner",
    goal="Plan a birthday party for a 10 year old child",
    backstory="You are an experienced event planner specializing in children's parties. You have a knack for creating fun and memorable events that cater to the interests of young children. Your expertise includes selecting themes, organizing activities, and coordinating with vendors to ensure a seamless experience.",
    verbose=True,
    llm=llm
)
#Agent 2 Budget Manager
budgetAgent2=Agent(
    role="Budget Manager",
    goal="Manage the budget for the birthday party and ensure that all expenses are within the allocated budget.",
    backstory="You are a meticulous budget manager with a strong background in financial planning. You excel at tracking expenses and ensuring that all costs remain within the allocated budget.",
    verbose=True,
    llm=llm
)

#Agent3 Risk Analyser
riskAgent3=Agent(
    role="Risk Analyser",
    goal="Find the Possible event Problems and Identify potential risks and challenges associated with the birthday party planning and provide strategies to mitigate them.",
    backstory="Expert in Risk Managements and You are a proactive risk analyst with experience in event planning. You have a keen eye for identifying potential issues and developing effective strategies to mitigate them, ensuring the success of the event.",
    verbose=True,
    llm=llm
)

event_name="Superhero Birthday Bash"
guests=20
date="2026-05-25"
budget=50000
venue="Local Community Center"

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
""",
expected_output="Simple and creative event plan with theme, activities, food, and decoration ideas.",
agent=plannerAgent1
)

budget_task=Task(
    description=f"""
    Budget:{budget}
    Check if budget is sufficient for the planned event and provide suggestions for cost-saving if necessary.
    Manage the budget for the event:
1.Create a detailed budget breakdown for the event, including all expected expenses such as venue rental, catering, decorations, entertainment, and any additional costs.,
2.Track expenses and ensure that all costs remain within the allocated budget.,
3.provide recommendations for cost-saving measures if the planned expenses exceed the budget.
""",
expected_output="Detailed budget breakdown and cost-saving recommendations if necessary.",
agent=budgetAgent2

)

risk_task3=Task(
    description=f"""
    Analyze Event Risks:

    Identify potential risks and challenges associated with the birthday party planning and provide strategies to mitigate them. Consider factors such as weather conditions, vendor reliability, guest safety, and any other relevant risks that could impact the success of the event.
    Find the possible event problems:
1.Assess the logistics of the event, including transportation, parking, and accessibility for guests.,
2.Evaluate the safety measures in place for the event, such as emergency exits, first aid availability, and crowd control.,
3.weather contigencies if the event is outdoors, including backup plans for inclement weather.,
4.agent=riskAgent3
""",
expected_output="Comprehensive risk analysis with identified risks and mitigation strategies.",
agent=riskAgent3   
)
#crew pipline
crew=Crew(
    agents=[plannerAgent1, budgetAgent2, riskAgent3],
    tasks=[PlanningTask1, budget_task, risk_task3],
    name="Birthday Party Planning Crew",
    process=Process.sequential,
    verbose=True
)

#run the crew
print("Starting the crew...")
results=crew.kickoff()
print("Crew completed. Results:")
print(results)