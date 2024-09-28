import os
import streamlit as st
import pandas as pd
import re
import base64



# Load the IPC data from CSV
def load_data(file_path):
    return pd.read_csv(file_path)

def get_ipc_info(ipc_data, user_query):
    # Look for a three-digit number (IPC code) in the user's query
    match = re.search(r"(\d{3})", user_query.lower())
    if match:
        ipc_code = int(match.group(1))  # Extract the IPC code as an integer
        
        # Limit the search to the first 10 words of the Description column
        ipc_info = ipc_data[ipc_data['Description'].apply(lambda x: ' '.join(x.split()[:10])).str.contains(rf'\b{ipc_code}\b', case=False)]

        if not ipc_info.empty:
            # Return all relevant IPC information as a formatted string
            details = []
            for _, row in ipc_info.iterrows():
                details.append(
                    f"**IPC Code:** {ipc_code}\n\n"
                    f"**Description:** {row['Description']}\n\n"
                    f"**Punishment:** {row['Punishment']}\n\n"
                    f"**Bail Status:** {row.get('Bail Status', 'Not specified')}\n"
                )
            return "\n".join(details)
        else:
            return "Sorry, I couldn't find that IPC code in the descriptions."
    return None

# Streamlit UI
st.set_page_config(page_title="👩🏼‍⚖️न्यायवाणी", page_icon="👩🏼‍⚖️")

# SideBar
st.sidebar.markdown('<div style="text-align: center;"><span style="font-size: 10.5rem;">👩🏼‍⚖️</span></div>', unsafe_allow_html=True)
st.sidebar.markdown('<div style="text-align: center;"><span style="font-size: 2.5rem;">न्यायवाणी</span></div>', unsafe_allow_html=True)
st.sidebar.markdown('<div style="text-align: center;"><span style="font-size: 1.5rem;">"An AI LawBot: He Answers Your Legal Questions..."</span></div>', unsafe_allow_html=True)

st.markdown('<div style="text-align: center;"><h1>👩🏼‍⚖️न्यायवाणी</h1><p></p></div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: center;"><p>Hello! I am LawBot, here to help with your legal queries based on Indian Penal Codes.</p></div>', unsafe_allow_html=True)
# Function to load and encode an image in base64 format
# def load_image_base64(image_path):
#     with open(image_path, "rb") as img_file:
#         return base64.b64encode(img_file.read()).decode("utf-8")

# # Define a reusable function to center the image (without the description)
# def centered_image(image_path):
#     # Load the image as base64 string
#     img_base64 = load_image_base64(image_path)
    
#     # Display the image in the center using HTML
#     st.markdown(
#         f"""
#         <div style="text-align: center;">
#             <img src="data:image/png;base64,{img_base64}" style="width:90%;">
#         </div>
#         """,
#         unsafe_allow_html=True
#     )

# # Layout with four columns
# col1, col2, col3, col4 = st.columns(4)

# # Display images in each column
# with col1:
#     centered_image('./images/indian_constitution.jpeg')

# with col2:
#     centered_image('./images/Equality.png')

# with col3:
#     centered_image('./images/IPC.png')

# with col4:
#     centered_image('./images/image.png')
    
# Blank Space
# st.markdown("<br><br>", unsafe_allow_html=True) 

# Load the IPC data
ipc_data = load_data('D:/Desktop/PROJs/न्यायवाणी/AI-LawBot/Data/cleaned_ipc_data.csv')

# User input
# Title for the question prompt
st.markdown(
    """
    <h4 >Ask me a legal question on IPC:</h4>
    """, 
    unsafe_allow_html=True
)
user_input = st.text_input("",placeholder="e.g., What is IPC 503 For?")


# Process the user query
if user_input:
    # Try to match the IPC code
    ipc_answer = get_ipc_info(ipc_data, user_input)

    if ipc_answer:
        st.write("### Answer:")
        st.write(ipc_answer)
    else:
        st.write("### Answer:")
        st.write("Sorry, I couldn't find any relevant information.\n Currently we are working hard to make our LawBot more Intelligent.")

    # Suggested actions
    st.write("### Suggested Actions:")
    st.write("""
    1. **Consult a Lawyer**: It's crucial to get legal representation to navigate the charges.
    2. **Understand Your Rights**: You have the right to be informed of the charges against you and to consult a lawyer.
    3. **Prepare Your Defense**: Gather any evidence or witnesses that can support your case.
    """)

# Footer
st.markdown("---")
st.markdown('<div style="text-align: center;">© 2024 न्यायवाणी</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: center;">For more information, Follow us on <a href="https://github.com/ganeshmohane/NyayVaani">GitHub</a></div>', unsafe_allow_html=True)

