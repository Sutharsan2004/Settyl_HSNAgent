# agent.py

class Agent:
    def __init__(self, name):
        self.name = name
        self.plans = {}

    def add_plan(self, goal_name, plan_obj):
        self.plans[goal_name] = plan_obj

    def handle_goal(self, goal):
        goal_name = goal['name']
        if goal_name in self.plans:
            return self.plans[goal_name].execute(goal)
        return {"status": "error", "message": "Unknown goal"}
