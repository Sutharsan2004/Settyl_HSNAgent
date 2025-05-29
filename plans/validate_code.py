from plan import Plan
from data_loader import load_hsn_data

class ValidateCode(Plan):
    def __init__(self):
        super().__init__()
        self.data = load_hsn_data()

    def execute(self, goal):
        code = goal['parameters'].get("code")

        if not code.isdigit():
            return {"status": "Invalid", "reason": "Code must be numeric."}

        if code in self.data['HSNCode'].values:
            desc = self.data[self.data['HSNCode'] == code]['Description'].values[0]
            return {"status": "Valid", "description": desc}
        else:
            return {"status": "Invalid", "reason": "Code not found"}
