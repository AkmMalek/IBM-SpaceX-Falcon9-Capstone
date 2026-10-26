# SpaceX Falcon 9 — Landing Prediction

**IBM Data Science Professional Certificate · Applied Data Science Capstone**

This project investigates whether historical launch characteristics can help predict the success of a Falcon 9 first-stage landing. The workflow combines Python data processing, SQL, visual analytics, geospatial exploration, an interactive Plotly Dash dashboard, and supervised classification.

## Project at a glance

| Component | Approach | Key output |
| --- | --- | --- |
| Data collection | SpaceX API workflow and historical web scraping | Web scraping dataset: 121 records, 11 columns |
| Data wrangling | pandas, missing-value review and landing labels | 90 labelled launches, 60 successful landings |
| SQL analysis | SQLite analytical queries | Historical SQL dataset: 101 rows |
| Exploratory visualizations | Matplotlib, Seaborn | Trends and comparisons by site, orbit and payload |
| Geospatial analysis | Folium | Launch-site mapping, clustered markers and coastal distance illustration |
| Interactive dashboard | Plotly Dash | Launch-site dropdown, success chart and payload-outcome scatter with range slider |
| Machine learning | Logistic Regression, SVM, Decision Tree, KNN | 83.33% accuracy on a held-out sample of 18 launches for each of the four fitted models |

The datasets used across these labs do not all represent the same observation cohort. Counts and percentages are therefore reported within their respective sources.

## Project files

- **[Final presentation (PDF)](Data%20Science%20Capstone%20Project%20Report.pdf)** — complete findings and presentation slides.
- **[Editable presentation (PPTX)](Data_Science_Capstone_Project_Report.pptx)** — slide deck.
- **[Notebooks](notebooks/)** — eight capstone labs covering collection, wrangling, SQL, visualization, Folium, Dash and machine learning.
- **[Dash application](spacex-dash-app.py)** — standalone interactive web dashboard.
- **[Dashboard screenshots](evidence/dash/)** — captures from the locally executed dashboard.
- **[Results summary](results_summary.csv)** — key statistics and metrics.
- **[Python dependencies](requirements.txt)** — required packages.

## Methodology

1. Collect and prepare historical launch data, identify first-stage landing outcomes and inspect data quality.
2. Explore relationships among launch sites, payload mass, orbit, booster configuration and landing success.
3. Use Folium to map geographic launch-site patterns and Plotly Dash to explore selectable launch and payload subsets.
4. Standardize predictive features, split the dataset into training and test sets, tune four classifiers with cross-validation, and evaluate held-out test accuracy and confusion matrices.

**Interpretation:** The predictive results describe a small, historical teaching dataset. All four evaluated classifiers scored 15/18 (83.33%) on the held-out test set; this does not establish reliable performance on future missions. The original modelling notebook applies scaling before train/test splitting, so a production-style follow-up would move preprocessing inside a cross-validation pipeline and validate on a later independent cohort.

The API collection notebook documents the API-based collection workflow; it is included for reference, but saved execution results are not available in that notebook. The web-scraping notebook contains executed results.

## Run the dashboard

Use a Python environment with JupyterLab or a terminal:

```bash
python -m pip install -r requirements.txt
python spacex-dash-app.py
```

Open the local URL printed by Dash, typically `http://127.0.0.1:8050/`. The application uses `spacex_launch_dash.csv` if available in the working directory or downloads the public IBM teaching dataset if internet access is available.

Alternatively, explore the Dash notebook in JupyterLab. Historical screenshots of the interactive interface are available in `evidence/dash/` without running the server.

## Data and acknowledgments

Course exercise and historical datasets: **IBM Skills Network — Applied Data Science Capstone**. This repository is an educational analysis of historical launches and is not affiliated with SpaceX or intended for operational launch forecasting.
