"""
Quick start script for TalentView Dashboard
"""
import subprocess
import sys
import os

def main():
    """Run the Streamlit dashboard"""
    print("="*70)
    print("Starting TalentView HR Dashboard...")
    print("="*70)
    print("\nThe dashboard will open in your default browser.")
    print("If it doesn't, navigate to: http://localhost:8501")
    print("\nPress Ctrl+C to stop the server.")
    print("="*70)
    
    try:
        # Run streamlit
        subprocess.run([sys.executable, "-m", "streamlit", "run", "app.py"])
    except KeyboardInterrupt:
        print("\n\nDashboard stopped.")
    except Exception as e:
        print(f"\nError starting dashboard: {e}")
        print("\nMake sure you have installed all requirements:")
        print("  pip install -r requirements.txt")

if __name__ == "__main__":
    main()

