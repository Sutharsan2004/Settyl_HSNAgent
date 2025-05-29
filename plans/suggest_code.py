from plan import Plan
from data_loader import load_hsn_data

class SuggestCode(Plan):
    def __init__(self):
        super().__init__()
        self.data = load_hsn_data()

    def execute(self, goal):
        query = goal['parameters'].get("query", "").lower()

        matches = self.data[self.data['Description'].str.lower().str.contains(query)]

        if matches.empty:
            return {"status": "No match found"}

        return {
            "status": "Suggestions",
            "results": matches[['HSNCode', 'Description']].to_dict(orient="records")
        }
