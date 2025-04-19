# 🐾 Zootopia Animals Web Generator

A Python project for fetching and displaying animal data using the [API Ninjas Animals API](https://api-ninjas.com/api/animals). The data is fetched via an API call and displayed in a neatly formatted HTML page.

## 📦 Project Overview

This tool queries animal information based on a user-provided animal name, processes the returned JSON data, and generates an HTML page showing cards for each animal.

Example:
- You input `"dog"`
- The API returns data about dogs
- Output: a nicely structured `animals.html` file

---

## 🚀 Features

- 🐶 Fetch live animal data from an API
- 🖼️ Generate animal cards in HTML format
- ✅ Display taxonomy, traits, and habitats
- 🔐 Secure use of API key via `.env` file

---

## 📁 Project Structure

```plaintext
Zootopia-API/
│
├── animals_web_generator.py     # Main script
├── data_fetcher.py              # Handles data fetching from the API
├── animals_template.html        # HTML template with placeholder
├── animals.html                 # Final HTML output
├── .env                         # (Not included in repo) API key
├── .gitignore                   # Ignores .env when pushing to GitHub
└── requirements.txt             # Python dependencies

