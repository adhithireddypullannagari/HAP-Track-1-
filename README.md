# **README**

# **AI-Powered Candidate Ranking System**

## **Overview**

Recruitment has become increasingly challenging as organizations receive thousands of applications for a single job opening. Reviewing every candidate manually is both time-consuming and prone to human bias. To address this challenge, we developed an AI-Powered Candidate Ranking System as part of the Redrob Intelligent Candidate Discovery & Ranking Challenge.

The primary objective of this project is to automatically identify the most suitable candidates for a given Job Description (JD) by analyzing multiple aspects of their profiles. Instead of relying only on keyword matching, the system evaluates candidates based on their technical skills, professional experience, behavioral signals, and overall profile quality. It then assigns each candidate a score and ranks them according to their suitability for the role.

The final output is a ranked list of the top candidates, making the recruitment process faster, more accurate, and transparent.

# **Problem Statement**

Traditional recruitment systems mainly depend on keyword-based searches. While these methods are simple, they often overlook talented candidates whose profiles use different terminology or present their experience differently. As a result, recruiters may miss qualified applicants and spend additional time manually reviewing profiles.

The goal of this project is to build an intelligent candidate ranking system that evaluates applicants more comprehensively. By considering multiple factors such as skills, work experience, and behavioral indicators, the system helps recruiters identify the best candidates efficiently and objectively.

# **Dataset**

The project uses a structured dataset containing detailed information about each candidate. The dataset includes:

- Candidate profile information
- Career history and work experience
- Educational qualifications
- Technical and professional skills
- Certifications
- Languages known
- Redrob behavioral signals

These features provide a complete understanding of each candidate and help improve the ranking process.

# **Methodology**

The ranking process consists of four major stages.

## 1\. Skill Matching

The first step is to compare the candidate's skills with the skills required in the Job Description. Every matching skill contributes positively to the candidate's overall score.

The Skill Score is calculated using the following formula:

Skill Score = Number of Matched Skills / Total Required Skills

A higher score indicates that the candidate possesses more of the required technical competencies.

## 2\. Experience Analysis

Experience plays a significant role in determining whether a candidate is suitable for a particular role. The system assigns scores based on the candidate's relevant years of experience.

| Experience        | Score |
| ----------------- | ----- |
| 6 years or more   | 1.0   |
| 4-5 years         | 0.8   |
| 2-3 years         | 0.6   |
| Less than 2 years | 0.3   |

This scoring method ensures that experienced professionals receive appropriate weight while still allowing promising early-career candidates to compete.

## 3\. Behavioral Signal Scoring

Apart from technical qualifications, recruiter engagement and candidate activity also provide valuable insights into candidate reliability.

The behavioral features considered include:

- Open to Work status
- Recruiter response rate
- Offer acceptance rate
- Profile completeness
- GitHub activity
- Email verification
- Phone verification

These indicators help identify candidates who are active, responsive, and genuinely interested in new opportunities.

## 4\. Final Candidate Ranking

After calculating the individual scores, the system combines them into a single Final Score using weighted importance.

Final Score =

(40% × Skill Score) + (25% × Experience Score) + (35% × Behavioral Score)

Candidates are then sorted in descending order based on their Final Score. The highest-scoring candidates appear at the top of the ranking list.

# **Explainable AI**

One of the key features of this project is its explainability. Instead of simply assigning a score, the system also provides a brief explanation for each candidate's ranking.

The reasoning is generated based on:

- Skill match with the job requirements
- Relevant work experience
- Positive behavioral indicators

This transparency allows recruiters to understand why a candidate received a particular ranking, increasing confidence in the recommendation system.

#

# **Technologies Used**

The project was implemented using the following technologies:

- Python
- Pandas
- NumPy
- Scikit-learn
- Google Colab

These tools were used for data preprocessing, feature analysis, score calculation, ranking, and result generation.

# **Output**

The system generates a file named submission.csv, which contains the ranked list of candidates.

Each record includes:

- Candidate ID
- Rank
- Final Score
- Ranking Reason

This output can be directly submitted for evaluation or integrated into a recruitment workflow.

#

# **Validation**

To ensure correctness, the generated submission file was tested using the official validator provided in the challenge.

Validation Status**:** Successfully Passed

The validation confirmed that the output format and ranking structure met all the competition requirements.

# **Advantages**

The proposed system offers several benefits:

- Reduces manual effort during candidate screening.
- Identifies qualified candidates more accurately than keyword-based methods.
- Considers both technical and behavioral aspects of candidates.
- Provides transparent explanations for every ranking.
- Produces consistent and unbiased candidate evaluations.
- Can be easily adapted for different job roles and industries.

# **Future Enhancements**

Although the current system performs well, several improvements can further enhance its performance:

- Use Natural Language Processing (NLP) to understand resumes and job descriptions more effectively.
- Apply deep learning models for semantic skill matching.
- Include interview feedback as an additional ranking factor.
- Support multilingual resumes.
- Integrate with Applicant Tracking Systems (ATS) for real-time recruitment.
- Continuously learn from recruiter feedback to improve future rankings.

# **Conclusion**

The AI-Powered Candidate Ranking System demonstrates how artificial intelligence can simplify and improve the recruitment process. By combining skill matching, experience evaluation, behavioral analysis, and explainable ranking, the system provides a reliable way to identify the most suitable candidates for a job.

Compared to traditional keyword-based recruitment methods, this approach offers greater accuracy, fairness, and transparency. It helps recruiters save valuable time while ensuring that deserving candidates receive the attention they deserve. Overall, this project highlights the potential of AI in building smarter and more efficient hiring solutions.

# **Author**

Developed as part of the Redrob Intelligent Candidate Discovery & Ranking Challenge.