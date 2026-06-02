# LangGraph Workflow Visualization
# pip install streamlit langgraph langchain-groq graphviz

import os
import time
import streamlit as st

from graphviz import Digraph
from typing import Annotated, TypedDict

from langgraph.graph import START, END, StateGraph
from langgraph.graph.message import add_messages

from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="LangGraph Workflow Visualization",
    layout="centered"
)

st.title("🤖 LangGraph Workflow Visualization")

# ---------------- API KEY ----------------

api_key = "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"

if api_key:
    os.environ["GROQ_API_KEY"] = api_key

# ---------------- STATE ----------------

class State(TypedDict):
    message: Annotated[list, add_messages]

# ---------------- LLM ----------------

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7
)

# ---------------- NODES ----------------

# User Prompt Node
def user_prompt_node(state: State):

    return {
        "message": state["message"]
    }

# Prompt Analyzer Node
def prompt_analyzer_node(state: State):

    user_message = state["message"][-1]

    analyzed_prompt = HumanMessage(
        content=f"Analyze this prompt and answer clearly: {user_message.content}"
    )

    return {
        "message": [analyzed_prompt]
    }

# AI Assistant Node
def ai_assistant_node(state: State):

    return {
        "message": state["message"]
    }

# LLM Node
def llm_node(state: State):

    response = llm.invoke(state["message"])

    return {
        "message": [response]
    }

# LangChain Node
def langchain_node(state: State):

    return {
        "message": state["message"]
    }

# Output Node
def output_node(state: State):

    return {
        "message": state["message"]
    }

# ---------------- LANGGRAPH WORKFLOW ----------------

workflow = StateGraph(State)

workflow.add_node("User Prompt", user_prompt_node)
workflow.add_node("Prompt Analyzer", prompt_analyzer_node)
workflow.add_node("AI Assistant", ai_assistant_node)
workflow.add_node("LLM", llm_node)
workflow.add_node("LangChain", langchain_node)
workflow.add_node("Output", output_node)

# ---------------- EDGES ----------------

workflow.add_edge(START, "User Prompt")
workflow.add_edge("User Prompt", "Prompt Analyzer")
workflow.add_edge("Prompt Analyzer", "AI Assistant")
workflow.add_edge("AI Assistant", "LLM")
workflow.add_edge("LLM", "LangChain")
workflow.add_edge("LangChain", "Output")
workflow.add_edge("Output", END)

app = workflow.compile()

# ---------------- GRAPH VISUALIZATION ----------------

def draw_graph(active_node=None):

    graph = Digraph()

    nodes = [
        "START",
        "User Prompt",
        "Prompt Analyzer",
        "AI Assistant",
        "LLM",
        "LangChain",
        "Output",
        "END"
    ]

    for node in nodes:

        color = "lightgray"

        if active_node == node:
            color = "yellow"

        if node == "START":
            color = "green" if active_node == "START" else "lightgray"

        if node == "END":
            color = "blue" if active_node == "END" else "lightgray"

        shape = "box"

        if node in ["START", "END"]:
            shape = "ellipse"

        graph.node(
            node,
            style="filled",
            fillcolor=color,
            shape=shape
        )

    # edges
    graph.edge("START", "User Prompt")
    graph.edge("User Prompt", "Prompt Analyzer")
    graph.edge("Prompt Analyzer", "AI Assistant")
    graph.edge("AI Assistant", "LLM")
    graph.edge("LLM", "LangChain")
    graph.edge("LangChain", "Output")
    graph.edge("Output", "END")

    return graph

# ---------------- UI ----------------

st.subheader("LangGraph Workflow")

graph_placeholder = st.empty()

graph_placeholder.graphviz_chart(draw_graph())

# ---------------- USER INPUT ----------------

user_input = st.text_input(
    "Enter your prompt:"
)

# ---------------- RUN WORKFLOW ----------------

if st.button("Run Workflow"):

    if user_input:

        status = st.empty()

        # START
        status.warning("Starting Workflow...")
        graph_placeholder.graphviz_chart(draw_graph("START"))
        time.sleep(1)

        # USER PROMPT
        status.info("Executing User Prompt Node...")
        graph_placeholder.graphviz_chart(draw_graph("User Prompt"))
        time.sleep(1)

        # PROMPT ANALYZER
        status.info("Executing Prompt Analyzer Node...")
        graph_placeholder.graphviz_chart(draw_graph("Prompt Analyzer"))
        time.sleep(1)

        # AI ASSISTANT
        status.info("Executing AI Assistant Node...")
        graph_placeholder.graphviz_chart(draw_graph("AI Assistant"))
        time.sleep(1)

        # LLM
        status.info("Executing LLM Node...")
        graph_placeholder.graphviz_chart(draw_graph("LLM"))
        time.sleep(1)

        # LANGCHAIN
        status.info("Executing LangChain Node...")
        graph_placeholder.graphviz_chart(draw_graph("LangChain"))
        time.sleep(1)

        # OUTPUT
        status.info("Generating Output...")
        graph_placeholder.graphviz_chart(draw_graph("Output"))
        time.sleep(1)

        # INPUT STATE
        input_state = {
            "message": [
                HumanMessage(content=user_input)
            ]
        }

        # RUN APP
        results = app.invoke(input_state)

        # END
        status.success("Workflow Completed!")
        graph_placeholder.graphviz_chart(draw_graph("END"))

        st.subheader("Final Output")

        st.write(results["message"][-1].content)

    else:
        st.warning("Please enter a prompt.")