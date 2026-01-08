# 📦 Installation & Setup Guide

## Quick Installation (5 minutes)

### Step 1: Extract Files
Extract the `TalentView_HR_Dashboard.zip` file to your desired location.

### Step 2: Open Terminal/Command Prompt
Navigate to the extracted folder:
```bash
cd TalentView_HR_Dashboard
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

**Required packages:**
- streamlit >= 1.28.0
- pandas >= 2.0.0
- numpy >= 1.24.0
- plotly >= 5.17.0

### Step 4: Run the Dashboard
```bash
streamlit run app.py
```

Or use the helper script:
```bash
python run_dashboard.py
```

### Step 5: Access Dashboard
- The dashboard will automatically open in your browser
- Default URL: `http://localhost:8501`
- If it doesn't open automatically, navigate to the URL shown in the terminal

---

## 📋 Prerequisites

- **Python 3.8 or higher** (Python 3.9+ recommended)
- **pip** package manager
- **Web browser** (Chrome, Firefox, Edge, Safari)

---

## 🔧 Troubleshooting

### Issue: "pip: command not found"
**Solution:** Install Python from python.org and ensure "Add Python to PATH" is checked during installation.

### Issue: "ModuleNotFoundError"
**Solution:** 
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Issue: "Port 8501 already in use"
**Solution:** 
- Close other Streamlit apps
- Or use a different port: `streamlit run app.py --server.port 8502`

### Issue: Dashboard doesn't load data
**Solution:**
- Check CSV file path is correct
- Ensure CSV file exists and is accessible
- Verify CSV has required columns (see README.md)

---

## 📁 Project Files

```
TalentView_HR_Dashboard/
├── app.py                 # Main application ⭐ START HERE
├── data_preparation.py    # Data modeling
├── dax_measures.py       # Calculations
├── run_dashboard.py      # Helper script
├── requirements.txt      # Dependencies
├── pages/                # Dashboard pages
│   ├── workforce_overview.py
│   ├── attrition_analysis.py
│   └── hiring_analysis.py
└── Documentation/
    ├── README.md
    ├── QUICK_START.md
    └── PROJECT_GUIDE.md
```

---

## 🚀 First Run

1. **Start the application:**
   ```bash
   streamlit run app.py
   ```

2. **Load your data:**
   - In the sidebar, enter your CSV file path
   - Click "🔄 Load Data"
   - Wait for "✅ Data Ready" message

3. **Explore the dashboard:**
   - Navigate between pages using sidebar radio buttons
   - Apply filters (Department, Job Role)
   - Interact with charts and visualizations

---

## 📊 Data Requirements

Your CSV file should contain these columns (minimum):
- `EmployeeNumber` - Unique identifier
- `Attrition` - "Yes" or "No"
- `Department` - Department name
- `JobRole` - Job title
- `Age`, `Gender`, `MaritalStatus` - Demographics
- `MonthlyIncome` - Salary
- `YearsAtCompany` - Tenure
- `JobSatisfaction`, `EnvironmentSatisfaction`, `WorkLifeBalance` - Satisfaction scores

See `README.md` for complete column list.

---

## ✅ Verification

After installation, verify everything works:

1. **Check Python version:**
   ```bash
   python --version
   ```
   Should show Python 3.8 or higher

2. **Check packages:**
   ```bash
   pip list | findstr streamlit
   pip list | findstr pandas
   pip list | findstr plotly
   ```

3. **Run test:**
   ```bash
   streamlit run app.py
   ```
   Should open dashboard without errors

---

## 🆘 Need Help?

1. Check `QUICK_START.md` for quick reference
2. Read `README.md` for complete documentation
3. Review `PROJECT_GUIDE.md` for technical details
4. Check error messages in terminal/console

---

## 🎯 Next Steps

After successful installation:
1. Load your HR data CSV file
2. Explore the three dashboard pages
3. Use filters to analyze specific departments
4. Review Key Influencers for attrition insights
5. Export insights for your team

---

**Ready to go?** Run `streamlit run app.py` and start exploring! 🚀

