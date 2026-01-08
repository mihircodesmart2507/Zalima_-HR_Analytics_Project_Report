# TalentView Project Guide

## 📖 Project Overview

This guide provides detailed information about the TalentView HR Dashboard project, including how it maps to Power BI concepts and the week-by-week development plan.

---

## 🔄 Power BI to Python Mapping

### Data Modeling

| Power BI Concept | Python Equivalent | File |
|-----------------|-------------------|------|
| Power Query | `data_preparation.py` | Data transformation and cleaning |
| Data Model | `HRDataModel` class | Object-oriented data structure |
| Dimension Tables (dEmployee, dDepartment) | `df_department`, `df_demographics` | Pandas DataFrames |
| Fact Tables (fHeadcount, fSeparations) | `f_headcount`, `f_separations` | Pandas DataFrames |
| Relationships | DataFrame merges | `.merge()` operations |

### DAX Measures

| Power BI DAX | Python Function | Description |
|--------------|-----------------|-------------|
| `COUNTROWS(dEmployee)` | `calculate_headcount()` | Total active employees |
| `COUNTROWS(FILTER(...))` | `calculate_new_hires()` | New employees |
| `COUNTROWS(fSeparations)` | `calculate_separations()` | Employees who left |
| `DIVIDE([Separations], [Headcount]) * 100` | `calculate_attrition_rate()` | Attrition percentage |
| `AVERAGE(dEmployee[YearsAtCompany])` | `calculate_avg_tenure()` | Average tenure |

### Visualizations

| Power BI Visual | Python/Streamlit Equivalent | Library |
|----------------|----------------------------|---------|
| KPI Cards | `st.metric()` | Streamlit |
| Bar Chart | `px.bar()` | Plotly |
| Line Chart | `px.line()` | Plotly |
| Donut Chart | `px.pie(hole=0.4)` | Plotly |
| Waterfall Chart | `go.Bar()` (horizontal) | Plotly |
| Funnel Chart | `go.Funnel()` | Plotly |
| Key Influencers | Correlation analysis | Pandas/NumPy |

---

## 📅 Week-by-Week Development Plan

### Week 1: Data Modeling & Overview ✅

**Data Modeling Tasks:**
- ✅ Data ingestion from CSV
- ✅ Data cleaning and type conversion
- ✅ PII anonymization (EmployeeNumber hashing)
- ✅ Dimension table creation (Department, Demographics)
- ✅ Fact table creation (Headcount snapshots, Separations)

**Visualization Tasks:**
- ✅ Workforce Overview page
- ✅ KPI cards (Headcount, Attrition Rate, Avg Tenure, New Hires)
- ✅ Headcount by Department bar chart
- ✅ Demographic donut charts (Gender, Age, Marital Status)

**Deliverables:**
- `data_preparation.py` - Complete data model
- `pages/workforce_overview.py` - Overview dashboard page

---

### Week 2: Attrition Analysis ✅

**Data Modeling Tasks:**
- ✅ Core DAX measures implementation
- ✅ Separation reason inference logic
- ✅ Monthly attrition trend simulation

**Visualization Tasks:**
- ✅ Attrition Analysis page
- ✅ Attrition Rate by Month line chart
- ✅ Separations by Reason waterfall chart
- ✅ Filtering system (Department, Job Role, Tenure)

**Deliverables:**
- `dax_measures.py` - All core measures
- `pages/attrition_analysis.py` - Attrition dashboard page
- Filtering functionality in main app

---

### Week 3: Advanced Analytics ✅

**Data Modeling Tasks:**
- ✅ Rolling 12-month attrition rate calculation
- ✅ Key Influencers correlation analysis
- ✅ Time-to-Hire metrics simulation
- ✅ Hiring Pipeline funnel data

**Visualization Tasks:**
- ✅ Key Influencers AI visual
- ✅ Hiring Analysis page
- ✅ Time-to-Hire distribution and metrics
- ✅ Hiring Pipeline funnel chart

**Deliverables:**
- `pages/hiring_analysis.py` - Hiring dashboard page
- Key Influencers analysis in attrition page

---

### Week 4: Polish & Documentation ✅

**Tasks:**
- ✅ Complete dashboard integration
- ✅ Navigation system
- ✅ Comprehensive README
- ✅ Project documentation
- ⏳ Row-Level Security (RLS) - *Power BI Service feature*

**Note on RLS:**
Row-Level Security is a Power BI Service feature that restricts data access based on user roles. In this Python implementation:
- Filters provide similar functionality for analysis
- Full RLS would require user authentication system
- Can be implemented with Streamlit-Authenticator or similar

**Deliverables:**
- `app.py` - Complete main application
- `README.md` - Comprehensive documentation
- `PROJECT_GUIDE.md` - This file
- `requirements.txt` - Dependencies

---

## 🎯 Key Features Implementation

### 1. Data Model Architecture

```
HRDataModel
├── df_employee (dEmployee)
│   └── Employee records with all attributes
├── df_department (dDepartment)
│   └── Department dimension table
├── df_demographics (dDemographics)
│   └── Demographic dimension table
├── f_headcount (fHeadcount)
│   └── Monthly headcount snapshots
└── f_separations (fSeparations)
    └── Employee separation records
```

### 2. DAX Measures Implementation

All measures support filtering through the `filters` parameter:

```python
# Example usage
measures = DAXMeasures(data_model)
headcount = measures.calculate_headcount({'Department': 'Sales'})
attrition_rate = measures.calculate_attrition_rate({'Department': 'Engineering'})
```

### 3. Key Influencers Algorithm

The Key Influencers analysis uses correlation analysis:

1. Convert Attrition to binary (Yes=1, No=0)
2. Calculate correlation with numeric factors
3. Sort by absolute correlation value
4. Determine direction (increases/decreases)
5. Return top N influencers

This mimics Power BI's Key Influencers visual which uses machine learning.

### 4. Filtering System

Filters are stored in `st.session_state.filters` and applied to:
- All DAX measures
- All visualizations
- All data queries

Filter types:
- **Department**: Dropdown selection
- **Job Role**: Dependent on Department
- **Tenure**: Range selection (future enhancement)

---

## 🔍 Use Case Walkthrough

### Scenario: Engineering Department High Attrition

1. **Open Dashboard**
   - User loads data from CSV
   - Dashboard displays company-wide metrics

2. **Identify Problem**
   - Workforce Overview shows 15% overall attrition
   - User navigates to Attrition Analysis page

3. **Filter by Department**
   - Select "Engineering" from Department filter
   - Dashboard updates to show Engineering-specific metrics

4. **Discover Issue**
   - Attrition Rate shows 30% for Engineering
   - This is double the company average

5. **Analyze Key Influencers**
   - Key Influencers visual shows:
     - Top factor: "MonthlyIncome" (25% impact)
     - Second factor: "YearsSinceLastPromotion" (18% impact)
   - Both factors "Increase" attrition

6. **Take Action**
   - Review compensation for Engineering roles
   - Implement promotion pathways
   - Create retention strategy

---

## 📊 Data Flow

```
CSV File
  ↓
HRDataModel.load_data()
  ↓
HRDataModel.clean_data()
  ↓
HRDataModel.anonymize_pii()
  ↓
Dimension Tables (Department, Demographics)
  ↓
Fact Tables (Headcount, Separations)
  ↓
DAXMeasures (calculations)
  ↓
Streamlit Pages (visualizations)
  ↓
Interactive Dashboard
```

---

## 🛠️ Technical Decisions

### Why Streamlit?
- Rapid development for data apps
- Built-in interactivity
- Easy deployment
- Python-native (matches data processing)

### Why Plotly?
- Interactive charts
- Professional appearance
- Export capabilities
- Wide chart type support

### Why Pandas?
- Industry standard for data manipulation
- Efficient for analytics
- Easy filtering and aggregation
- Compatible with all libraries

---

## 🚀 Deployment Options

### Local Development
```bash
streamlit run app.py
```

### Streamlit Cloud
1. Push to GitHub
2. Connect to Streamlit Cloud
3. Deploy automatically

### Docker
```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["streamlit", "run", "app.py", "--server.port=8501"]
```

### Power BI Service Alternative
For production Power BI deployment:
1. Use Power BI Desktop with same data model
2. Recreate DAX measures
3. Recreate visualizations
4. Publish to Power BI Service
5. Configure RLS roles

---

## 📝 Notes

### Simulated Data
Some features use simulated data:
- Monthly headcount snapshots (would come from HRIS)
- Time-to-Hire metrics (would come from ATS)
- Hiring Pipeline (would come from ATS)

In production, these would connect to actual systems.

### Performance
- Data is cached using `@st.cache_data`
- Large datasets may need optimization
- Consider data sampling for very large files

### Extensibility
The architecture supports:
- Additional data sources
- More DAX measures
- New dashboard pages
- Custom visualizations
- API integrations

---

## ✅ Project Completion Checklist

- [x] Data modeling complete
- [x] DAX measures implemented
- [x] Workforce Overview page
- [x] Attrition Analysis page
- [x] Hiring Analysis page
- [x] Filtering system
- [x] Key Influencers analysis
- [x] Documentation complete
- [ ] RLS implementation (Power BI Service)
- [ ] Production deployment

---

**Last Updated:** 2024

