# Smart Resume Analyzer 

![App Screenshot](https://raw.githubusercontent.com/uchennaibe22/smart-resume-analyzer/main/screenshot.png)



A simple Flask web app that allows users to compare resume text or upload there own resume, against a job description. It highlights common skills, missing skills, and gives the users an ac curate match score percentage based on results.


## Features
- Paste your resume or upload a PDF
- Paste a Job Descritiption
- Insantly see:
- Common Skills
- Missing Skills
- Match Scores

## 🛠️ Tech Stack
- Python (Flask)
- HTML, CSS (Jinja templating)
- pdfplumber (for resume parsing)



## Example Skills It Detects
Python, Java, C++, SQL, Flask, Django, AWS, Git, Docker, Pandas, Machine Learning, Data Analysis


   ## 🚀 Run Locally
Clone the project:
```bash
git clone https://github.com/uchennaibe22/smart-resume-analyzer.git
cd smart-resume-analyzer
pip install -r requirements.txt
python app.py
