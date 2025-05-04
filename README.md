# Excel to Oracle SQL Schema Converter

A simple Python script that converts Excel spreadsheets into Oracle-compatible SQL schema and insert statements.

---

## 📂 Features

- Automatically generates `CREATE TABLE` statements from each sheet in the Excel file.
- Infers column types (`NUMBER`, `VARCHAR(n)`, `DATE`) based on actual cell values.
- Inserts data using `INSERT INTO` statements.
- Handles multiple sheets and commits each sheet's data.

---

## 🛠️ Requirements

- Python 3.x
- pandas

Install pandas if not already installed:

```bash
pip install pandas
```

▶️ How to Run
Place your Excel file (e.g., Employee Data.xlsx) in the same folder as the script.

Update the filename in the script or pass it dynamically if modified.

Run the script:

```bash
python excel_to_oracle_schema.py
```

The output SQL file (e.g., data.sql) will be created in the same directory.

📄 Example
If your Excel has a sheet called Employees with columns like ID, Name, and Join Date, the script will generate:

```bash
CREATE TABLE employees (ID NUMBER, Name VARCHAR(50), Join Date DATE);
INSERT INTO employees (ID, Name, Join Date) VALUES (1, 'Ali', TO_DATE('15-02-2023', 'DD-MM-YYYY'));
COMMIT;
```
