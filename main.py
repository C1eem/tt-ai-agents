from langgraph.graph import StateGraph, MessagesState, START, END
from langgraph.types import Command
from typing import Literal

def trend_finder_agent(state: MessagesState) -> Command[END]:
    print("trend_finder_agent activated")
    return Command(goto=END)

def main():
    builder = StateGraph(MessagesState)
    builder.add_node("trend_finder", trend_finder_agent)
    builder.add_edge(START, "trend_finder")
    graph = builder.compile()
    state = {"messages": []}
    result = graph.invoke(state)
    print("Finished with result:", result)

if __name__ == "__main__":
    main()
