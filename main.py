import streamlit as st
import openai
import pdfplumber

# Set your OpenAI API key here
openai.api_key = "YOUR_OPENAI_API_KEY"

def extract_text_from_pdf(uploaded_file):
    with pdfplumber.open(uploaded_file) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text

def generate_response(prompt, max_tokens=50):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=max_tokens
    )
    return response.choices[0].text.strip()

def main():
    st.title("PDF Chatbot")
    st.write("Upload a PDF file to chat with its contents.")

    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

    if uploaded_file is not None:
        pdf_text = extract_text_from_pdf(uploaded_file)
        st.write("PDF contents:")
        st.write(pdf_text)

        user_input = st.text_input("You: ")
        if st.button("Send"):
            chat_history = f"You: {user_input}\nPDF: {pdf_text}"
            response = generate_response(chat_history)
            st.write("PDF Chatbot:", response)

if __name__ == "__main__":
    main()
