#Graph Viz
#Digraph 
#pip install graphviz

import streamlit as st
from graphviz import Digraph

def create_graph():
    graph=Digraph()
    graph.node('s','Start')
    graph.node('up','User Prompt')
    graph.node('aa','Ai Agent')
    graph.node('l','LLM Model')
    graph.node('lc','LangChain')
    graph.node('o','Output')
   
    graph.edge('s','up',label="Edge from Start to User Prompt")
    graph.edge('up','aa',label="Edge from User Prompt to Ai Agent") 
    graph.edge('aa','l',label="Edge from Ai Agent to LLM Model")
    graph.edge('l','lc',label="Edge from LLM Model to LangChain")
    graph.edge('lc','o',label="Edge from LangChain to Output")
   
    return graph

def main():
    st.title("Graph Visualization with Graphviz")
    graph=create_graph()
    st.graphviz_chart(graph)
if __name__=="__main__":
    main()

#python -m streamlit run LangGraphprogram.py
