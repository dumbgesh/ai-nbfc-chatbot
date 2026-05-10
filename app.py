import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

# -----------------------------
# LOAD ENV VARIABLES
# -----------------------------
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.error("GROQ_API_KEY not found in .env file")
    st.stop()

# -----------------------------
# INITIALIZE GROQ CLIENT
# -----------------------------
client = Groq(api_key=api_key)

# -----------------------------
# LOAD FAQ DATA
# -----------------------------
try:
    with open("faq_data.txt", "r", encoding="utf-8") as file:
        faq_data = file.read()

except FileNotFoundError:
    st.error("faq_data.txt file not found")
    st.stop()

# -----------------------------
# STREAMLIT PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="QuickLoan NBFC AI Assistant",
    page_icon="💬",
    layout="centered"
)

# -----------------------------
# HEADER
# -----------------------------
st.title("💬 QuickLoan NBFC AI Assistant")

st.caption("Powered by AI • QuickLoan NBFC Virtual Assistant")

st.write(
    """
Ask questions about:
- Loans
- EMI
- Eligibility
- Documentation
- Approval process
- Business loans
"""
)

# -----------------------------
# CHAT MEMORY
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# DISPLAY OLD MESSAGES
# -----------------------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# -----------------------------
# USER INPUT
# -----------------------------
user_question = st.chat_input("Ask your question")

# -----------------------------
# PROCESS USER QUESTION
# -----------------------------
if user_question:

    # Show user message
    st.session_state.messages.append(
        {"role": "user", "content": user_question}
    )

    with st.chat_message("user"):
        st.write(user_question)

    # Generate AI response
    with st.chat_message("assistant"):

        with st.spinner("Generating response..."):

            prompt = f"""
You are an AI assistant for QuickLoan NBFC.

Answer ONLY from the FAQ data below.

Rules:
- Be concise and professional
- Do not make up information
- If information is unavailable, say:
  "Please contact our support team for exact details."

FAQ DATA:
{faq_data}

USER QUESTION:
{user_question}
"""

            try:

                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {
                            "role": "system",
                            "content": "You are a professional NBFC customer support assistant."
                        },
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                    temperature=0.3
                )

                answer = response.choices[0].message.content

                st.write(answer)

                # Save assistant response
                st.session_state.messages.append(
                    {"role": "assistant", "content": answer}
                )

            except Exception as e:
                st.error(f"Error: {e}")

# -----------------------------
# DIVIDER
# -----------------------------
st.divider()

# -----------------------------
# LEAD CAPTURE FORM
# -----------------------------
st.subheader("Need More Assistance?")

st.write(
    "Leave your details and our loan advisor will contact you shortly."
)

name = st.text_input("Your Name")
phone = st.text_input("Phone Number")
loan_amount = st.text_input("Interested Loan Amount")

if st.button("Submit Inquiry"):

    if name and phone:

        st.success(
            "Thank you! Our team will contact you shortly."
        )

    else:
        st.warning(
            "Please enter your name and phone number."
        )