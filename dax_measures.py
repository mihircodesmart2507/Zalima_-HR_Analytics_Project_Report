"""
DAX Measures Module
Python equivalent of Power BI DAX measures for HR analytics
"""
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

class DAXMeasures:
    """DAX-like measures for HR analytics"""
    
    def __init__(self, data_model):
        self.data_model = data_model
        self.df = data_model['merged']
        self.separations = data_model['separations']
        self.headcount = data_model['headcount']
        
    def calculate_headcount(self, filters=None):
        """
        Calculate total headcount
        Equivalent to: Headcount = COUNTROWS(dEmployee)
        """
        df_filtered = self._apply_filters(self.df, filters)
        return len(df_filtered[df_filtered['Attrition'] == 'No'])
    
    def calculate_new_hires(self, filters=None, period_months=12):
        """
        Calculate new hires in the last N months
        Equivalent to: New Hires = COUNTROWS(FILTER(dEmployee, YearsAtCompany <= 1))
        """
        df_filtered = self._apply_filters(self.df, filters)
        # Consider employees with less than 1 year as new hires
        new_hires = df_filtered[df_filtered['YearsAtCompany'] < 1]
        return len(new_hires)
    
    def calculate_separations(self, filters=None, period_months=12):
        """
        Calculate separations in the last N months
        Equivalent to: Separations = COUNTROWS(fSeparations)
        """
        if filters:
            separations_filtered = self._apply_filters(self.separations, filters)
        else:
            separations_filtered = self.separations
        
        # Filter by period if needed
        if period_months < 12:
            cutoff_date = datetime.now() - timedelta(days=period_months * 30)
            separations_filtered = separations_filtered[
                separations_filtered['SeparationDate'] >= cutoff_date
            ]
        
        return len(separations_filtered)
    
    def calculate_attrition_rate(self, filters=None, period_months=12):
        """
        Calculate attrition rate (rolling 12 months)
        Equivalent to: Attrition Rate % = DIVIDE([Separations], [Headcount], 0) * 100
        """
        separations = self.calculate_separations(filters, period_months)
        headcount = self.calculate_headcount(filters)
        
        if headcount == 0:
            return 0.0
        
        # Annualize the rate
        rate = (separations / headcount) * 100
        return round(rate, 2)
    
    def calculate_avg_tenure(self, filters=None):
        """
        Calculate average tenure
        Equivalent to: Avg. Tenure = AVERAGE(dEmployee[YearsAtCompany])
        """
        df_filtered = self._apply_filters(self.df, filters)
        df_active = df_filtered[df_filtered['Attrition'] == 'No']
        
        if len(df_active) == 0:
            return 0.0
        
        return round(df_active['YearsAtCompany'].mean(), 2)
    
    def calculate_headcount_by_department(self, filters=None):
        """Calculate headcount grouped by department"""
        df_filtered = self._apply_filters(self.df, filters)
        df_active = df_filtered[df_filtered['Attrition'] == 'No']
        
        return df_active.groupby('Department').size().to_dict()
    
    def calculate_attrition_by_department(self, filters=None):
        """Calculate attrition rate by department"""
        df_filtered = self._apply_filters(self.df, filters)
        
        results = {}
        for dept in df_filtered['Department'].unique():
            dept_filters = {**filters, 'Department': dept} if filters else {'Department': dept}
            results[dept] = self.calculate_attrition_rate(dept_filters)
        
        return results
    
    def calculate_attrition_by_month(self, filters=None):
        """Calculate attrition rate by month (simulated)"""
        # Simulate monthly attrition data
        months = pd.date_range(end=datetime.now(), periods=12, freq='M')
        monthly_rates = []
        
        for month in months:
            # Simulate variation in attrition
            base_rate = self.calculate_attrition_rate(filters)
            variation = np.random.uniform(-2, 2)
            monthly_rates.append({
                'Month': month.strftime('%Y-%m'),
                'AttritionRate': max(0, round(base_rate + variation, 2))
            })
        
        return pd.DataFrame(monthly_rates)
    
    def calculate_separations_by_reason(self, filters=None):
        """Calculate separations grouped by reason"""
        if filters:
            separations_filtered = self._apply_filters(self.separations, filters)
        else:
            separations_filtered = self.separations
        
        return separations_filtered['SeparationReason'].value_counts().to_dict()
    
    def calculate_demographics(self, filters=None, category='Gender'):
        """Calculate demographic distribution"""
        df_filtered = self._apply_filters(self.df, filters)
        df_active = df_filtered[df_filtered['Attrition'] == 'No']
        
        if category == 'Gender':
            if 'Gender' in df_active.columns:
                return df_active['Gender'].value_counts().to_dict()
        elif category == 'AgeGroup':
            demo = self.data_model.get('demographics')
            if demo is not None and 'AgeGroup' in demo.columns:
                df_with_demo = df_active.merge(
                    demo[['EmployeeNumber', 'AgeGroup']],
                    on='EmployeeNumber',
                    how='left'
                )
                return df_with_demo['AgeGroup'].value_counts().to_dict()
        elif category == 'MaritalStatus':
            if 'MaritalStatus' in df_active.columns:
                return df_active['MaritalStatus'].value_counts().to_dict()
        
        return {}
    
    def calculate_time_to_hire(self, filters=None):
        """
        Calculate time-to-hire metrics (simulated)
        In real scenario, this would come from ATS data
        """
        # Simulate time-to-hire data
        avg_time_to_hire = np.random.uniform(25, 45)  # days
        return {
            'Average': round(avg_time_to_hire, 1),
            'Median': round(avg_time_to_hire - 5, 1),
            'Min': round(avg_time_to_hire - 15, 1),
            'Max': round(avg_time_to_hire + 15, 1)
        }
    
    def calculate_hiring_pipeline(self, filters=None):
        """
        Calculate hiring pipeline funnel (simulated)
        In real scenario, this would come from ATS data
        """
        # Simulate pipeline data
        base_count = 1000
        return {
            'Applied': base_count,
            'Screened': int(base_count * 0.6),
            'Interviewed': int(base_count * 0.3),
            'Offered': int(base_count * 0.15),
            'Hired': int(base_count * 0.1)
        }
    
    def identify_key_influencers(self, filters=None, top_n=5):
        """
        Identify key influencers of attrition using correlation analysis
        Equivalent to Power BI Key Influencers visual
        """
        df_filtered = self._apply_filters(self.df, filters)
        
        # Convert attrition to binary
        df_filtered['AttritionBinary'] = (df_filtered['Attrition'] == 'Yes').astype(int)
        
        # Select numeric columns for correlation
        numeric_cols = [
            'Age', 'MonthlyIncome', 'YearsAtCompany', 'TotalWorkingYears',
            'JobSatisfaction', 'EnvironmentSatisfaction', 'WorkLifeBalance',
            'YearsSinceLastPromotion', 'DistanceFromHome', 'PercentSalaryHike'
        ]
        
        # Calculate correlations
        correlations = {}
        for col in numeric_cols:
            if col in df_filtered.columns:
                corr = df_filtered[col].corr(df_filtered['AttritionBinary'])
                if not np.isnan(corr):
                    correlations[col] = abs(corr)
        
        # Sort by absolute correlation
        sorted_corrs = sorted(correlations.items(), key=lambda x: x[1], reverse=True)
        
        # Get top influencers
        top_influencers = []
        for col, corr_value in sorted_corrs[:top_n]:
            # Determine direction
            actual_corr = df_filtered[col].corr(df_filtered['AttritionBinary'])
            direction = "Increases" if actual_corr > 0 else "Decreases"
            
            top_influencers.append({
                'Factor': col,
                'Impact': round(corr_value * 100, 2),
                'Direction': direction
            })
        
        return pd.DataFrame(top_influencers)
    
    def _apply_filters(self, df, filters):
        """Apply filters to dataframe"""
        if filters is None:
            return df
        
        df_filtered = df.copy()
        for key, value in filters.items():
            if key in df_filtered.columns and value is not None:
                if isinstance(value, list):
                    df_filtered = df_filtered[df_filtered[key].isin(value)]
                else:
                    df_filtered = df_filtered[df_filtered[key] == value]
        
        return df_filtered

