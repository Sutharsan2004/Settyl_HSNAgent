# hsn_agent.py

from agent import Agent  # This refers to the class from agent.py
from plans.validate_code import ValidateCode
from plans.suggest_code import SuggestCode

class HSNAgent(Agent):
    def __init__(self):
        super().__init__("HSNValidatorAgent")
        self.add_plan("validate", ValidateCode())
        self.add_plan("suggest", SuggestCode())
