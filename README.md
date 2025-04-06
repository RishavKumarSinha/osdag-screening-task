
# Osdag IITB Screening Task Submission 🎯

This repository contains the submission for the Osdag IITB Screening Task, comprising:

- 📈 **Task 1:** Shear Force Diagram (SFD) & Bending Moment Diagram (BMD) using PyPlot.
- 🏗️ **Task 2:** CAD model of a Laced Compound Column using PythonOCC.

---

## 📌 Objective

**Osdag** is a free and open-source software used for the design and detailing of steel structures such as buildings and bridges.

This task showcases visualization of structural data and 3D modeling capabilities relevant to Osdag’s design environment.

---

## 🛠️ Setup Instructions

Before running the code, ensure you have Python 3.8+ installed.

### 1. Clone the repository

```bash
git clone https://github.com/RishavKumarSinha/osdag-screening-task.git
cd osdag-screening-task
```

### 2. Create and activate virtual environment

```bash
python -m venv osdag_env
osdag_env\Scripts\activate  # On Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available, install manually:

```bash
pip install pandas matplotlib openpyxl pythonocc-core
```

---

## ✅ Task Descriptions

### 🔹 Task 1: SFD & BMD Plotter

**File:** `SFD_BMD_Plotter.py`

This script reads values from an Excel file (`data/SFS_Screening_SFDBMD.xlsx`) and generates:

- A **Shear Force Diagram (SFD)** 📊
- A **Bending Moment Diagram (BMD)** 📈

Using `matplotlib.pyplot` and `pandas` for plotting and data handling.

#### ▶️ To Run:

```bash
python SFD_BMD_Plotter.py
```

---

### 🔹 Task 2: Laced Compound Column CAD Model

**File:** `laced_column.py`

This PythonOCC script generates a 3D CAD model of a **Laced Compound Column**, as per the provided specifications:

- Two I-sections spaced at 450mm
- End battens of 300mm × 10mm
- Diagonal laces (100mm wide × 8mm thick) at ~45° angles

#### ▶️ To Run:

```bash
python laced_column.py
```

The model viewer will open automatically via PythonOCC GUI.

---

## 📹 Video Demonstration

Unlisted video showing both tasks in action:  
🔗 [YouTube Video Link Here](https://youtu.be/oYs9tj6UIV4)

---

## 📄 Report Documentation

A PDF report detailing the code logic, approach, and challenges is included in the repo.

- `Osdag_IITB_Report.pdf`

---

## 🗂️ Submission Package Includes

- Python scripts (`.py`)
- CAD output files (`.step`)
- Excel input files (`.xlsx`)
- Demo video link
- Report PDF
- All source files zipped (`osdag_screening_submission.zip`)

---

## ⚖️ License
All submissions are licensed under:

Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)
🔗 [View License](https://creativecommons.org/licenses/by-sa/4.0/)

---

## 👥 Collaborators

GitHub repo shared with: `osdag-admin` (as collaborator)

---

## 🙌 Acknowledgement

Thanks to the FOSSEE team at IIT Bombay for the opportunity. This task was both a challenge and a learning experience.

---
