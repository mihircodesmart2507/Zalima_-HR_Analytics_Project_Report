"""
Data Preparation Module (Power Query Equivalent)
Handles data ingestion, cleaning, anonymization, and data modeling
"""
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

class HRDataModel:
    """Main data model class for HR data preparation"""
    
    def __init__(self, data_path):
        self.data_path = data_path
        self.df_employee = None
        self.df_department = None
        self.df_demographics = None
        self.f_headcount = None
        self.f_separations = None
        self.df_merged = None
        
    def load_data(self):
        """Load and ingest raw HR data"""
        print("Loading HR data...")
        self.df_employee = pd.read_csv(self.data_path)
        print(f"Loaded {len(self.df_employee)} employee records")
        return self.df_employee
    
    def anonymize_pii(self):
        """Anonymize Personally Identifiable Information"""
        print("Anonymizing PII...")
        if 'EmployeeNumber' in self.df_employee.columns:
            # Hash employee numbers for anonymization
            self.df_employee['EmployeeID'] = self.df_employee['EmployeeNumber'].apply(
                lambda x: hash(str(x)) % 100000
            )
        return self.df_employee
    
    def create_department_table(self):
        """Create dimension table for departments"""
        print("Creating department dimension table...")
        departments = self.df_employee['Department'].unique()
        self.df_department = pd.DataFrame({
            'DepartmentID': range(1, len(departments) + 1),
            'DepartmentName': departments
        })
        return self.df_department
    
    def create_demographics_table(self):
        """Create demographics dimension table"""
        print("Creating demographics dimension table...")
        demo_cols = ['Gender', 'MaritalStatus', 'EducationField', 'Age']
        available_cols = ['EmployeeNumber'] + [col for col in demo_cols if col in self.df_employee.columns]
        self.df_demographics = self.df_employee[available_cols].copy()
        
        # Add age groups
        if 'Age' in self.df_demographics.columns:
            self.df_demographics['AgeGroup'] = pd.cut(
                self.df_demographics['Age'],
                bins=[0, 25, 35, 45, 55, 100],
                labels=['18-25', '26-35', '36-45', '46-55', '55+']
            )
        
        return self.df_demographics
    
    def create_headcount_snapshot(self):
        """Create monthly headcount fact table (simulated)"""
        print("Creating headcount snapshots...")
        # Simulate monthly snapshots for the past 12 months
        months = pd.date_range(end=datetime.now(), periods=12, freq='M')
        
        headcount_data = []
        for month in months:
            # Simulate headcount (in real scenario, this would come from HRIS)
            # For now, we'll use current data and simulate some variation
            base_count = len(self.df_employee)
            # Simulate some variation
            count = base_count + np.random.randint(-20, 20)
            headcount_data.append({
                'Month': month,
                'Headcount': max(count, base_count * 0.9)  # Ensure reasonable values
            })
        
        self.f_headcount = pd.DataFrame(headcount_data)
        return self.f_headcount
    
    def create_separations_table(self):
        """Create separations fact table"""
        print("Creating separations fact table...")
        # Filter employees who left (Attrition = Yes)
        separations = self.df_employee[self.df_employee['Attrition'] == 'Yes'].copy()
        
        # Simulate separation dates (in real scenario, this would be actual dates)
        # Use YearsAtCompany to estimate when they left
        separations['SeparationDate'] = pd.to_datetime('2024-01-01') - pd.to_timedelta(
            separations['YearsAtCompany'] * 365, unit='D'
        )
        
        # Add separation reasons (inferred from data)
        separations['SeparationReason'] = separations.apply(self._infer_separation_reason, axis=1)
        
        self.f_separations = separations[[
            'EmployeeNumber', 'Department', 'JobRole', 'SeparationDate', 
            'SeparationReason', 'MonthlyIncome', 'YearsAtCompany'
        ]].copy()
        
        return self.f_separations
    
    def _infer_separation_reason(self, row):
        """Infer separation reason based on employee attributes"""
        reasons = []
        if row['JobSatisfaction'] <= 2:
            reasons.append('Low Job Satisfaction')
        if row['EnvironmentSatisfaction'] <= 2:
            reasons.append('Poor Work Environment')
        if row['WorkLifeBalance'] <= 2:
            reasons.append('Work-Life Balance')
        if row['MonthlyIncome'] < self.df_employee['MonthlyIncome'].median():
            reasons.append('Compensation')
        if row['OverTime'] == 'Yes':
            reasons.append('Overtime Concerns')
        if row['YearsSinceLastPromotion'] > 5:
            reasons.append('Limited Growth')
        
        return reasons[0] if reasons else 'Other'
    
    def merge_tables(self):
        """Merge all tables for analysis"""
        print("Merging tables...")
        self.df_merged = self.df_employee.copy()
        
        # Add department info
        if self.df_department is not None:
            self.df_merged = self.df_merged.merge(
                self.df_department,
                left_on='Department',
                right_on='DepartmentName',
                how='left'
            )
        
        return self.df_merged
    
    def clean_data(self):
        """Clean and prepare data"""
        print("Cleaning data...")
        # Remove constant columns
        constant_cols = [col for col in self.df_employee.columns 
                        if self.df_employee[col].nunique() <= 1]
        if constant_cols:
            self.df_employee = self.df_employee.drop(columns=constant_cols)
        
        # Ensure proper data types
        numeric_cols = ['Age', 'MonthlyIncome', 'YearsAtCompany', 'TotalWorkingYears']
        for col in numeric_cols:
            if col in self.df_employee.columns:
                self.df_employee[col] = pd.to_numeric(self.df_employee[col], errors='coerce')
        
        return self.df_employee
    
    def prepare_complete_model(self):
        """Run complete data preparation pipeline"""
        print("="*70)
        print("HR DATA MODEL PREPARATION")
        print("="*70)
        
        # Load data
        self.load_data()
        
        # Clean data
        self.clean_data()
        
        # Anonymize PII
        self.anonymize_pii()
        
        # Create dimension tables
        self.create_department_table()
        self.create_demographics_table()
        
        # Create fact tables
        self.create_headcount_snapshot()
        self.create_separations_table()
        
        # Merge tables
        self.merge_tables()
        
        print("\n" + "="*70)
        print("DATA MODEL PREPARATION COMPLETE")
        print("="*70)
        print(f"Employee Records: {len(self.df_employee)}")
        print(f"Departments: {len(self.df_department)}")
        print(f"Separations: {len(self.f_separations)}")
        print("="*70)
        
        return {
            'employee': self.df_employee,
            'department': self.df_department,
            'demographics': self.df_demographics,
            'headcount': self.f_headcount,
            'separations': self.f_separations,
            'merged': self.df_merged
        }

