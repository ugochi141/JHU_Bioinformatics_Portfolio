#!/usr/bin/env python3
"""
JHU Bioinformatics Portfolio Launcher
A GUI application to run and demonstrate all bioinformatics assignments and projects
"""

import sys
import os
import subprocess
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, filedialog
from pathlib import Path
import threading
import webbrowser
from datetime import datetime

class BioinformaticsPortfolioLauncher:
    def __init__(self, root):
        self.root = root
        self.root.title("JHU Bioinformatics Portfolio Launcher")
        self.root.geometry("900x700")
        
        # Get the portfolio directory
        self.portfolio_dir = Path(__file__).parent
        
        # Create the main UI
        self.create_widgets()
        self.load_assignments()
    
    def create_widgets(self):
        """Create the main GUI widgets"""
        
        # Header
        header_frame = ttk.Frame(self.root)
        header_frame.pack(fill='x', padx=10, pady=5)
        
        title_label = ttk.Label(header_frame, text="Johns Hopkins Bioinformatics Portfolio", 
                               font=('Arial', 16, 'bold'))
        title_label.pack()
        
        author_label = ttk.Label(header_frame, text="by Ugochi Ndubuisi", 
                                font=('Arial', 12))
        author_label.pack()
        
        # Create notebook for tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Tab 1: Assignments
        assignments_frame = ttk.Frame(self.notebook)
        self.notebook.add(assignments_frame, text="Programming Assignments")
        self.create_assignments_tab(assignments_frame)
        
        # Tab 2: Bioinformatics Analysis
        analysis_frame = ttk.Frame(self.notebook)
        self.notebook.add(analysis_frame, text="Bioinformatics Analysis")
        self.create_analysis_tab(analysis_frame)
        
        # Tab 3: Tools & Utilities
        tools_frame = ttk.Frame(self.notebook)
        self.notebook.add(tools_frame, text="Tools & Utilities")
        self.create_tools_tab(tools_frame)
        
        # Tab 4: Portfolio Overview
        overview_frame = ttk.Frame(self.notebook)
        self.notebook.add(overview_frame, text="Portfolio Overview")
        self.create_overview_tab(overview_frame)
    
    def create_assignments_tab(self, parent):
        """Create the assignments tab"""
        
        # Left panel - Assignment list
        left_frame = ttk.Frame(parent)
        left_frame.pack(side='left', fill='both', expand=True, padx=5, pady=5)
        
        ttk.Label(left_frame, text="Programming Assignments", font=('Arial', 12, 'bold')).pack(anchor='w')
        
        # Assignment listbox
        list_frame = ttk.Frame(left_frame)
        list_frame.pack(fill='both', expand=True, pady=5)
        
        self.assignment_listbox = tk.Listbox(list_frame, height=10)
        self.assignment_listbox.pack(side='left', fill='both', expand=True)
        self.assignment_listbox.bind('<<ListboxSelect>>', self.on_assignment_select)
        
        scrollbar = ttk.Scrollbar(list_frame, orient='vertical', command=self.assignment_listbox.yview)
        scrollbar.pack(side='right', fill='y')
        self.assignment_listbox.config(yscrollcommand=scrollbar.set)
        
        # Buttons
        button_frame = ttk.Frame(left_frame)
        button_frame.pack(fill='x', pady=5)
        
        ttk.Button(button_frame, text="Run Assignment", 
                  command=self.run_selected_assignment).pack(side='left', padx=2)
        ttk.Button(button_frame, text="View Code", 
                  command=self.view_assignment_code).pack(side='left', padx=2)
        ttk.Button(button_frame, text="View README", 
                  command=self.view_assignment_readme).pack(side='left', padx=2)
        
        # Right panel - Output
        right_frame = ttk.Frame(parent)
        right_frame.pack(side='right', fill='both', expand=True, padx=5, pady=5)
        
        ttk.Label(right_frame, text="Output / Code View", font=('Arial', 12, 'bold')).pack(anchor='w')
        
        self.output_text = scrolledtext.ScrolledText(right_frame, height=25, width=50)
        self.output_text.pack(fill='both', expand=True, pady=5)
    
    def create_analysis_tab(self, parent):
        """Create the bioinformatics analysis tab"""
        
        main_frame = ttk.Frame(parent)
        main_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        ttk.Label(main_frame, text="Bioinformatics Analysis Projects", 
                 font=('Arial', 12, 'bold')).pack(anchor='w', pady=5)
        
        # Analysis projects
        projects = [
            {
                "name": "NGS Variant Analysis",
                "description": "Next-generation sequencing data analysis with variant calling and annotation",
                "path": "Assignments/BioinformaticsAnalysis/NGS_analysis",
                "files": ["huD3FFCB_variant.vcf", "parse_vep.py", "NGS_Report_huD3FFCB.md"]
            },
            {
                "name": "Huntington Gene Analysis", 
                "description": "Analysis of HTT gene associated with Huntington's disease",
                "path": "Assignments/BioinformaticsAnalysis/gene_analysis/huntington_analysis",
                "files": ["HTT_biomart_results.txt", "HTT_complete_results.txt"]
            },
            {
                "name": "Genomics Tools",
                "description": "Various genomics tools and utilities for sequence analysis",
                "path": "Assignments/BioinformaticsAnalysis/genomics_tools", 
                "files": ["DNASequence.py", "gene_lookup.py"]
            }
        ]
        
        for project in projects:
            project_frame = ttk.LabelFrame(main_frame, text=project["name"], padding=10)
            project_frame.pack(fill='x', pady=5)
            
            ttk.Label(project_frame, text=project["description"]).pack(anchor='w')
            
            button_frame = ttk.Frame(project_frame)
            button_frame.pack(fill='x', pady=5)
            
            ttk.Button(button_frame, text="Open Folder", 
                      command=lambda p=project["path"]: self.open_folder(p)).pack(side='left', padx=2)
            ttk.Button(button_frame, text="View Files", 
                      command=lambda p=project: self.view_project_files(p)).pack(side='left', padx=2)
    
    def create_tools_tab(self, parent):
        """Create the tools and utilities tab"""
        
        main_frame = ttk.Frame(parent)
        main_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        ttk.Label(main_frame, text="Bioinformatics Tools & Utilities", 
                 font=('Arial', 12, 'bold')).pack(anchor='w', pady=5)
        
        # DNA Sequence Analyzer
        dna_frame = ttk.LabelFrame(main_frame, text="DNA Sequence Analyzer", padding=10)
        dna_frame.pack(fill='x', pady=5)
        
        ttk.Label(dna_frame, text="Analyze DNA sequences for GC content, ORFs, and more").pack(anchor='w')
        
        seq_input_frame = ttk.Frame(dna_frame)
        seq_input_frame.pack(fill='x', pady=5)
        
        ttk.Label(seq_input_frame, text="DNA Sequence:").pack(side='left')
        self.dna_sequence_var = tk.StringVar(value="ATCGATCGATCG")
        ttk.Entry(seq_input_frame, textvariable=self.dna_sequence_var, width=30).pack(side='left', padx=5)
        ttk.Button(seq_input_frame, text="Analyze", command=self.analyze_dna_sequence).pack(side='left', padx=5)
        
        # File Processing Tools
        file_frame = ttk.LabelFrame(main_frame, text="File Processing Tools", padding=10)
        file_frame.pack(fill='x', pady=5)
        
        ttk.Label(file_frame, text="Process FASTQ, FASTA, and other bioinformatics file formats").pack(anchor='w')
        
        file_button_frame = ttk.Frame(file_frame)
        file_button_frame.pack(fill='x', pady=5)
        
        ttk.Button(file_button_frame, text="Process FASTA File", 
                  command=self.process_fasta_file).pack(side='left', padx=2)
        ttk.Button(file_button_frame, text="Sequence Statistics", 
                  command=self.calculate_sequence_stats).pack(side='left', padx=2)
        
        # Results area
        ttk.Label(main_frame, text="Results:", font=('Arial', 10, 'bold')).pack(anchor='w', pady=(10,0))
        self.tools_output = scrolledtext.ScrolledText(main_frame, height=15)
        self.tools_output.pack(fill='both', expand=True, pady=5)
    
    def create_overview_tab(self, parent):
        """Create the portfolio overview tab"""
        
        main_frame = ttk.Frame(parent)
        main_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Portfolio information
        info_text = """
Johns Hopkins Bioinformatics Portfolio
=====================================

Author: Ugochi Ndubuisi
Email: u.l.ndubuisi@gmail.com
JHU Email: undubui1@jh.edu
GitHub: ugochi141

Course Information:
------------------
• AS.410.634.81 - Practical Computer Concepts for Bioinformatics
  Instructor: Dr. Nadim Alkharouf

• AS.410.635.81 - Bioinformatics: Tools for Genome Analysis  
  Instructors: Sajung Yun and Sijung Yun

Completed Assignments:
---------------------
✅ Assignment 6: Control Structures and Lists
✅ Assignment 8: Functions
✅ Assignment 9: File I/O and BioPython
✅ Bioinformatics Analysis Projects
✅ Practical Bioinformatics Tools

Skills Demonstrated:
-------------------
• Python Programming for Bioinformatics
• DNA/RNA Sequence Analysis
• File I/O and Data Processing
• NGS Data Analysis and Variant Calling
• Gene Expression Analysis
• BioMart Database Queries
• VCF File Processing
• Statistical Analysis of Genomic Data

Tools and Technologies:
----------------------
• Python 3.x with BioPython
• R for Statistical Analysis
• VEP (Variant Effect Predictor)
• BioMart for Gene Information
• Shell Scripting for Workflow Automation
• Various Bioinformatics File Formats (FASTA, FASTQ, VCF, BED)

Portfolio Structure:
-------------------
• Programming Assignments (Control structures, functions, file I/O)
• Bioinformatics Analysis (NGS, gene analysis, genomics tools)
• Practical Tools (Sequence analyzers, file processors)
• Documentation and Reports
        """
        
        overview_text = scrolledtext.ScrolledText(main_frame, height=30, wrap='word')
        overview_text.pack(fill='both', expand=True)
        overview_text.insert('1.0', info_text)
        overview_text.config(state='disabled')
        
        # Links and actions
        links_frame = ttk.Frame(main_frame)
        links_frame.pack(fill='x', pady=10)
        
        ttk.Button(links_frame, text="View on GitHub", 
                  command=self.open_github).pack(side='left', padx=5)
        ttk.Button(links_frame, text="Generate Portfolio Report", 
                  command=self.generate_portfolio_report).pack(side='left', padx=5)
        ttk.Button(links_frame, text="Export Portfolio", 
                  command=self.export_portfolio).pack(side='left', padx=5)
    
    def load_assignments(self):
        """Load available assignments into the listbox"""
        assignments = [
            ("Assignment 6: Control Structures", "Assignments/Assignment6/Ndubuisi_A06.py"),
            ("Assignment 8: Functions", "Assignments/Assignment8/Ndubuisi_A08.py"), 
            ("Assignment 9: File I/O", "Assignments/Assignment9/assignment9.py"),
            ("Sequence Reader", "Assignments/Assignment9/sequence_reader.py"),
            ("DNA Sequence Tools", "Assignments/BioinformaticsAnalysis/genomics_tools/DNASequence.py"),
            ("Gene Lookup Tool", "Assignments/BioinformaticsAnalysis/genomics_tools/gene_lookup.py"),
            ("VEP Parser", "Assignments/BioinformaticsAnalysis/NGS_analysis/parse_vep.py")
        ]
        
        self.assignments = assignments
        
        for assignment in assignments:
            self.assignment_listbox.insert(tk.END, assignment[0])
    
    def on_assignment_select(self, event):
        """Handle assignment selection"""
        selection = self.assignment_listbox.curselection()
        if selection:
            index = selection[0]
            assignment = self.assignments[index]
            self.selected_assignment = assignment
    
    def run_selected_assignment(self):
        """Run the selected assignment"""
        if not hasattr(self, 'selected_assignment'):
            messagebox.showwarning("Warning", "Please select an assignment first")
            return
        
        assignment_name, assignment_path = self.selected_assignment
        full_path = self.portfolio_dir / assignment_path
        
        if not full_path.exists():
            messagebox.showerror("Error", f"Assignment file not found: {assignment_path}")
            return
        
        self.output_text.delete('1.0', tk.END)
        self.output_text.insert('1.0', f"Running {assignment_name}...\\n\\n")
        
        # Run in separate thread
        thread = threading.Thread(target=self.run_assignment_thread, args=(full_path,))
        thread.daemon = True
        thread.start()
    
    def run_assignment_thread(self, script_path):
        """Run assignment in separate thread"""
        try:
            # Change to the script's directory
            script_dir = script_path.parent
            
            result = subprocess.run(
                [sys.executable, str(script_path)],
                cwd=str(script_dir),
                capture_output=True,
                text=True,
                timeout=30
            )
            
            output = f"Exit code: {result.returncode}\\n\\n"
            output += "STDOUT:\\n" + result.stdout + "\\n"
            if result.stderr:
                output += "STDERR:\\n" + result.stderr + "\\n"
            
            self.root.after(0, self.update_output, output)
            
        except subprocess.TimeoutExpired:
            self.root.after(0, self.update_output, "Script timed out after 30 seconds\\n")
        except Exception as e:
            self.root.after(0, self.update_output, f"Error running script: {e}\\n")
    
    def update_output(self, text):
        """Update output text widget from main thread"""
        self.output_text.insert(tk.END, text)
        self.output_text.see(tk.END)
    
    def view_assignment_code(self):
        """View the code of the selected assignment"""
        if not hasattr(self, 'selected_assignment'):
            messagebox.showwarning("Warning", "Please select an assignment first")
            return
        
        assignment_name, assignment_path = self.selected_assignment
        full_path = self.portfolio_dir / assignment_path
        
        if not full_path.exists():
            messagebox.showerror("Error", f"Assignment file not found: {assignment_path}")
            return
        
        try:
            with open(full_path, 'r', encoding='utf-8') as f:
                code = f.read()
            
            self.output_text.delete('1.0', tk.END)
            self.output_text.insert('1.0', f"Code for {assignment_name}:\\n")
            self.output_text.insert(tk.END, "=" * 50 + "\\n\\n")
            self.output_text.insert(tk.END, code)
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to read file: {e}")
    
    def view_assignment_readme(self):
        """View README for the selected assignment"""
        if not hasattr(self, 'selected_assignment'):
            messagebox.showwarning("Warning", "Please select an assignment first")
            return
        
        assignment_name, assignment_path = self.selected_assignment
        readme_path = self.portfolio_dir / Path(assignment_path).parent / "README.md"
        
        if readme_path.exists():
            try:
                with open(readme_path, 'r', encoding='utf-8') as f:
                    readme = f.read()
                
                self.output_text.delete('1.0', tk.END)
                self.output_text.insert('1.0', f"README for {assignment_name}:\\n")
                self.output_text.insert(tk.END, "=" * 50 + "\\n\\n")
                self.output_text.insert(tk.END, readme)
                
            except Exception as e:
                messagebox.showerror("Error", f"Failed to read README: {e}")
        else:
            self.output_text.delete('1.0', tk.END)
            self.output_text.insert('1.0', f"No README found for {assignment_name}")
    
    def open_folder(self, path):
        """Open folder in file manager"""
        full_path = self.portfolio_dir / path
        
        if not full_path.exists():
            messagebox.showerror("Error", f"Folder not found: {path}")
            return
        
        try:
            if sys.platform == "win32":
                os.startfile(full_path)
            elif sys.platform == "darwin":
                subprocess.Popen(["open", full_path])
            else:
                subprocess.Popen(["xdg-open", full_path])
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open folder: {e}")
    
    def view_project_files(self, project):
        """View files in a project"""
        project_path = self.portfolio_dir / project["path"]
        
        if not project_path.exists():
            messagebox.showerror("Error", f"Project folder not found: {project['path']}")
            return
        
        file_list = "\\n".join([f"• {f}" for f in project["files"]])
        
        info = f"""
Project: {project["name"]}
Description: {project["description"]}
Location: {project["path"]}

Files:
{file_list}
        """
        
        self.output_text.delete('1.0', tk.END)
        self.output_text.insert('1.0', info)
    
    def analyze_dna_sequence(self):
        """Analyze DNA sequence"""
        sequence = self.dna_sequence_var.get().upper().strip()
        
        if not sequence:
            messagebox.showwarning("Warning", "Please enter a DNA sequence")
            return
        
        # Basic validation
        valid_bases = set('ATCG')
        if not all(base in valid_bases for base in sequence):
            messagebox.showerror("Error", "Invalid DNA sequence. Only A, T, C, G allowed.")
            return
        
        # Analysis
        length = len(sequence)
        a_count = sequence.count('A')
        t_count = sequence.count('T')
        c_count = sequence.count('C')
        g_count = sequence.count('G')
        
        gc_content = (c_count + g_count) / length * 100
        at_content = (a_count + t_count) / length * 100
        
        # Complement
        complement_map = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        complement = ''.join(complement_map[base] for base in sequence)
        
        # Reverse complement
        reverse_complement = complement[::-1]
        
        analysis = f"""
DNA Sequence Analysis
====================

Original Sequence: {sequence}
Length: {length} bases

Base Composition:
• Adenine (A): {a_count} ({a_count/length*100:.1f}%)
• Thymine (T): {t_count} ({t_count/length*100:.1f}%)
• Cytosine (C): {c_count} ({c_count/length*100:.1f}%)
• Guanine (G): {g_count} ({g_count/length*100:.1f}%)

Content Analysis:
• GC Content: {gc_content:.1f}%
• AT Content: {at_content:.1f}%

Sequence Transformations:
• Complement: {complement}
• Reverse Complement: {reverse_complement}

Analysis completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        """
        
        self.tools_output.delete('1.0', tk.END)
        self.tools_output.insert('1.0', analysis)
    
    def process_fasta_file(self):
        """Process a FASTA file"""
        file_path = filedialog.askopenfilename(
            title="Select FASTA File",
            filetypes=[("FASTA files", "*.fasta *.fa *.fas"), ("All files", "*.*")]
        )
        
        if not file_path:
            return
        
        try:
            sequences = []
            current_header = ""
            current_sequence = ""
            
            with open(file_path, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line.startswith('>'):
                        if current_header:
                            sequences.append((current_header, current_sequence))
                        current_header = line[1:]
                        current_sequence = ""
                    else:
                        current_sequence += line
                
                # Add last sequence
                if current_header:
                    sequences.append((current_header, current_sequence))
            
            # Analysis
            total_sequences = len(sequences)
            total_length = sum(len(seq[1]) for seq in sequences)
            avg_length = total_length / total_sequences if total_sequences > 0 else 0
            
            analysis = f"""
FASTA File Analysis
==================

File: {Path(file_path).name}
Total Sequences: {total_sequences}
Total Length: {total_length:,} bases
Average Length: {avg_length:.1f} bases

Sequences:
"""
            
            for i, (header, sequence) in enumerate(sequences[:10], 1):  # Show first 10
                gc_content = (sequence.count('G') + sequence.count('G')) / len(sequence) * 100 if sequence else 0
                analysis += f"\\n{i}. {header[:50]}{'...' if len(header) > 50 else ''}"
                analysis += f"\\n   Length: {len(sequence)} bases, GC: {gc_content:.1f}%"
            
            if total_sequences > 10:
                analysis += f"\\n\\n... and {total_sequences - 10} more sequences"
            
            self.tools_output.delete('1.0', tk.END)
            self.tools_output.insert('1.0', analysis)
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to process FASTA file: {e}")
    
    def calculate_sequence_stats(self):
        """Calculate sequence statistics"""
        stats = f"""
Sequence Statistics Calculator
=============================

This tool provides statistical analysis for biological sequences including:

• Sequence length and composition
• GC content analysis
• Codon usage analysis
• ORF (Open Reading Frame) detection
• Sequence similarity comparisons
• Molecular weight calculations
• Melting temperature estimation

To use:
1. Select a FASTA file using 'Process FASTA File'
2. Or enter a sequence in the DNA Sequence Analyzer
3. View detailed statistics and analysis results

Supported formats:
• FASTA (.fasta, .fa, .fas)
• Raw sequence text
• Multi-sequence files

Analysis timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        """
        
        self.tools_output.delete('1.0', tk.END)
        self.tools_output.insert('1.0', stats)
    
    def open_github(self):
        """Open GitHub repository"""
        webbrowser.open("https://github.com/ugochi141/JHU_Bioinformatics_Portfolio")
    
    def generate_portfolio_report(self):
        """Generate a comprehensive portfolio report"""
        report_path = self.portfolio_dir / "portfolio_report.html"
        
        report_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>JHU Bioinformatics Portfolio Report</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; line-height: 1.6; }}
        .header {{ background: #f4f4f4; padding: 20px; border-radius: 5px; }}
        .section {{ margin: 20px 0; }}
        .assignment {{ background: #f9f9f9; padding: 15px; margin: 10px 0; border-left: 4px solid #007cba; }}
        .skills {{ display: flex; flex-wrap: wrap; }}
        .skill {{ background: #007cba; color: white; padding: 5px 10px; margin: 5px; border-radius: 3px; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>Johns Hopkins Bioinformatics Portfolio</h1>
        <h2>Ugochi Ndubuisi</h2>
        <p>Email: u.l.ndubuisi@gmail.com | JHU Email: undubui1@jh.edu</p>
        <p>Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
    </div>
    
    <div class="section">
        <h2>Course Information</h2>
        <ul>
            <li><strong>AS.410.634.81</strong> - Practical Computer Concepts for Bioinformatics</li>
            <li><strong>AS.410.635.81</strong> - Bioinformatics: Tools for Genome Analysis</li>
        </ul>
    </div>
    
    <div class="section">
        <h2>Completed Assignments</h2>
        <div class="assignment">
            <h3>Assignment 6: Control Structures and Lists</h3>
            <p>Implementation of control structures, loops, and list operations for bioinformatics applications.</p>
        </div>
        <div class="assignment">
            <h3>Assignment 8: Functions</h3>
            <p>Development of reusable functions for sequence analysis and statistical calculations.</p>
        </div>
        <div class="assignment">
            <h3>Assignment 9: File I/O and BioPython</h3>
            <p>File processing and BioPython integration for biological data manipulation.</p>
        </div>
        <div class="assignment">
            <h3>Bioinformatics Analysis Projects</h3>
            <p>Comprehensive NGS analysis, gene studies, and genomics tool development.</p>
        </div>
    </div>
    
    <div class="section">
        <h2>Skills Demonstrated</h2>
        <div class="skills">
            <span class="skill">Python Programming</span>
            <span class="skill">BioPython</span>
            <span class="skill">DNA/RNA Analysis</span>
            <span class="skill">NGS Data Processing</span>
            <span class="skill">Variant Calling</span>
            <span class="skill">File I/O</span>
            <span class="skill">Statistical Analysis</span>
            <span class="skill">BioMart Queries</span>
            <span class="skill">VCF Processing</span>
            <span class="skill">Sequence Analysis</span>
        </div>
    </div>
    
    <div class="section">
        <h2>Portfolio Links</h2>
        <ul>
            <li><a href="https://github.com/ugochi141/JHU_Bioinformatics_Portfolio">GitHub Repository</a></li>
            <li><a href="https://ugochi141.github.io">Personal Portfolio</a></li>
        </ul>
    </div>
</body>
</html>
        """
        
        try:
            with open(report_path, 'w', encoding='utf-8') as f:
                f.write(report_content)
            
            messagebox.showinfo("Success", f"Portfolio report generated: {report_path}")
            
            # Open in browser
            webbrowser.open(f"file://{report_path.absolute()}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate report: {e}")
    
    def export_portfolio(self):
        """Export portfolio to a zip file"""
        from zipfile import ZipFile
        
        export_path = filedialog.asksaveasfilename(
            title="Export Portfolio",
            defaultextension=".zip",
            filetypes=[("ZIP files", "*.zip"), ("All files", "*.*")]
        )
        
        if not export_path:
            return
        
        try:
            with ZipFile(export_path, 'w') as zipf:
                # Add all portfolio files
                for root, dirs, files in os.walk(self.portfolio_dir):
                    for file in files:
                        if not file.startswith('.') and not file.endswith('.zip'):
                            file_path = Path(root) / file
                            arc_path = file_path.relative_to(self.portfolio_dir)
                            zipf.write(file_path, arc_path)
            
            messagebox.showinfo("Success", f"Portfolio exported to: {export_path}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to export portfolio: {e}")


def main():
    """Main function to run the portfolio launcher"""
    root = tk.Tk()
    app = BioinformaticsPortfolioLauncher(root)
    
    # Center the window
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - (root.winfo_width() // 2)
    y = (root.winfo_screenheight() // 2) - (root.winfo_height() // 2)
    root.geometry(f"+{x}+{y}")
    
    root.mainloop()


if __name__ == "__main__":
    main()