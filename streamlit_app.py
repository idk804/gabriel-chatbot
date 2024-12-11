import streamlit as st
from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI(
    api_key="youractualapikeyhere",  # Replace with your actual API key
    base_url="http://localhost:1337/v1"  # Ensure the base URL is correct
)

# Set the maximum token limit (4096 tokens)
MAX_TOKENS = 4096

# Streamlit UI
st.title("Custom OpenAI GPT Models Web Interface")
st.write("Select a model and enter a prompt to interact with the AI:")

# List of custom models (from your previous code)
available_models = [
    "o1-mini",
    "o1-preview",
    "gpt-4o-mini",
    "gpt-4o",
    "gpt-4",
    "gpt-3.5-turbo"
]

# Dropdown to select model
selected_model = st.selectbox("Choose a model:", available_models)

# Input box for user prompt
user_input = st.text_area("Enter your prompt:")

# Submit button
if st.button("Get Response"):
    if user_input:
        if selected_model:
            try:
                # Send the request to the OpenAI API with a max token limit
                response = client.chat.completions.create(
                    model=selected_model,  # Use selected model
                    messages=[{"role": "user", "content": user_input}],
                    max_tokens=MAX_TOKENS,  # Set the max token limit to 4096
                    stream=False  # Stream is disabled
                )

                # Display the AI response
                st.subheader("AI Response:")
                st.write(response.choices[0].message.content)

            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.warning("Please select a model.")
    else:
        st.warning("Please enter a prompt to get a response.")
