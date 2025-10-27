# app.py
import os
import json
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# --- THE GEMINI API KEY ---
GOOGLE_API_KEY = "AIzaSyBGf9rY5j4Mhp4olQPrEtAMZe0Btlg0R9o"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('models/gemini-flash-latest')

# --- FINAL, COMPLETE KNOWLEDGE BASE ---
schemes_data = [
    {
        "name_en": "Stand-Up India Scheme",
        "scheme_type": "Central Government",
        "desc_en": "Facilitates bank loans between ₹10 lakh and ₹1 Crore to SC/ST and/or woman entrepreneurs for setting up a new enterprise.",
        "eligibility_criteria_en": ["SC/ST and/or woman entrepreneurs, above 18 years of age.", "Loans are for greenfield projects (first-time ventures) only.", "Borrower should not be in default to any bank."],
        "documents_required_en": ["Identity Proof (Aadhaar, etc.)", "Address Proof", "Business Address Proof", "Project report"],
        "application_process_en": "The loan can be applied for directly at a bank branch, or through the Stand-Up India portal (standupmitra.in)."
    },
    {
        "name_en": "Kisan Credit Card (KCC)",
        "scheme_type": "Central Government",
        "desc_en": "A special credit scheme providing farmers timely access to loans for cultivation and other needs.",
        "eligibility_criteria_en": ["All farmers - individuals/joint borrowers.", "Tenant farmers, oral lessees & share croppers.", "Self Help Groups (SHGs) of farmers."],
        "documents_required_en": ["Completed Application form", "Identity proof", "Address proof", "Land documents"],
        "application_process_en": "Visit the nearest branch of a nationalized bank (e.g., SBI, PNB) with the filled form and all required documents."
    },
    {
        "name_en": "TS ePASS Scholarship (Post Matric)",
        "scheme_type": "State Government (Telangana)",
        "desc_en": "Provides financial assistance to SC, ST, BC, EBC, and Disabled students studying post-matriculation courses in Telangana.",
        "eligibility_criteria_en": ["Student from SC, ST, BC, EBC, or Disabled categories.", "Parental income must be below the prescribed limit.", "Studying in a recognized institution in Telangana."],
        "documents_required_en": ["Passport size photo", "Aadhaar Card", "Bank pass book", "Caste Certificate", "Income Certificate"],
        "application_process_en": "Applications are submitted online through the official Telangana ePASS website: telanganaepass.cgg.gov.in."
    },
    {
        "name_en": "Central Sector Scheme of Scholarships",
        "scheme_type": "Central Government",
        "desc_en": "Provides financial aid for meritorious students from economically weaker sections pursuing higher education anywhere in India.",
        "eligibility_criteria_en": ["Pursuing a regular course at a recognized institution.", "Family income must be less than ₹4.5 lakh per annum.", "Scored above 80th percentile in Class 12."],
        "documents_required_en": ["Class 12 Marksheet", "Income Certificate", "Aadhaar Card", "College Admission Proof"],
        "application_process_en": "Applications are submitted online through the National Scholarship Portal (NSP) at scholarships.gov.in."
    },{
        "name_en": "Pradhan Mantri Awas Yojana - Urban (PMAY-U)",
        "scheme_type": "Central Government",
        "desc_en": "Aims to provide affordable housing to the urban poor. It provides a credit-linked subsidy on home loan interest rates.",
        "eligibility_criteria_en": [
            "The beneficiary family should not own a pucca house in any part of India.",
            "Eligibility is based on annual income categories: Economically Weaker Section (EWS), Low Income Group (LIG), and Middle Income Groups (MIG-I & MIG-II).",
            "The scheme is applicable to all statutory towns as per the 2011 Census."
        ],
        "documents_required_en": [
            "Identity Proof (Aadhaar Card, PAN Card)",
            "Address Proof",
            "Proof of Income (Salary slips, ITR)",
            "Affidavit stating that the family does not own a pucca house."
        ],
        "application_process_en": "Applications can be submitted online through the PMAY-U official website (pmay-urban.gov.in) or offline by visiting the nearest Common Service Centre (CSC)."
    },
    {
        "name_en": "Pradhan Mantri MUDRA Yojana (PMMY)",
        "scheme_type": "Central Government",
        "desc_en": "Provides loans up to ₹10 lakh to non-corporate, non-farm small/micro-enterprises. Loans are given under three categories: Shishu, Kishore, and Tarun.",
        "eligibility_criteria_en": [
            "Any Indian Citizen who has a business plan for a non-farm sector income-generating activity.",
            "Activities include manufacturing, processing, trading, or the service sector.",
            "The credit requirement must be less than ₹10 lakh."
        ],
        "documents_required_en": [
            "Completed Application Form",
            "Identity & Address Proof (Aadhaar, Voter ID, etc.)",
            "Proof of business existence",
            "Quotations for machinery or other items to be purchased (if applicable)."
        ],
        "application_process_en": "Applicants can approach any MUDRA lending institution like Banks, NBFCs, or MFIs. A formal application with the business plan and required documents needs to be submitted to the loan officer."
    }
]

def get_ai_recommendations(situation, lang):
    schemes_context = json.dumps(schemes_data)
    prompt = f"""
    You are 'Sahayak', an expert AI assistant for Indian government schemes.

    **CRITICAL INSTRUCTIONS:**
    1.  Analyze the user's situation to find the most relevant scheme(s) from the knowledge base.
    2.  **LOCATION LOGIC:** If the user's situation does NOT mention a specific state (like Telangana), you MUST prioritize 'Central Government' schemes. Only recommend a 'State Government' scheme if the user's location is mentioned and it matches the scheme's state.
    3.  Structure your response as a JSON object with fields: "name", "scheme_type", "description", "eligibility_criteria" (list of strings), "documents_required" (list of strings), and "application_process".
    4.  If the application process has online steps, format it as a clear, step-by-step guide.
    5.  Respond with ONLY a valid JSON object inside a "schemes" list. If no schemes are a good match, return an empty list.

    ---
    **Knowledge Base:**
    {schemes_context}
    ---
    **User's Situation:**
    "{situation}"
    ---
    """
    try:
        response = model.generate_content(prompt)
        json_response_text = response.text.strip().replace("```json", "").replace("```", "")
        parsed_json = json.loads(json_response_text)
        for scheme in parsed_json.get("schemes", []):
            if isinstance(scheme.get("eligibility_criteria"), str):
                scheme["eligibility_criteria"] = [item.strip() for item in scheme["eligibility_criteria"].split('\\n') if item.strip()]
            if isinstance(scheme.get("documents_required"), str):
                scheme["documents_required"] = [item.strip() for item in scheme["documents_required"].split('\\n') if item.strip()]
        return parsed_json
    except Exception as e:
        print(f"AN ERROR OCCURRED: {e}")
        return {}

@app.route("/")
def index(): return render_template("index.html")

@app.route("/get_scheme", methods=["POST"])
def get_scheme():
    data = request.get_json()
    situation = data.get("situation", "").lower()
    lang = 'en'
    ai_response = get_ai_recommendations(situation, lang)
    if ai_response and ai_response.get("schemes"):
        return jsonify(ai_response)
    else:
        fallback_msg = "I couldn't find a suitable scheme based on your situation. Could you please provide more details?"
        myScheme_url = f"https://www.myscheme.gov.in/search?q={situation.replace(' ', '%20')}"
        return jsonify({"fallback_message": fallback_msg, "myScheme_url": myScheme_url})

if __name__ == "__main__": app.run(debug=True)