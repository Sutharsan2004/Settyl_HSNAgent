# Explanation video link
https://drive.google.com/file/d/1Wz37uq1VcJ25UR3xxEeA0HfVz65wl3ty/view?usp=sharing 


# HSN Code Validation Agent using ADK Framework

This agent validates and suggests Harmonized System Nomenclature (HSN) codes based on an Excel master dataset, using a modular agent design inspired by Google ADK.

## ✅ Features
- Validates user-entered HSN codes (format + existence)
- Suggests relevant HSN codes for product descriptions
- Uses modular Plan-based architecture (Validation & Suggestion)

## 📂 Project Structure
- `agent.py` – Base Agent class
- `plan.py` – Base Plan class
- `hsn_agent.py` – Custom HSNAgent combining Plans
- `main.py` – Entry point (demo/test)
- `data_loader.py` – Loads Excel dataset
- `plans/` – Contains validation and suggestion logic

## 🛠 How to Run
```bash
python main.py
