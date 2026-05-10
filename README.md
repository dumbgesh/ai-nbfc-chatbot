# AI-Powered NBFC Customer Support Chatbot

A GenAI-powered chatbot built for a fictional NBFC (QuickLoan NBFC) to automate customer support and answer loan-related queries using LLMs.

## Overview

This project demonstrates how AI assistants can help financial businesses automate repetitive customer interactions such as:

* Loan eligibility questions
* EMI and repayment queries
* Documentation requirements
* Approval timelines
* Business loan support

The chatbot uses a structured FAQ knowledge base along with an LLM to generate accurate and contextual responses.

---

## Features

* AI-powered conversational assistant
* Loan & EMI query handling
* FAQ-based contextual responses
* Chat memory support
* Lead capture form
* Clean Streamlit UI
* Groq API integration
* Finance-focused use case

---

## Tech Stack

* Python
* Streamlit
* Groq API
* Llama 3.3 70B
* dotenv

---

## Project Structure

```plaintext id="p6v2nx"
ai-nbfc-chatbot/
│
├── app.py
├── faq_data.txt
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

---

## How It Works

1. User enters a loan-related query
2. The chatbot reads the FAQ knowledge base
3. The prompt and FAQ context are sent to the LLM
4. The model generates a contextual response
5. Lead information can be collected using the inquiry form

---

## Example Questions

* What documents are required for a personal loan?
* What is the minimum credit score required?
* Can freelancers apply for loans?
* How long does approval take?

---

## Future Improvements

* WhatsApp integration
* Voice-based assistant
* CRM integration
* Admin analytics dashboard
* Multi-language support
* Vector database retrieval

---

## Purpose

This project was built as part of a portfolio focused on AI solutions for fintech and NBFC businesses.
