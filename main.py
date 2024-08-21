import streamlit as st
from transformers import pipeline


# # Initialize the NLP pipeline (this should be replaced with your custom model)
qa_pipeline = pipeline("question-answering")

def get_answer(question):
    # Replace this with your model's prediction function
    context = """
    The Indian Penal Code (IPC) defines theft under Section 378. According to this section:
    "Whoever, intending to take dishonestly any movable property out of the possession of any person without that person's consent, moves that property in order to such taking, is said to commit theft."
    For theft, the punishment can be imprisonment which may extend to three years, or a fine, or both.
    """
    result = qa_pipeline(question=question, context=context)
    return result['answer']

# Streamlit UI
st.set_page_config(page_title="🤖 Law Chatbot", page_icon="🤖")

st.markdown('<div style="text-align: center;"><h1>🤖 न्यायवाणी</h1><p>An AI LawBot : He Answers Your Legal Questions...<p/></div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: center;"><p>Hello! I am LawBot, here to help with your legal queries based on Indian law.</p></div>', unsafe_allow_html=True)

# Blank Space
st.markdown("<br>", unsafe_allow_html=True) 

# Card Design
col1, col2, col3, col4 = st.columns(4)

# Define a reusable function to center the image and text
def centered_image_and_text(image_path, description):
    st.markdown(
        f"""
        <div style="text-align: center;">
            <img src="data:image/png;base64,{st.image(image_path, use_column_width='always', output_format='auto')._img}" alt="{description}" style="width:25%;">
          
        </div>
        """,
        unsafe_allow_html=True
    )

with col1:
    centered_image_and_text('./images/image.png', 'Feature 1 Description')

with col2:
    centered_image_and_text('./images/Equality.png', 'Feature 2 Description')

with col3:
    centered_image_and_text('./images/IPC.png', 'Feature 3 Description')

with col4:
    centered_image_and_text('./images/image.png', 'Feature 4 Description')

# with col2:
#     st.markdown('<div style="text-align: center;"><img src="https://via.placeholder.com/100" alt="Logo 2" style="width:50%;"></div>', unsafe_allow_html=True)
#     st.markdown('<div style="text-align: center;"><p>Feature 2 Description</p></div>', unsafe_allow_html=True)

# with col3:
#     st.markdown('<div style="text-align: center;"><img src="https://via.placeholder.com/100" alt="Logo 3" style="width:50%;"></div>', unsafe_allow_html=True)
#     st.markdown('<div style="text-align: center;"><p>Feature 3 Description</p></div>', unsafe_allow_html=True)

# with col4:
#     st.markdown('<div style="text-align: center;"><img src="https://via.placeholder.com/100" alt="Logo 4" style="width:50%;"></div>', unsafe_allow_html=True)
#     st.markdown('<div style="text-align: center;"><p>Feature 4 Description</p></div>', unsafe_allow_html=True)

# Blank Space
st.markdown("<br><br>", unsafe_allow_html=True) 

# User input
user_input = st.text_input("Ask me a legal question:")

if user_input:
    answer = get_answer(user_input)
    st.write("### Answer:")
    st.write(answer)

    st.write("### Suggested Actions:")
    st.write("""
    1. **Consult a Lawyer**: It's crucial to get legal representation to navigate the charges.
    2. **Understand Your Rights**: You have the right to be informed of the charges against you and to consult a lawyer.
    3. **Prepare Your Defense**: Gather any evidence or witnesses that can support your case.
    """)

# Footer
st.markdown("---")
st.markdown('<div style="text-align: center;">© 2024 LawBot</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: center;">For more information Follow us on <a href="https://github.com/ganeshmohane/LawBot">GitHub</a></div>', unsafe_allow_html=True)
