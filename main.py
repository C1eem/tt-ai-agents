from langgraph.graph import StateGraph, MessagesState, START, END


def trend_finder_agent(state: MessagesState):
    print("trend_finder_agent activated")
    return {"messages": state["messages"] + [{"role": "assistant", "content": "Analysis completed"}]}


def main():
    builder = StateGraph(MessagesState)
    builder.add_node("trend_finder", trend_finder_agent)
    builder.add_edge(START, "trend_finder")
    builder.add_edge("trend_finder", END)

    graph = builder.compile()
    state = {"messages": []}
    result = graph.invoke(state)
    print("Finished with result:", result)


if __name__ == "__main__":
    main()