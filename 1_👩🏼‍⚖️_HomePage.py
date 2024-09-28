import streamlit as st
import pandas as pd
import re
import torch
from transformers import BertForSequenceClassification, BertTokenizer

# Streamlit UI
st.set_page_config(page_title="👩🏼‍⚖️न्यायवाणी", page_icon="👩🏼‍⚖️")


# Load the IPC data from CSV
def load_data(file_path):
    return pd.read_csv(file_path)

# Custom CSS for chat bubbles and message UI
st.markdown("""
    <style>
        .user-msg {
            background-color: #dcf8c6;
            color: black;
            padding: 10px;
            border-radius: 10px;
            margin: 5px;
            text-align: left;
            width: fit-content;
        }
        .bot-msg {
            background-color: #f1f0f0;
            color: black;
            padding: 10px;
            border-radius: 10px;
            margin: 5px;
            text-align: left;
            width: fit-content;
        }
        .response-box {
            background-color: white;  /* White background for responses */
            color: black;
            padding: 15px;
            border-radius: 10px;
            margin: 10px 0;  /* Add margin for separation */
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);  /* Subtle shadow for better visibility */
        }
    </style>
""", unsafe_allow_html=True)

def get_ipc_info(ipc_data, user_query):
    match = re.search(r"(\d{3})", user_query.lower())
    bail_status_prediction = None  # Initialize variable to store bail status

    if match:
        ipc_code = int(match.group(1))
        ipc_info = ipc_data[ipc_data['Description'].apply(lambda x: ' '.join(x.split()[:10])).str.contains(rf'\b{ipc_code}\b', case=False)]
        
        if not ipc_info.empty:
            # Get the first matched description for prediction
            description = ipc_info.iloc[0]['Description']
            bail_status_prediction = predict_bail_status(description)
            details = f"""
            <div class="response-box">
                <strong>IPC Code:</strong> {ipc_code}<br>
                <strong>Description:</strong> {description}<br>
                <strong>Punishment:</strong> {ipc_info.iloc[0]['Punishment']}<br>
                <strong>Predicted Bail Status:</strong> {bail_status_prediction}
            </div>
            """
            return details
    else:
        # No IPC code found; attempt to predict bail status using user query
        bail_status_prediction = predict_bail_status(user_query)
        return f'<div class="response-box">Sorry, I couldn\'t find a valid IPC code. However, based on your query, the predicted bail status is: <strong>{bail_status_prediction}</strong>.</div>'
    
    return None

def predict_bail_status(description):
    # Tokenize the input text
    inputs = tokenizer(description, return_tensors="pt", padding=True, truncation=True, max_length=512)
    
    # Make predictions
    with torch.no_grad():
        outputs = model(**inputs)
        predictions = torch.argmax(outputs.logits, dim=-1)
        print(predictions.item())
    
    # Map the predicted label back to bail status
    return "Bailable" if predictions.item() == 0 else "Non-Bailable"  # Adjust indices as needed based on your model's output


# # Custom CSS for chat bubbles and message UI
# st.markdown("""
#     <style>
#         .user-msg {
#             background-color: #dcf8c6;
#             color: black;
#             padding: 10px;
#             border-radius: 10px;
#             margin: 5px;
#             text-align: left;
#             width: fit-content;
#         }
#         .bot-msg {
#             background-color: #f1f0f0;
#             color: black;
#             padding: 10px;
#             border-radius: 10px;
#             margin: 5px;
#             text-align: left;
#             width: fit-content;
#         }
#     </style>
# """, unsafe_allow_html=True)

# SideBar
st.sidebar.markdown('<div style="text-align: center;"><span style="font-size: 10.5rem;">👩🏼‍⚖️</span></div>', unsafe_allow_html=True)
st.sidebar.markdown('<div style="text-align: center;"><span style="font-size: 2.5rem;">न्यायवाणी</span></div>', unsafe_allow_html=True)
st.sidebar.markdown('<div style="text-align: center;"><span style="font-size: 1.5rem;">"An AI LawBot: He Answers Your Legal Questions..."</span></div>', unsafe_allow_html=True)

st.markdown('<div style="text-align: center;"><h1>👩🏼‍⚖️न्यायवाणी</h1><p></p></div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: center;"><p>Hello! I am LawBot, here to help with your legal queries based on Indian Penal Codes.</p></div>', unsafe_allow_html=True)

# Load the IPC data
ipc_data = load_data('D:/Desktop/PROJs/न्यायवाणी/AI-LawBot/Data/cleaned_ipc_data.csv')

# Load the model and tokenizer
model = BertForSequenceClassification.from_pretrained(r'C:\Users\Ganesh\Downloads\model\model')
tokenizer = BertTokenizer.from_pretrained(r'C:\Users\Ganesh\Downloads\model\model')

# Initialize session state for conversation and user input
if 'conversation' not in st.session_state:
    st.session_state.conversation = []

# Process the user's query when the input is submitted
def submit_query():
    user_input = st.session_state.user_input
    ipc_answer = get_ipc_info(ipc_data, user_input)
    
    if ipc_answer:
        user_message = f"You: {user_input}"
        bot_response = f"न्यायवाणी: {ipc_answer}"
        st.write("")
    else:
        user_message = f"You: {user_input}"
        bot_response = "न्यायवाणी: Sorry, I couldn't find any relevant information.\nCurrently, we are working hard to make our LawBot more intelligent."
        st.write("")
    
    st.session_state.conversation.append({"user": user_message, "bot": bot_response})
    st.session_state.user_input = ""  # Clear the input after submission

# Display the conversation in chat format
for message in st.session_state.conversation:
    st.markdown(f'<div class="user-msg">{message["user"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="bot-msg">{message["bot"]}</div>', unsafe_allow_html=True)

# Input box for user's query
st.write("")
st.text_input("Ask me a legal question on IPC: ", placeholder="e.g., What is IPC 503 For?", key='user_input', on_change=submit_query)

# Footer
st.markdown("---")
st.markdown('<div style="text-align: center;">© 2024 न्यायवाणी</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: center;">For more information, Follow us on <a href="https://github.com/ganeshmohane/NyayVaani">GitHub</a></div>', unsafe_allow_html=True)
