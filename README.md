# Nifty 50 Data Analysis and Automation 📊

## Overview
This project fetches historical Nifty 50 data using the `yfinance` API, calculates key technical indicators, visualizes them, and saves results in Excel and PNG formats. It's designed as a starter for Python automation and algorithmic trading scripts.

---

## 📈 Features

- Fetches daily Nifty 50 data from **2020 to 2024**
- Calculates:
  - 20-day, 50-day, and 200-day moving averages
  - Daily returns and cumulative returns
- Visualizes:
  - Price vs. Moving Averages
  - Daily Return Histogram
  - Cumulative Return Plot
- Saves:
  - Raw data to Excel (`data/nifty_data_with_ma.xlsx`)
  - Summary statistics to Excel (`summary/summary_stats.xlsx`)
  - All graphs as PNGs (`graphs/`)

---

## 🛠️ Installation

1️⃣ Clone the repository:
```bash
git clone https://github.com/your_username/nifty_analysis_project.git
cd nifty_analysis_project
