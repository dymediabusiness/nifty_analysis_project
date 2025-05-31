# Nifty 50 Data Analysis and Automation

## Overview
This project fetches historical Nifty 50 data using the `yfinance` API, calculates key technical indicators, visualizes them, and saves them in Excel and PNG formats. It's an ideal starter for Python automation and algo-trading scripts.

## Features
- Fetches daily Nifty 50 data from 2020 to 2024
- Calculates:
  - 20-day, 50-day, and 200-day moving averages
  - Daily returns and cumulative returns
- Visualizes:
  - Price vs. moving averages
  - Daily return histogram
  - Cumulative return plot
- Saves:
  - Raw data to Excel (`data/nifty_data_with_ma.xlsx`)
  - Summary statistics to Excel (`summary/summary_stats.xlsx`)
  - All graphs as PNGs (`graphs/`)

## Installation
```bash
pip install -r requirements.txt
