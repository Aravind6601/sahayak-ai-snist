🧠 Sahayak - Your AI Governance Assistant
Sahayak is an intelligent, multilingual AI assistant designed to demystify government schemes for every Indian citizen. It transforms the complex maze of bureaucratic information into simple, personalized, and actionable advice.

This project was built for the "Hack-AI-thon – 2025" hosted by the Department of Artificial Intelligence & Machine Learning at SNIST.

🚀 The Problem
India has over 1,000 welfare schemes, but citizens face significant barriers to accessing them:

Information Overload: The sheer volume of schemes makes it impossible to track opportunities.

Complex Jargon: Details are often buried in dense, hard-to-understand official documents.

Lack of Personalization: Citizens don't know which of the hundreds of schemes applies to their specific situation.

As a result, a massive gap exists between the government's intention and the impact on our citizens.

✨ Our Solution
Sahayak acts as an intelligent guide. A user simply describes their situation in plain language—using text or voice—and our AI does the rest.

Unlike a simple search engine, Sahayak uses a powerful Large Language Model to understand a user's intent and context. It is location-aware, distinguishing between Central and State schemes to provide truly personalized and accurate recommendations in a clear, step-by-step format.

📸 Screenshots
Here's a look at Sahayak in action:

Intelligent, Location-Aware Recommendations:

Conversational Clarification for Vague Queries:

Detailed, Actionable Guides with Full Voice Control:

🛠️ Key Features
AI-Powered Recommendations: Utilizes the Google Gemini LLM to understand natural language and provide relevant scheme recommendations.

Context & Location-Awareness: Intelligently prioritizes Central schemes but suggests State-specific schemes when a location is mentioned.

Full Voice Control: Integrated Speech-to-Text (STT) for voice commands and Text-to-Speech (TTS) for reading out results, ensuring accessibility.

Detailed Actionable Guides: Presents information in a clean, structured format, including eligibility criteria, required documents, and a step-by-step application process.

Clean, Modern UI: A user-friendly interface designed for clarity and ease of use.

💻 Technology Stack
Backend: Python with the Flask framework, serving a REST API.

AI Engine: Google Gemini (gemini-flash-latest) for core reasoning and Natural Language Understanding.

Frontend: HTML5, CSS3, and modern JavaScript.

Voice Interface: The browser-native Web Speech API (SpeechRecognition and SpeechSynthesis).

🏗️ Architecture
For the hackathon, we implemented a robust "Presentation Mode" architecture to ensure a fast and flawless live demonstration.

Curated Knowledge Base: The AI's brain is a comprehensive, hand-crafted dataset of high-quality scheme information stored locally.

Prompt Engineering: We use an advanced prompt to instruct the Gemini model, providing it with the knowledge base and a strict set of reasoning rules (like the location-aware logic).

Flask API: The Python backend serves the user interface and orchestrates the communication with the Gemini API.

Dynamic Frontend: The index.html file communicates with our Flask API to fetch and display the AI-generated results dynamically.

🚀 Getting Started
To run this project locally, follow these steps:

**Clone the repository:**

**Bash**

git clone https://github.com/your-username/sahayak.git
cd sahayak
Create and activate a virtual environment:

**Bash**

python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate # On macOS/Linux
Install the required packages:

**Bash**

pip install Flask google-generativeai
Add your API Key:

Open the app.py file.

Find the line GOOGLE_API_KEY = "PASTE_YOUR_GEMINI_API_KEY_HERE".

Paste your own Google Gemini API key inside the quotes.

Run the application:

**Bash**

python app.py
Open your web browser and navigate to http://127.0.0.1:5000.

🤝 Our Team
This project is the result of a collaborative effort from our dedicated team for the Hack-AI-thon – 2025.

Aravind Ili (Avi) - Lead Developer & AI Architect

[Ankitha Namoju] - UI/UX & Frontend Specialist

[Charmi jahanavi] - Research & Content Lead

[Ruchith Barigala] - Data Pipeline & Backend Engineer

[Karthik Rapolu] - Project Manager & QA Lead

📜 License
This project is licensed under the MIT License. See the LICENSE file for details.
