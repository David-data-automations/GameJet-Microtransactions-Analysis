# GameJet-Microtransactions-Analysis
GameJet is a blockchain gaming and NFT platform powered by the JET token.

**Overview**: Data analysis project focused on understanding player behavior and spending patterns in a Free-to-Play mobile game to optimize revenue strategy.

The core objective was to segment the user base into distinct purchasing personas and quantify their financial contribution, ultimately informing the product team on high-leverage marketing and game design decisions.

---

## 🔑 Key Insights & Business Impact

* **Pareto Principle Validation**: The analysis confirmed a heavily skewed monetization model, where **Whales** (users spending over \$100) and **Dolphins** (users spending \$20-\$100) collectively generate over 80% of total revenue, despite making up less than 5% of the total user base.
* **Conversion Criticality**: **Day 0 conversion** is the most critical period. A significant portion of first purchases occur on the same day as the user installs the app, proving that the **onboarding experience** is the single most important factor for maximizing lifetime value (LTV).
* **Engagement Skew**: The distribution of sessions per user is heavily skewed, with a small group of highly engaged "power users" driving activity. Metrics like the median are required to accurately gauge the typical player experience.

---

## 🛠️ Technical Stack & Project Components

* **Methodology**: User segmentation using complex SQL `CASE` statements, calculation of aggregate revenue using `SUM()`, and time-series analysis on days-to-first-purchase using date arithmetic and `MIN()` functions.
* **Tools**: SQL (PostgreSQL/BigQuery dialect - Joins, CTEs, CASE), Python (Pandas for data verification, Matplotlib for visualization), NumPy for data simulation.
* **Data**: Three simulated tables (`users`, `sessions`, `iaps`) mimicking a real-world F2P game monetization schema.

| File / Folder | Description |
| :--- | :--- |
| `sql/` | Contains the cleaned, commented SQL queries for Segmentation, Revenue, and Time-to-First-Purchase analysis. |
| `generate_data.py` | Python script to programmatically create the three runnable, inter-related CSV files, ensuring reproducibility. |
| `requirements.txt` | Lists all necessary Python dependencies (Pandas, Matplotlib, etc.). |
| `notebooks/` | (Future extension) Will contain the Python notebook to run the SQL results and generate visual summaries (e.g., persona revenue pie chart). |

## ▶️ How to Run Locally

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/your-username/gamejet-monetization-analysis.git](https://github.com/your-username/gamejet-monetization-analysis.git)
    cd gamejet-monetization-analysis
    ```
2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Generate Data Files:**
    ```bash
    python generate_data.py
    ```
4.  **Run SQL:** The queries in the `sql/` folder can be run against the generated CSVs in a local PostgreSQL/SQLite environment or directly executed within a Pandas workflow for analysis.
---

extracting the SQL from the Traffic Collisions PDF?**
