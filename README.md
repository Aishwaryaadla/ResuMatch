ResuMatch

📌 Overview

ResuMatch is a web application that leverages Machine Learning and Natural Language Processing (NLP) to classify resumes into job categories and analyze skill relevance. It helps job seekers understand how well their resumes match specific job roles and provides feedback to improve them.

🚀 Features

AI-Powered Resume Classification – Predicts the most relevant job category based on resume content.

Skill Extraction – Identifies key technical and soft skills.

Match Percentage Calculation – Compares extracted skills with the expected job skills.

Resume Strength Analysis – Evaluates resume length and completeness.

Feedback & Suggestions – Highlights missing skills and suggests improvements.

🛠️ Technologies Used

Python – Backend processing

Streamlit – Web framework for UI

Natural Language Toolkit (NLTK) – Text preprocessing and tokenization

Scikit-learn – TF-IDF vectorization and machine learning classification

Pickle – Model serialization and loading

📂 Installation & Setup

1️⃣ Clone the Repository

git clone https://github.com/Aishwaryaadla/ResuMatch.git
cd ResuMatch

2️⃣ Create a Virtual Environment (Optional but Recommended)

python -m venv my_env
source my_env/bin/activate  # For macOS/Linux
my_env\Scripts\activate    # For Windows

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Run the Application

streamlit run app.py

📌 Usage

Upload a resume file in .txt or .pdf format.

The app will analyze the content and classify it into a job category.

View skill match percentage, missing skills, and resume strength.

Get feedback to improve your resume for better job prospects.


📸 Screenshots

Here are some screenshots of the application in action:



<img width="1438" alt="Screenshot 2025-03-16 at 1 14 53 PM" src="https://github.com/user-attachments/assets/d9f7c396-93da-4c61-8395-90ab793c0818" />

<img width="1440" alt="Screenshot 2025-03-16 at 1 15 31 PM" src="https://github.com/user-attachments/assets/dc85329a-d5ba-4c3d-881b-9ba6c79923eb" />

<img width="1418" alt="Screenshot 2025-03-16 at 1 15 55 PM" src="https://github.com/user-attachments/assets/6b48a500-9567-4313-b7c6-b9974860b634" />




📝 Sample Output!

Predicted Job Category: Python Developer

Match Percentage: 80%

Matched Skills: Python, Django, TensorFlow

Missing Skills: Flask, Pandas

Resume Strength: ✅ Well-Balanced Resume!

Soft Skills Detected: Leadership, Problem-Solving

🔥 Future Enhancements

Integration with GPT-based resume evaluation

Support for more job categories and detailed analytics

PDF parsing improvements for better accuracy

🤝 Contributing

Want to contribute? Feel free to fork the repo, create a new branch, and submit a pull request (PR).

📜 License

This project is licensed under the MIT License.

