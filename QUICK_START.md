# 🚀 Quick Start Guide - TalentView Dashboard

## Installation & Setup (5 minutes)

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run the Dashboard
```bash
streamlit run app.py
```

Or use the helper script:
```bash
python run_dashboard.py
```

### Step 3: Load Your Data
1. Open the sidebar (click ☰ if not visible)
2. Enter your CSV file path (default is pre-filled)
3. Click "🔄 Load Data"
4. Wait for "✅ Data Ready" message

### Step 4: Explore!
- Use the navigation radio buttons to switch pages
- Apply filters to analyze specific departments
- Interact with charts and visualizations

---

## 📊 Dashboard Pages

### 1. Workforce Overview
- **View:** Company-wide headcount and demographics
- **Key Metrics:** Headcount, Attrition Rate, Avg Tenure, New Hires
- **Charts:** Department breakdown, Gender/Age/Marital Status distributions

### 2. Attrition Analysis  
- **View:** Turnover trends and drivers
- **Key Metrics:** Separations, Attrition Rate, Avg Tenure of Leavers
- **Charts:** Monthly trends, Separation reasons, **Key Influencers AI analysis**

### 3. Hiring Analysis
- **View:** Recruitment metrics and pipeline
- **Key Metrics:** Time-to-Hire (Avg/Median/Min/Max)
- **Charts:** Time-to-Hire distribution, Department comparison, Hiring funnel

---

## 🔍 Key Features

### Interactive Filtering
- **Department:** Filter by Sales, R&D, HR, etc.
- **Job Role:** Filter by specific roles (updates based on department)
- **Clear Filters:** Reset all filters with one click

### AI-Powered Insights
- **Key Influencers:** Automatically identifies top factors driving attrition
- **Impact Scores:** Shows correlation strength
- **Direction:** Indicates if factor increases or decreases attrition

### Responsive Design
- Works on desktop, tablet, and mobile
- Interactive charts with hover details
- Professional, clean interface

---

## 💡 Example Use Cases

### Use Case 1: Identify High Attrition Department
1. Go to **Attrition Analysis** page
2. Filter by **Department: Engineering**
3. See attrition rate (e.g., 30%)
4. Check **Key Influencers** to see why (e.g., Salary, Promotion)

### Use Case 2: Analyze Hiring Efficiency
1. Go to **Hiring Analysis** page
2. View **Time-to-Hire** metrics
3. Check **Hiring Pipeline** funnel
4. Identify bottlenecks (e.g., low Interview → Offer conversion)

### Use Case 3: Workforce Demographics
1. Go to **Workforce Overview** page
2. View **Demographics** section
3. Analyze Gender, Age, and Marital Status distributions
4. Compare across departments using filters

---

## 🐛 Troubleshooting

### "Data not loading"
- ✅ Check CSV file path is correct
- ✅ Ensure file exists and is accessible
- ✅ Verify CSV has required columns (see README.md)

### "Charts not showing"
- ✅ Make sure data loaded successfully (check sidebar)
- ✅ Clear filters if they exclude all data
- ✅ Refresh the page

### "Module not found"
- ✅ Run: `pip install -r requirements.txt`
- ✅ Check Python version (3.8+)

---

## 📁 Project Structure

```
pricing_analysis/
├── app.py                 # Main application (START HERE)
├── data_preparation.py    # Data modeling
├── dax_measures.py       # Calculations
├── pages/
│   ├── workforce_overview.py
│   ├── attrition_analysis.py
│   └── hiring_analysis.py
├── requirements.txt      # Dependencies
└── README.md            # Full documentation
```

---

## 🎯 Next Steps

1. **Customize:** Modify charts and metrics for your needs
2. **Extend:** Add new pages or visualizations
3. **Deploy:** Share with your team (Streamlit Cloud, Docker, etc.)
4. **Integrate:** Connect to real HRIS/ATS systems

---

## 📚 Documentation

- **README.md** - Complete project documentation
- **PROJECT_GUIDE.md** - Technical details and Power BI mapping
- **Code comments** - Inline documentation

---

**Need Help?** Check the full README.md for detailed information.

**Ready to go?** Run `streamlit run app.py` and start exploring! 🚀

