# Customer Satisfaction by Product Category – Seaborn Barplot

**Analyst Email:** 24f2008507@ds.study.iitm.ac.in  

## Overview

This repository contains a professional Seaborn-based visualization for analyzing **average customer satisfaction scores by product category**. The visualization is designed for executive-facing use cases, including quarterly business reviews, board presentations, and strategic planning documents.

The project is built for **Shanahan Deckow and Conn**, a data-driven customer experience company that transforms raw customer data into actionable insights for business leaders.

---

## Business Context

A major retail client wants to compare customer satisfaction across different product categories to:

- Identify high-performing categories  
- Detect underperforming areas  
- Support data-driven decisions on product strategy and investments  

The client specifically requested a **Seaborn barplot** to ensure a **statistically sound** and **visually polished** representation of average satisfaction scores.

This visualization will feed into:

- Quarterly business review decks  
- Executive and board reports  
- Strategic planning discussions  

---

## Data

The dataset is **synthetic but realistic**, representing customer satisfaction survey responses on a **1–5 scale** across multiple product categories:

- Electronics  
- Home & Kitchen  
- Clothing  
- Beauty & Personal Care  
- Sports & Outdoors  

For each category, multiple customer responses are generated and stored in a pandas DataFrame with the following columns:

- `product_category` – product category name  
- `satisfaction_score` – customer satisfaction score (1–5, continuous)  

The barplot then visualizes the **mean satisfaction score** per product category, with error bars representing 95% confidence intervals.

---

## Visualization Details

The visualization is implemented in **Seaborn** using `sns.barplot()`.

Key characteristics:

- **Chart type:** Barplot (`sns.barplot`)  
- **X-axis:** `product_category`  
- **Y-axis:** `satisfaction_score` (average per category)  
- **Estimator:** Mean satisfaction score (default estimator via NumPy mean)  
- **Error bars:** 95% confidence intervals (`errorbar=("ci", 95)`)  
- **Color palette:** `Blues_d` for a professional, executive-ready look  
- **Style & context:**
  - `sns.set_style("whitegrid")` for clarity and readability  
  - `sns.set_context("talk")` for presentation-sized text  

The resulting figure:

- Clearly compares satisfaction across categories  
- Is easily interpretable by non-technical stakeholders  
- Is publication-ready for slides and reports  

---

## Files in This Repository

- `README.md` – This documentation, including business context and implementation details.  
- `chart.py` – Python script that generates the Seaborn barplot and exports `chart.png`.  
- `chart.png` – The generated barplot image (exactly 512x512 pixels).

---

## How to Run the Script and Generate the Chart

1. Make sure you have Python 3 installed.  
2. Install required libraries (if they are not already installed):

   ```bash
   pip install seaborn matplotlib pandas numpy
