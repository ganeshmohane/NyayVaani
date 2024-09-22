import os
os.environ["TRANSFORMERS_NO_TF"] = "1"

import streamlit as st
import pandas as pd
import re
from transformers import pipeline

# Load the IPC data from Excel
def load_data(file_path):
    return pd.read_excel(file_path)

# Define the function to match IPC codes in user queries
def get_ipc_info(ipc_data, user_query):
    # Look for IPC code in the query
    match = re.search(r"ipc (\d+)", user_query.lower())
    if match:
        ipc_code = int(match.group(1))
        ipc_info = ipc_data[ipc_data['IPC Code'] == ipc_code]
        if not ipc_info.empty:
            return f"**IPC {ipc_code}:** {ipc_info['Description'].values[0]}\n\n**Punishment:** {ipc_info['Punishment'].values[0]}"
        else:
            return "Sorry, I couldn't find that IPC code."
    else:
        return None

# Initialize the BERT QA pipeline (from HuggingFace's transformers)
qa_pipeline = pipeline("question-answering", model="bert-large-uncased-whole-word-masking-finetuned-squad")

def get_nlp_answer(question, context):
    # Use BERT to answer more general questions based on the legal context
    result = qa_pipeline(question=question, context=context)
    return result['answer']

# Sample context about IPC (you can customize this with more data)
legal_context = """
    The Indian Penal Code (IPC) is the official criminal code of India. It is a comprehensive law that covers all substantive aspects of criminal law. Section 375 of the IPC defines rape as sexual intercourse with a woman against her will or without her consent.
    Punishment for theft under IPC Section 378 is imprisonment which may extend to three years, or a fine, or both.
    Section 302 of the IPC pertains to punishment for murder, which is death or imprisonment for life, and a fine.
"""

# Streamlit UI
st.set_page_config(page_title="🤖 Law Chatbot", page_icon="🤖")

st.markdown('<div style="text-align: center;"><h1>🤖 न्यायवाणी</h1><p>An AI LawBot: He Answers Your Legal Questions...</p></div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: center;"><p>Hello! I am LawBot, here to help with your legal queries based on Indian law.</p></div>', unsafe_allow_html=True)

# Load the IPC data (replace with your actual file path)
ipc_data = load_data('path_to_your_excel_file.xlsx')

# User input
user_input = st.text_input("Ask me a legal question:")

# Process the user query
if user_input:
    # First, try to match the IPC code from the query
    ipc_answer = get_ipc_info(ipc_data, user_input)

    if ipc_answer:
        # If IPC-specific information is found, display it
        st.write("### Answer:")
        st.write(ipc_answer)
    else:
        # If no IPC-specific information is found, use BERT for NLP-based answering
        bert_answer = get_nlp_answer(user_input, legal_context)
        st.write("### Answer:")
        st.write(bert_answer)

    # Suggested actions (optional)
    st.write("### Suggested Actions:")
    st.write("""
    1. **Consult a Lawyer**: It's crucial to get legal representation to navigate the charges.
    2. **Understand Your Rights**: You have the right to be informed of the charges against you and to consult a lawyer.
    3. **Prepare Your Defense**: Gather any evidence or witnesses that can support your case.
    """)

# Footer
st.markdown("---")
st.markdown('<div style="text-align: center;">© 2024 LawBot</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: center;">For more information, Follow us on <a href="https://github.com/ganeshmohane/LawBot">GitHub</a></div>', unsafe_allow_html=True)


# import streamlit as st
# from transformers import pipeline


# # # Initialize the NLP pipeline (this should be replaced with your custom model)
# qa_pipeline = pipeline("question-answering")

# def get_answer(question):
#     # Replace this with your model's prediction function
#     context = """
#     The Indian Penal Code (IPC) defines theft under Section 378. According to this section:
#     "Whoever, intending to take dishonestly any movable property out of the possession of any person without that person's consent, moves that property in order to such taking, is said to commit theft."
#     For theft, the punishment can be imprisonment which may extend to three years, or a fine, or both.
#     """
#     result = qa_pipeline(question=question, context=context)
#     return result['answer']

# # Streamlit UI
# st.set_page_config(page_title="🤖 Law Chatbot", page_icon="🤖")

# st.markdown('<div style="text-align: center;"><h1>🤖 न्यायवाणी</h1><p>An AI LawBot : He Answers Your Legal Questions...<p/></div>', unsafe_allow_html=True)
# st.markdown('<div style="text-align: center;"><p>Hello! I am LawBot, here to help with your legal queries based on Indian law.</p></div>', unsafe_allow_html=True)

# # Blank Space
# st.markdown("<br>", unsafe_allow_html=True) 

# # Card Design
# col1, col2, col3, col4 = st.columns(4)

# # Define a reusable function to center the image and text
# def centered_image_and_text(image_path, description):
#     st.markdown(
#         f"""
#         <div style="text-align: center;">
#             <img src="data:image/png;base64,{st.image(image_path, use_column_width='always', output_format='auto')._img}" alt="{description}" style="width:25%;">
          
#         </div>
#         """,
#         unsafe_allow_html=True
#     )

# with col1:
#     centered_image_and_text('./images/image.png', 'Feature 1 Description')

# with col2:
#     centered_image_and_text('./images/Equality.png', 'Feature 2 Description')

# with col3:
#     centered_image_and_text('./images/IPC.png', 'Feature 3 Description')

# with col4:
#     centered_image_and_text('./images/image.png', 'Feature 4 Description')

# # with col2:
# #     st.markdown('<div style="text-align: center;"><img src="https://via.placeholder.com/100" alt="Logo 2" style="width:50%;"></div>', unsafe_allow_html=True)
# #     st.markdown('<div style="text-align: center;"><p>Feature 2 Description</p></div>', unsafe_allow_html=True)

# # with col3:
# #     st.markdown('<div style="text-align: center;"><img src="https://via.placeholder.com/100" alt="Logo 3" style="width:50%;"></div>', unsafe_allow_html=True)
# #     st.markdown('<div style="text-align: center;"><p>Feature 3 Description</p></div>', unsafe_allow_html=True)

# # with col4:
# #     st.markdown('<div style="text-align: center;"><img src="https://via.placeholder.com/100" alt="Logo 4" style="width:50%;"></div>', unsafe_allow_html=True)
# #     st.markdown('<div style="text-align: center;"><p>Feature 4 Description</p></div>', unsafe_allow_html=True)

# # Blank Space
# st.markdown("<br><br>", unsafe_allow_html=True) 

# # User input
# user_input = st.text_input("Ask me a legal question:")

# if user_input:
#     answer = get_answer(user_input)
#     st.write("### Answer:")
#     st.write(answer)

#     st.write("### Suggested Actions:")
#     st.write("""
#     1. **Consult a Lawyer**: It's crucial to get legal representation to navigate the charges.
#     2. **Understand Your Rights**: You have the right to be informed of the charges against you and to consult a lawyer.
#     3. **Prepare Your Defense**: Gather any evidence or witnesses that can support your case.
#     """)

# # Footer
# st.markdown("---")
# st.markdown('<div style="text-align: center;">© 2024 LawBot</div>', unsafe_allow_html=True)
# st.markdown('<div style="text-align: center;">For more information Follow us on <a href="https://github.com/ganeshmohane/LawBot">GitHub</a></div>', unsafe_allow_html=True)
