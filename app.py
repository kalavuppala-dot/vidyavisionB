import streamlit as st
import os
from groq import Groq
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Groq client
def get_groq_client():
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        st.error("⚠️ GROQ_API_KEY not found in environment variables!")
        st.stop()
    return Groq(api_key=api_key)

# Career guidance prompt
def create_career_guidance_prompt(user_data):
    return f"""You are an advanced Career Guidance and Resume Generator assistant.

Student Profile:
- Technical Skills: {user_data.get('skills', 'Not provided')}
- Interests: {user_data.get('interests', 'Not provided')}
- Education: {user_data.get('education', 'Not provided')}
- Projects: {user_data.get('projects', 'Not provided')}
- Experience Level: {user_data.get('experience_level', 'Beginner')}

Your task:
1. Recommend 5 relevant career paths in technology
2. Select the BEST-MATCHED role and assign a realistic match percentage (0-100%)
3. For the best-matched role, provide:
   - Matched skills (skills the student already has)
   - Skills to learn (gaps to fill)
   - A step-by-step learning roadmap (5-7 actionable steps)

Format your response EXACTLY as follows:

🎯 RECOMMENDED CAREERS
1. [Career Name 1] - [Brief description]
2. [Career Name 2] - [Brief description]
3. [Career Name 3] - [Brief description]
4. [Career Name 4] - [Brief description]
5. [Career Name 5] - [Brief description]

🧠 SKILL MATCH ANALYSIS
**Best Match: [Career Name]**
**Match Score: [X]%**

**Matched Skills:**
- [Skill 1]
- [Skill 2]
- [Skill 3]

**Skills to Learn:**
- [Skill 1]
- [Skill 2]
- [Skill 3]

🗺️ LEARNING ROADMAP
**Step 1:** [Action item]
**Step 2:** [Action item]
**Step 3:** [Action item]
**Step 4:** [Action item]
**Step 5:** [Action item]

Keep explanations concise, beginner-friendly, and practical."""

# Resume generation prompt
def create_resume_prompt(user_data):
    return f"""Generate a professional, ATS-friendly resume in Markdown format.

User Information:
- Name: {user_data.get('name', 'Not provided')}
- Email: {user_data.get('email', 'Not provided')}
- Phone: {user_data.get('phone', 'Not provided')}
- LinkedIn: {user_data.get('linkedin', 'Not provided')}
- Technical Skills: {user_data.get('skills', 'Not provided')}
- Education: {user_data.get('education', 'Not provided')}
- Projects: {user_data.get('projects', 'Not provided')}
- Experience: {user_data.get('experience', 'None')}
- Target Role: {user_data.get('target_role', 'Not specified')}

Create a resume with these sections:
1. Header (Name and contact info)
2. Professional Summary (2-3 lines tailored to target role)
3. Technical Skills (categorized)
4. Projects (with descriptions and technologies used)
5. Education
6. Experience (if any)

Use clean Markdown formatting. Do NOT hallucinate information. Keep it ATS-compatible and professional."""

# Call Groq API
def get_groq_response(prompt, temperature=0.7):
    try:
        client = get_groq_client()
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert career counselor and resume writer specializing in technology careers."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            model="llama-3.3-70b-versatile",
            temperature=temperature,
            max_tokens=2048,
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        st.error(f"Error calling Groq API: {str(e)}")
        return None

# Streamlit UI
def main():
    st.set_page_config(
        page_title="AI Career Guidance & Resume Generator",
        page_icon="🎓",
        layout="wide"
    )
    
    st.title("🎓 AI Career Guidance & Resume Generator")
    st.markdown("*Powered by Llama 3.3 70B via Groq*")
    st.divider()
    
    # Sidebar for user input
    with st.sidebar:
        st.header("📝 Your Information")
        
        tab1, tab2 = st.tabs(["Career Guidance", "Resume Generator"])
        
        with tab1:
            st.subheader("Career Guidance Input")
            skills = st.text_area(
                "Technical Skills",
                placeholder="e.g., Python, JavaScript, React, SQL",
                help="List your current technical skills"
            )
            interests = st.text_area(
                "Interests",
                placeholder="e.g., Web Development, AI/ML, Data Science",
                help="What areas of tech interest you?"
            )
            education = st.text_input(
                "Education",
                placeholder="e.g., B.Tech in Computer Science"
            )
            projects = st.text_area(
                "Projects",
                placeholder="Briefly describe 1-2 projects you've worked on"
            )
            experience_level = st.selectbox(
                "Experience Level",
                ["Beginner", "Intermediate", "Advanced"]
            )
            
            analyze_btn = st.button("🎯 Get Career Guidance", type="primary", use_container_width=True)
        
        with tab2:
            st.subheader("Resume Input")
            name = st.text_input("Full Name*")
            email = st.text_input("Email*")
            phone = st.text_input("Phone")
            linkedin = st.text_input("LinkedIn Profile")
            
            resume_skills = st.text_area(
                "Technical Skills*",
                placeholder="e.g., Python, React, Node.js, Docker"
            )
            resume_education = st.text_area(
                "Education*",
                placeholder="Degree, University, Year"
            )
            resume_projects = st.text_area(
                "Projects*",
                placeholder="Project name, description, technologies used"
            )
            resume_experience = st.text_area(
                "Experience (Optional)",
                placeholder="Job title, company, duration, responsibilities"
            )
            target_role = st.text_input(
                "Target Role",
                placeholder="e.g., Full Stack Developer"
            )
            
            generate_btn = st.button("📄 Generate Resume", type="primary", use_container_width=True)
    
    # Main content area
    if analyze_btn:
        if not skills or not interests:
            st.warning("⚠️ Please provide at least your skills and interests!")
        else:
            with st.spinner("🤖 Analyzing your profile and generating career guidance..."):
                user_data = {
                    'skills': skills,
                    'interests': interests,
                    'education': education,
                    'projects': projects,
                    'experience_level': experience_level
                }
                
                prompt = create_career_guidance_prompt(user_data)
                response = get_groq_response(prompt)
                
                if response:
                    st.success("✅ Career Guidance Generated!")
                    st.markdown(response)
                    
                    # Download option
                    st.download_button(
                        label="📥 Download Career Guidance",
                        data=response,
                        file_name=f"career_guidance_{datetime.now().strftime('%Y%m%d')}.md",
                        mime="text/markdown"
                    )
    
    if generate_btn:
        if not name or not email or not resume_skills or not resume_education:
            st.warning("⚠️ Please fill in all required fields (marked with *)!")
        else:
            with st.spinner("🤖 Generating your professional resume..."):
                user_data = {
                    'name': name,
                    'email': email,
                    'phone': phone,
                    'linkedin': linkedin,
                    'skills': resume_skills,
                    'education': resume_education,
                    'projects': resume_projects,
                    'experience': resume_experience,
                    'target_role': target_role
                }
                
                prompt = create_resume_prompt(user_data)
                response = get_groq_response(prompt, temperature=0.5)
                
                if response:
                    st.success("✅ Resume Generated!")
                    st.markdown(response)
                    
                    # Download option
                    st.download_button(
                        label="📥 Download Resume",
                        data=response,
                        file_name=f"{name.replace(' ', '_')}_resume.md",
                        mime="text/markdown"
                    )
    
    # Initial instructions
    if not analyze_btn and not generate_btn:
        st.info("""
        ### 👋 Welcome!
        
        This application helps you:
        - **Get Career Guidance**: Discover suitable tech careers based on your skills and interests
        - **Generate Resume**: Create an ATS-friendly professional resume
        
        **How to use:**
        1. Fill in your information in the sidebar
        2. Choose either "Career Guidance" or "Resume Generator" tab
        3. Click the button to generate results
        4. Download your results as a Markdown file
        
        **Powered by Llama 3.3 70B via Groq API**
        """)

if __name__ == "__main__":
    main()
