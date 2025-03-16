import streamlit as st
import pickle
import re
import nltk

nltk.download('punkt')
nltk.download('stopwords')


#loading models
with open('/Users/aishwaryaadla/Desktop/resume_analyzer/my_env/clf.pkl', 'rb') as f:
    clf = pickle.load(f)
with open('/Users/aishwaryaadla/Desktop/resume_analyzer/my_env/tfidf.pkl', 'rb') as f:
    tfidf = pickle.load(f)

def cleanResume(txt):
  cleantxt = re.sub('http\S+\s','',txt)
  cleantxt = re.sub('RT|cc',' ',cleantxt)
  cleantxt = re.sub('#\S+',' ',cleantxt)
  cleantxt = re.sub('@\S+',' ',cleantxt)
  cleantxt = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""),' ',cleantxt)
  cleantxt = re.sub(r'[^\x00-\x7f]',' ',cleantxt)
  cleantxt = re.sub('\s+',' ',cleantxt)
  return cleantxt


  # Predefined skill set for different categories

SKILL_SET = {
    "Python Developer": ["Python", "Flask", "Django", "TensorFlow", "Pandas", "NumPy"],
    "Java Developer": ["Java", "Spring", "Hibernate", "J2EE", "Maven"],
    "Data Science": ["Machine Learning", "Deep Learning", "Pandas", "NumPy", "Scikit-learn"],
    "Web Designing": ["HTML", "CSS", "JavaScript", "React", "Figma"],
}
# def extract_skills(text):
#     """Extract relevant skills using keyword matching"""
#     detected_skills = []
#     for category, skills in SKILL_SET.items():
#         for skill in skills:
#             if skill.lower() in text.lower():
#                 detected_skills.append(skill)
#     return detected_skills

def extract_skills(text):
    """Extract skills from resume text using keyword matching."""
    SKILL_KEYWORDS = [
        "python", "java", "c++", "machine learning", "data analysis", "sql", "aws", "docker", 
        "javascript", "html", "css", "react", "node.js", "tensorflow", "pandas", "excel",
        "communication", "leadership", "teamwork", "problem-solving"
    ]
    
    text = text.lower()
    detected_skills = [skill for skill in SKILL_KEYWORDS if skill in text]
    
    return detected_skills


def calculate_match_percentage(resume_skills, category_name):
    """Calculate match percentage based on skills extracted from resume."""
    SKILL_SET = {
        "Java Developer": ["java", "spring", "hibernate", "junit", "maven"],
        "Python Developer": ["python", "django", "flask", "tensorflow", "pandas"],
        "Web Designing": ["html", "css", "javascript", "bootstrap", "react"],
        "Data Science": ["python", "machine learning", "data analysis", "tensorflow"],
        "Database": ["sql", "mysql", "mongodb", "oracle", "postgresql"],
        "DevOps Engineer": ["aws", "docker", "kubernetes", "jenkins", "terraform"]
    }
    
    # Ensure category exists in the skill set
    job_skills = SKILL_SET.get(category_name, [])
    if not job_skills:
        return 0.0, []  # If category not found, return 0%

    matched_skills = list(set(resume_skills) & set(job_skills))
    match_percentage = (len(matched_skills) / len(job_skills)) * 100 if job_skills else 0

    return round(match_percentage, 2), matched_skills


def generate_feedback(resume_skills, category_name):
    """Suggest missing skills"""
    job_skills = SKILL_SET.get(category_name, [])
    missing_skills = set(job_skills) - set(resume_skills)

    if not missing_skills:
        return "✅ Your resume has all required skills!"
    
    feedback = f"⚠️ Missing Skills: {', '.join(missing_skills)}\n"
    feedback += "🔹 Consider adding relevant projects or certifications."
    return feedback

def calculate_resume_strength(text):
    """Analyze resume length and suggest improvements"""
    word_count = len(text.split())

    if word_count < 250:
        return "❌ Too Short - Add more details!"
    elif word_count > 1000:
        return "⚠️ Too Long - Try to be concise."
    else:
        return "✅ Well-Balanced Resume!"

def detect_soft_skills(text):
    """Detect soft skills in the resume text"""
    SOFT_SKILLS = ["communication", "teamwork", "leadership", "problem-solving", "creativity", "adaptability"]

    detected_skills = [skill for skill in SOFT_SKILLS if skill.lower() in text.lower()]
    return detected_skills


# #web app
def main():
    st.title("Smart Resume Analyzer")
    upload_file = st.file_uploader('Upload Resume',type=['txt','pdf'])
    if upload_file is not None:
        try:
            resume_bytes = upload_file.read()
            resume_text = resume_bytes.decode('utf-8')
        except UnicodeDecodeError:
            resume_text = resume_bytes.decode('latin-1')

        new_resume = cleanResume(resume_text)
        input_features = tfidf.transform([new_resume])
        prediction_id = clf.predict(input_features)[0]
    # st.write(prediction_id)

        category_mapping = {
            15: "Java Developer",
            23:"Testing",
            8: "DevOps Engineer",
            20: "Python Developer",
            24: "Web Designing",
            12: "HR",
            13: "Hadoop",
            3: "Blockchain",
            10: "ETL Developer",
            18: "Operations Manager",
            6: "Data Science",
            22: "Sales",
            16: "Mechanical Engineer",
            1: "Arts",
            7: "Database",
            11: "Electrical Engineer",
            14: "Health and Fitness",
            19: "PMO",
            4: "Business Analyst",
            9: "DotNet Developer",
            2: "Automation Testing",
            17: "Network Security Engineer",
            21: "SAP Developer",
            5: "Civil Engineer",
            8: "Advocate"
        }

        category_name = category_mapping.get(prediction_id, "Unknown")

        st.write("Predicted Category: ",category_name)

        #CG-Extract skills
        resume_skills = extract_skills(new_resume)
        match_percentage, matched_skills = calculate_match_percentage(resume_skills, category_name)

        st.subheader("🔍 Skill Matching")
        st.write(f"✅ **Match Percentage:** {match_percentage}%")
        st.write(f"🔹 **Matched Skills:** {', '.join(matched_skills) if matched_skills else 'None'}")

        # Generate feedback
        feedback = generate_feedback(resume_skills, category_name)
        st.subheader("📢 Resume Feedback")
        st.warning(feedback)

        # Resume strength
        st.subheader("📊 Resume Strength")
        st.write(calculate_resume_strength(new_resume))

        # Detect soft skills
        soft_skills = detect_soft_skills(new_resume)
        st.subheader("💡 Soft Skills Detected")
        st.write(", ".join(soft_skills) if soft_skills else "No soft skills detected.")

if __name__ == "__main__":
    main()