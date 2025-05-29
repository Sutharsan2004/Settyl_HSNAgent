from hsn_agent import HSNAgent

if __name__ == "__main__":
    agent = HSNAgent()

    # ✅ Test 1: Validation
    goal_validate = {
        "name": "validate",
        "parameters": {"code": "01011010"}  # Use a valid or test code from your dataset
    }
    result = agent.handle_goal(goal_validate)
    print("Validation Result:", result)

    # ✅ Test 2: Suggestion
    goal_suggest = {
        "name": "suggest",
        "parameters": {"query": "live horses"}  # Use a description from your dataset
    }
    result = agent.handle_goal(goal_suggest)
    print("Suggestion Result:", result)
