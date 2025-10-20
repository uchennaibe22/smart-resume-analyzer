from flask import Flask, render_template, request 
import pdfplumber

app = Flask(__name__)

# simple list of skills to look for
SKILLS = ["python", "java", "c++", "sql", "flask", "django", "aws", "git", "docker", "pandas", "machine learning", "data analysis"]

@app.route("/", methods=["GET", "POST"])
def home_control():
    # make sure lists always exist
    found_skills = []
    common_skills = []
    missing_skills = []
    match_score = 0

    if request.method == "POST":
        if "resume_file" in request.files and request.files["resume_file"].filename  != "":
            upload_file = request.files["resume_file"]
            with pdfplumber.open(upload_file) as pdf:
                resume_text = ""
                for page in pdf.pages:
                    resume_text += page.extract_text() + " "
            resume_text = resume_text.lower()


            
        else:
            resume_text = request.form["resume_text"].lower()
        
        job_text = request.form.get("job_text", "").lower()
        print("Raw job text received:", job_text[:200])



        # Job description skills
        job_skills = []
        for skill in SKILLS:
            if skill in job_text:
                job_skills.append(skill)

        # Resume skills
        for skill in SKILLS:
            if skill.lower().strip() in resume_text.lower():
                found_skills.append(skill.lower().strip())

        # Normalize skill lists to lowercase and trimmed versions
        found_skills = [s.lower().strip() for s in found_skills]
        job_skills = [s.lower().strip() for s in job_skills]

        # Compare
        common_skills = [s for s in found_skills if s in job_skills]
        missing_skills = [s for s in job_skills if s not in found_skills]

        print("FOUND SKILLS:", found_skills)
        print("JOB SKILLS:", job_skills)
        print("COMMON SKILLS:", common_skills)
        print("MISSING SKILLS:", missing_skills)


        
        if len(job_skills) > 0:
          match_score = (len(common_skills) / len(job_skills)) * 100
        else: 
             match_score = 0
       
        if "match_score" not in locals(): 
            match_score = 0

        # ✅ Move this block inside the POST section (8 spaces indented)
        print("==== DEBUG ====")
        print("Job text:", job_text[:200])
        print("Job skills found:", job_skills)
        print("Resume skills found:", found_skills)
        print("Common skills:", common_skills)
        print("Match score:", match_score)
        print("================")


    # always return, no matter GET or POST
    return render_template(
        "index.html",
        found_skills=found_skills,
        common_skills=common_skills,
        missing_skills=missing_skills,
        match_score=match_score

    )


if __name__ == "__main__":
    print("App.py is being run directly")
    app.run(debug=True)



