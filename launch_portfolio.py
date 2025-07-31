#!/usr/bin/env python3
"""
Portfolio Launcher - Double-click to run
This script launches the JHU Bioinformatics Portfolio GUI
"""

import sys
import os
import subprocess
from pathlib import Path

def main():
    """Launch the Portfolio GUI"""
    try:
        # Get script directory
        script_dir = Path(__file__).parent
        gui_script = script_dir / "portfolio_launcher.py"
        
        if not gui_script.exists():
            print("Error: Portfolio launcher not found!")
            print(f"Looking for: {gui_script}")
            input("Press Enter to exit...")
            return
        
        # Launch the GUI
        print("Launching JHU Bioinformatics Portfolio...")
        subprocess.run([sys.executable, str(gui_script)])
        
    except Exception as e:
        print(f"Error launching portfolio: {e}")
        input("Press Enter to exit...")

if __name__ == "__main__":
    main()