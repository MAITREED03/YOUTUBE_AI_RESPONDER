import streamlit as st
import pandas as pd
from transformers import pipeline

# Load a smaller, open-source model for text generation
def load_model():
    # Using GPT-2 as an example (smaller and open-source)
    return pipeline("text-generation", model="gpt2")

# Generate a response using the model
def generate_response(model, comment):
    prompt = f"You are a YouTube AI responder. Reply thoughtfully to this comment: {comment}"
    response = model(prompt, max_length=100, num_return_sequences=1)
    return response[0]['generated_text']

def main():
    st.title("YouTube AI Responder")
    
    # Load dataset
    df = pd.read_csv("YoutubeCommentsDataSet.csv").dropna()
    
    # Sidebar: Show sample data
    st.sidebar.subheader("Dataset Preview")
    st.sidebar.dataframe(df.head(10))
    
    # Load model
    model = load_model()
    
    # User Input
    user_comment = st.text_area("Enter a YouTube comment:")
    if st.button("Generate Response"):
        if user_comment:
            response = generate_response(model, user_comment)
            st.subheader("AI Response:")
            st.write(response)
        else:
            st.warning("Please enter a comment.")
    
if __name__ == "__main__":
    main()