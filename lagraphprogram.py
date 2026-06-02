#LangGraph

#pip install langgraph
#pip install langgraph_core


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
    page_title="LangGraph Visualization",
    layout="centered"
)

st.title("🤖 LangGraph Visualization")

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

# ---------------- CHATBOT NODE ----------------

def chatbot_node(state: State):

    user_message = state["message"][-1]

    response = llm.invoke([user_message])

    return {
        "message": [response]
    }

# ---------------- LANGGRAPH WORKFLOW ----------------

workflow = StateGraph(State)

workflow.add_node("Chatbot", chatbot_node)

workflow.add_edge(START, "Chatbot")
workflow.add_edge("Chatbot", END)

app = workflow.compile()

# ---------------- GRAPH VISUALIZATION ----------------

def draw_graph(active_node=None):

    graph = Digraph()

    start_color = "green" if active_node == "START" else "lightgray"
    chatbot_color = "yellow" if active_node == "Chatbot" else "lightgray"
    end_color = "blue" if active_node == "END" else "lightgray"

    graph.node(
        "START",
        style="filled",
        fillcolor=start_color,
        shape="ellipse"
    )

    graph.node(
        "Chatbot",
        style="filled",
        fillcolor=chatbot_color,
        shape="box"
    )

    graph.node(
        "END",
        style="filled",
        fillcolor=end_color,
        shape="ellipse"
    )

    graph.edge("START", "Chatbot")
    graph.edge("Chatbot", "END")

    return graph

# ---------------- UI ----------------

st.subheader("LangGraph Workflow Visualization")

graph_placeholder = st.empty()

graph_placeholder.graphviz_chart(draw_graph())

# ---------------- USER INPUT ----------------

user_input = st.text_input(
    "Enter your message for the chatbot:"
)

# ---------------- RUN WORKFLOW ----------------

if st.button("Run Workflow"):

    if user_input:

        status = st.empty()

        status.warning("Running workflow...")

        graph_placeholder.graphviz_chart(
            draw_graph("START")
        )

        time.sleep(1)

        status.info("Executing Chatbot node...")

        graph_placeholder.graphviz_chart(
            draw_graph("Chatbot")
        )

        input_state = {
            "message": [
                HumanMessage(content=user_input)
            ]
        }

        results = app.invoke(input_state)

        time.sleep(1)

        status.success("Workflow completed!")

        graph_placeholder.graphviz_chart(
            draw_graph("END")
        )

        time.sleep(1)

        st.subheader("Chatbot Response:")

        st.write(results["message"][-1].content)

    else:
        st.warning(
            "Please enter a message to run the workflow."
        )