# **Methodology**

## **Project Overview**

The main objective of this project is to develop an intelligent candidate ranking system that identifies the most suitable applicants for a specific Job Description (JD). Instead of relying only on keyword matching, the proposed system evaluates candidates using multiple factors, including their technical skills, professional experience, and behavioral signals. By combining these factors, the system generates an overall score for each candidate and ranks them according to their suitability for the job.

The final output of the system is a ranked list of candidates, along with their scores and a brief explanation describing why they were recommended. This approach helps recruiters make faster, more informed, and transparent hiring decisions.

# **Data Understanding**

A clear understanding of the available data is essential for building an effective ranking system. The candidate dataset contains comprehensive information that represents both the professional qualifications and behavioral characteristics of each applicant.

The dataset includes the following details:

- Candidate profile information
- Career history
- Educational qualifications
- Technical and professional skills
- Certifications
- Languages known
- Redrob behavioral signals

Among these features, the behavioral signals provide valuable insights into candidate engagement, responsiveness, and profile quality. These indicators help the system distinguish between candidates who have similar technical qualifications but differ in their level of activity and reliability.

# **Ranking Approach**

The proposed ranking system evaluates every candidate using three major scoring components. Each component measures a different aspect of candidate suitability, ensuring a balanced and comprehensive evaluation.

## 1\. Skill Matching Score

The first stage focuses on comparing the candidate's skills with the skills required in the Job Description. Since technical skills are one of the most important factors in recruitment, this component carries the highest weight in the final score.

The skill matching process involves the following steps:

- Extract the list of required skills from the Job Description.
- Retrieve the skills listed in the candidate's profile.
- Compare both skill sets to identify matching skills.
- Calculate a normalized score between 0 and 1.

The Skill Score is calculated using the formula:

Skill Score = Number of Matching Skills / Total Required Skills

A candidate who possesses most or all of the required skills receives a higher score, increasing their overall ranking.

## 2\. Experience Score

Professional experience is another important factor that reflects a candidate's ability to perform effectively in a given role. The system evaluates the total years of relevant work experience and assigns a normalized score based on predefined experience ranges.

The evaluation process includes:

- Extracting the candidate's years of professional experience.
- Comparing the experience with the expected requirements.
- Assigning an appropriate score.

The experience scoring criteria are shown below:

| Experience        | Score |
| ----------------- | ----- |
| 6 years or more   | 1.0   |
| 4-5 years         | 0.8   |
| 2-3 years         | 0.6   |
| Less than 2 years | 0.3   |

This scoring strategy ensures that experienced candidates receive appropriate recognition while still providing opportunities for promising early-career professionals.

## 3\. Behavioral Score

Technical qualifications alone do not always indicate whether a candidate is suitable for a role. Therefore, the system also considers behavioral signals that reflect candidate engagement and profile quality.

The behavioral features used in this project include:

- Open to Work status
- Profile completeness score
- Recruiter response rate
- Offer acceptance rate
- GitHub activity
- Verified email
- Verified phone number

These indicators help identify candidates who are:

- Actively seeking employment
- Responsive to recruiters
- Reliable and trustworthy
- Maintaining complete and updated profiles

Including behavioral analysis improves the overall quality of the ranking process by considering factors that are often overlooked in traditional recruitment systems.

# **Final Ranking Formula**

After calculating the Skill Score, Experience Score, and Behavioral Score, the system combines these values into a single Final Score using weighted scoring.

The Final Score is calculated as:

Final Score =

(40% × Skill Score) + (25% × Experience Score) + (35% × Behavioral Score)

Greater importance is given to skill matching because technical competency is the primary requirement for most job roles. Experience and behavioral quality are also considered to ensure a balanced evaluation.

# **Candidate Ranking Process**

The complete candidate ranking workflow consists of the following steps:

- Load the candidate dataset.
- Extract the required skills from the Job Description.
- Calculate the Skill Matching Score.
- Evaluate the Experience Score.
- Compute the Behavioral Score.
- Calculate the Final Score using the weighted formula.
- Sort all candidates in descending order based on the Final Score.
- Assign ranking positions to each candidate.
- Select the top-ranked candidates for the final submission.

This systematic workflow ensures that every candidate is evaluated consistently using the same set of criteria.

# **Explainability**

One of the important features of the proposed system is its ability to explain the ranking decisions. Rather than simply assigning a numerical score, the system generates a brief reasoning statement for every candidate.

The explanation highlights key factors that influenced the ranking, including:

- Relevant technical skills
- Professional experience
- Positive behavioral indicators

For example:

_"Strong skill match with the required technologies, relevant professional experience, and excellent behavioral engagement signals."_

Providing these explanations increases transparency and helps recruiters understand why a candidate was recommended.

# **Validation**

After generating the ranked candidate list, the submission file is validated using the official validation script provided in the challenge.

The validation process verifies several important aspects, including:

- Presence of all required columns
- Correct candidate ID format
- Proper ranking order
- Correct score ordering
- Required submission size

The generated submission file successfully passed all validation checks, confirming that it meets the competition requirements.

**Technologies Used**

The project was implemented using the following technologies:

- Python
- Pandas
- JSON
- Google Colab

These technologies were used for data preprocessing, score calculation, ranking generation, and validation.

# **Conclusion**

The proposed AI-Powered Candidate Ranking System provides an efficient and transparent approach to identifying the most suitable candidates for a given job role. By combining skill matching, experience evaluation, and behavioral analysis, the system delivers more accurate rankings than traditional keyword-based methods.

The methodology is computationally efficient, easy to understand, and scalable for large candidate datasets. Additionally, the explainable ranking mechanism improves recruiter confidence by providing clear reasons behind every recommendation. Overall, this approach demonstrates how artificial intelligence can simplify recruitment while improving both efficiency and decision-making quality.