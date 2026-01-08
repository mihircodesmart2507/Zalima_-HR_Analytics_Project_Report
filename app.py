"""
TalentView - HR Attrition & Workforce Dashboard
Main Streamlit Application
"""
import streamlit as st
import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from data_preparation import HRDataModel
from dax_measures import DAXMeasures
from pages.workforce_overview import render_workforce_overview
from pages.attrition_analysis import render_attrition_analysis
from pages.hiring_analysis import render_hiring_analysis

# Page configuration
st.set_page_config(
    page_title="TalentView - HR Dashboard",
    page_icon="👥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        padding: 1rem 0;
    }
    .stMetric {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'data_model' not in st.session_state:
    st.session_state.data_model = None
    st.session_state.measures = None
    st.session_state.data_loaded = False
    st.session_state.filters = {}

@st.cache_data
def load_data_model(data_path):
    """Load and prepare data model (cached)"""
    model = HRDataModel(data_path)
    data_dict = model.prepare_complete_model()
    measures = DAXMeasures(data_dict)
    return data_dict, measures

def main():
    """Main application function"""
    
    # Header
    st.markdown('<div class="main-header">👥 TalentView - HR Attrition & Workforce Dashboard</div>', 
                unsafe_allow_html=True)
    st.markdown("---")
    
    # Sidebar
    with st.sidebar:
        st.header("⚙️ Configuration")
        
        # Data loading
        st.subheader("Data Source")
        data_path = st.text_input(
            "CSV File Path",
            value=r"c:\Users\Asus\Downloads\WA_Fn-UseC_-HR-Employee-Attrition.csv",
            help="Enter the path to your HR data CSV file"
        )
        
        if st.button("🔄 Load Data", type="primary"):
            with st.spinner("Loading and preparing data..."):
                try:
                    data_model, measures = load_data_model(data_path)
                    st.session_state.data_model = data_model
                    st.session_state.measures = measures
                    st.session_state.data_loaded = True
                    st.success("✅ Data loaded successfully!")
                except Exception as e:
                    st.error(f"❌ Error loading data: {str(e)}")
                    st.session_state.data_loaded = False
        
        if st.session_state.data_loaded:
            st.success("✅ Data Ready")
        
        st.markdown("---")
        
        # Filters
        st.subheader("🔍 Filters")
        
        if st.session_state.data_loaded:
            data_model = st.session_state.data_model
            
            # Department filter
            departments = ['All'] + list(data_model['merged']['Department'].unique())
            selected_dept = st.selectbox(
                "Department",
                departments,
                index=0
            )
            
            if selected_dept != 'All':
                st.session_state.filters['Department'] = selected_dept
            elif 'Department' in st.session_state.filters:
                del st.session_state.filters['Department']
            
            # Job Role filter
            if 'Department' in st.session_state.filters:
                dept_data = data_model['merged'][
                    data_model['merged']['Department'] == st.session_state.filters['Department']
                ]
                job_roles = ['All'] + list(dept_data['JobRole'].unique())
            else:
                job_roles = ['All'] + list(data_model['merged']['JobRole'].unique())
            
            selected_role = st.selectbox(
                "Job Role",
                job_roles,
                index=0
            )
            
            if selected_role != 'All':
                st.session_state.filters['JobRole'] = selected_role
            elif 'JobRole' in st.session_state.filters:
                del st.session_state.filters['JobRole']
            
            # Tenure filter
            tenure_options = ['All', '0-2 years', '3-5 years', '6-10 years', '10+ years']
            selected_tenure = st.selectbox(
                "Tenure Range",
                tenure_options,
                index=0
            )
            
            # Note: Tenure filtering would be implemented in measures if needed
            
            # Clear filters button
            if st.button("Clear All Filters"):
                st.session_state.filters = {}
                st.rerun()
        
        st.markdown("---")
        
        # Navigation
        st.subheader("📑 Navigation")
        page = st.radio(
            "Select Page",
            ["Workforce Overview", "Attrition Analysis", "Hiring Analysis"],
            index=0
        )
        
        st.markdown("---")
        
        # Info
        st.info("""
        **TalentView Dashboard**  
        Comprehensive HR analytics for workforce insights, attrition analysis, and hiring metrics.
        """)
    
    # Main content area
    if not st.session_state.data_loaded:
        st.warning("⚠️ Please load data from the sidebar to begin.")
        st.info("""
        ### Getting Started
        
        1. Enter the path to your HR data CSV file in the sidebar
        2. Click "Load Data" to prepare the data model
        3. Use filters to analyze specific departments or roles
        4. Navigate between pages to explore different insights
        
        ### Project Overview
        
        This dashboard provides:
        - **Workforce Overview**: Headcount, demographics, and key metrics
        - **Attrition Analysis**: Turnover trends, reasons, and key influencers
        - **Hiring Analysis**: Time-to-hire and pipeline metrics
        """)
    else:
        # Render selected page
        data_model = st.session_state.data_model
        measures = st.session_state.measures
        
        if page == "Workforce Overview":
            render_workforce_overview(data_model, measures)
        elif page == "Attrition Analysis":
            render_attrition_analysis(data_model, measures)
        elif page == "Hiring Analysis":
            render_hiring_analysis(data_model, measures)

if __name__ == "__main__":
    main()

