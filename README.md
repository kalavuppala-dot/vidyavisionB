# 🎓 AI Career Guidance & Resume Generator

A powerful Streamlit web application that provides personalized career guidance and generates professional, ATS-friendly resumes using **Llama 3.3 70B** via **Groq API**.

## ✨ Features

- **Career Guidance**: Get 5 personalized career recommendations based on your skills and interests
- **Skill Match Analysis**: See which skills you have and which you need to learn
- **Learning Roadmap**: Step-by-step guide to achieve your target career
- **Resume Generator**: Create professional, ATS-compatible resumes in Markdown format
- **Powered by Llama 3.3 70B**: State-of-the-art AI via Groq's ultra-fast inference

## 🚀 Quick Start

### 1. Prerequisites

- Python 3.8 or higher
- Groq API key ([Get one here](https://console.groq.com))

### 2. Installation

```bash
# Clone or navigate to the project directory
cd vidyavisionB

# Install dependencies
pip install -r requirements.txt
```

### 3. Configuration

Create a `.env` file in the project root:

```bash
# Copy the example file
copy .env.example .env
```

Edit `.env` and add your Groq API key:

```
GROQ_API_KEY=your_actual_groq_api_key_here
```

### 4. Run the Application

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## 📖 How to Use

### Career Guidance

1. Go to the **Career Guidance** tab in the sidebar
2. Fill in:
   - Your technical skills
   - Your interests
   - Education background
   - Projects you've worked on
   - Experience level
3. Click **"🎯 Get Career Guidance"**
4. Review your personalized recommendations
5. Download the results as a Markdown file

### Resume Generation

1. Go to the **Resume Generator** tab in the sidebar
2. Fill in:
   - Personal information (name, email, phone, LinkedIn)
   - Technical skills
   - Education
   - Projects
   - Experience (optional)
   - Target role
3. Click **"📄 Generate Resume"**
4. Review your professional resume
5. Download as a Markdown file

## 🔑 Getting a Groq API Key

1. Visit [Groq Console](https://console.groq.com)
2. Sign up or log in
3. Navigate to API Keys section
4. Create a new API key
5. Copy and paste it into your `.env` file

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **AI Model**: Llama 3.3 70B (via Groq)
- **Language**: Python 3.8+
- **API**: Groq API

## 📝 Output Format

### Career Guidance Output
- 🎯 5 Recommended Careers
- 🧠 Skill Match Analysis (with percentage)
- 🗺️ Learning Roadmap (5-7 actionable steps)

### Resume Output
- Professional Markdown format
- ATS-compatible structure
- Sections: Header, Summary, Skills, Projects, Education, Experience

## 🔒 Security Notes

- Never commit your `.env` file to version control
- Keep your `GROQ_API_KEY` private
- The `.env.example` file is safe to share

## 📄 License

This project is open source and available for educational purposes.

## 🤝 Support

For issues or questions:
- Check the Groq documentation: https://console.groq.com/docs
- Review Streamlit docs: https://docs.streamlit.io

---

**Built with ❤️ using Llama 3.3 70B and Groq**
