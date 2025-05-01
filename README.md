# 📊 Sales Data Analysis Dashboard

This project is a simple interactive dashboard built with **Python**, **Pandas**, **Matplotlib**, and **Streamlit**. It visualizes and analyzes sales data from a CSV file.

---

## 📁 Project Structure

```
sales_data_analysis/
├── analysis/
│   └── dashboard.py           # Streamlit app code
├── data/
│   └── sales_data.csv         # Sample sales data
└── README.md                  # This file
```

---

## ✅ Requirements

Make sure you have Python 3 installed. Then install the required libraries:

```bash
pip install pandas matplotlib streamlit
```

---

## 🚀 How to Run

1. Place your CSV file at:

   ```
   sales_data_analysis/data/sales_data.csv
   ```

2. Run the Streamlit dashboard from the terminal:

   ```bash
  streamlit run "E:\Document\python\sales_data_analysis\analysis\dashboard.py"
   ```

3. The app will open automatically in your browser (e.g. Local URL   : http://localhost:8504
                                                            Network URL : http://192.168.86.240:8504).

---

## 📌 Features

- Filter data by date
- View total sales, average order value, and top-performing region
- Bar chart for regional sales
- Horizontal bar chart for top-selling products
- Line chart of sales over time

---


## 🙋‍♂️ Need Help?

If you run into any errors:
- Make sure the file paths are correct
- Use absolute paths if needed
- Ensure `sales_data.csv` exists and is formatted correctly

---
