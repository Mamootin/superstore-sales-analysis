# 🏬 Superstore Sales Analysis

> End‑to‑end data analysis and profit prediction using Python, pandas, scikit‑learn, and Streamlit.

---

## 📋 Project Steps (Checklist)

- [ ] **Set up Python 3.12** and install PyCharm (Community Edition).
- [ ] **Create project folder** and internal directory structure (`data/`, `src/`, `notebooks/`, `reports/`, `app/`, `tests/`).
- [ ] **Move raw data** (`Superstore.xlsx`) into `data/raw/`.
- [ ] **Create and activate a virtual environment** (`venv`).
- [ ] **Install required packages** (`pandas`, `numpy`, `matplotlib`, `seaborn`, `jupyter`, `openpyxl`, `scikit‑learn`, `joblib`, `streamlit`, `plotly`, `pytest`).
- [ ] **Generate `requirements.txt`** with exact versions.
- [ ] **Initialise Git** and create a `.gitignore` (exclude `venv/`, `__pycache__/`, `.idea/`, etc.).
- [ ] **Make the first commit** and push to a new GitHub repository.
- [ ] **Stage A – Data Loading & Cleaning**  
  - Write `load_orders()` and `clean_orders()` in `src/data_prep.py`.  
  - Explore the data in a Jupyter notebook (`notebooks/01_load_explore.ipynb`).  
  - Save cleaned data as `data/processed/orders_clean.csv`.  
  - Generate key charts (sales by region, profit by category, monthly trends).  
  - Write findings in `reports/EDA_findings.md`.  
  - Commit and push.
- [ ] **Stage B – Machine Learning**  
  - Build features (`src/features.py`) with one‑hot encoding.  
  - Train a baseline linear regression model and a Random Forest regressor (`src/model.py`).  
  - Compare performance (MAE, R²) and check feature importance.  
  - Save the best model (`app/profit_model.joblib`).  
  - Document results in `reports/model_summary.md`.  
  - Commit and push.
- [ ] **Stage C – Streamlit Dashboard**  
  - Build `app/dashboard.py` with KPIs, filters, and charts.  
  - Run locally with `streamlit run app/dashboard.py`.  
  - (Optional) Deploy to Streamlit Cloud.  
  - Commit and push.
- [ ] **Final Polish**  
  - Write a comprehensive `README.md` (this file) with setup instructions and findings.  
  - Add a few unit tests (`tests/test_data_prep.py`) and run them with `pytest`.  
  - Update `requirements.txt` with final package versions.  
  - Tag the release (`git tag v1.0`) and push tags.

---

## 🚀 How to Run

```bash
# Clone the repo
git clone https://github.com/<your-username>/superstore-sales-analysis.git
cd superstore-sales-analysis

# Create and activate a virtual environment
python3.12 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the dashboard
streamlit run app/dashboard.py
