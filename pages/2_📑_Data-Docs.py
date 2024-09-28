import streamlit as st
import base64

# Set page configuration
st.set_page_config(page_title="न्यायवाणी", page_icon="👩🏼‍⚖️", layout="wide")

# Title and header
st.title("📑 Data & Documentations")

# Sidebar content
st.sidebar.markdown('<div style="text-align: center;"><span style="font-size: 10.5rem;">👩🏼‍⚖️</span></div>', unsafe_allow_html=True)
st.sidebar.markdown('<div style="text-align: center;"><span style="font-size: 2.5rem;">न्यायवाणी</span></div>', unsafe_allow_html=True)
st.sidebar.markdown('<div style="text-align: center;"><span style="font-size: 1.5rem;">"An AI LawBot: He Answers Your Legal Questions..."</span></div>', unsafe_allow_html=True)

# Function to create a download link for the PowerPoint or any file
def create_download_link(file_path, link_text):
    with open(file_path, "rb") as f:
        data = f.read()
    b64 = base64.b64encode(data).decode('utf-8')
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="{file_path}">{link_text}</a>'
    return href

# Provide a download link for the PPT
st.markdown("### Download the presentation:")
ppt_link = create_download_link("D:\Desktop\PROJs\न्यायवाणी\AI-LawBot\Docs\न्यायवाणी.pdf", "Click here to download the PPT presentation")
st.markdown(ppt_link, unsafe_allow_html=True)

# Function to load images as base64 and display them with explanations and download buttons
def load_image_base64(image_path):
    """Loads an image and encodes it in base64 for HTML display."""
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")

def image_with_explanation(image_path, explanation, dataset_path, dataset_name):
    img_base64 = load_image_base64(image_path)
    st.markdown(
        f"""
        <div style="text-align: center;">
            <img src="data:image/png;base64,{img_base64}" style="width:70%;">
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown(f"**{explanation}**")
    
    # Create a download button for the dataset
    dataset_link = create_download_link(dataset_path, f"Download {dataset_name}")
    st.markdown(dataset_link, unsafe_allow_html=True)
    st.markdown("---")

# Show images with explanations and download buttons below
st.markdown("### Explore Legal Topics:")
image_with_explanation('./images/indian_constitution.jpeg', "Indian Constitution: Fundamental principles that govern India.", 'path_to_dataset_1.csv', 'Indian Constitution Dataset')
image_with_explanation('./images/Equality.png', "Equality Rights: Learn about the rights ensuring equality for all citizens.", 'path_to_dataset_2.csv', 'Equality Rights Dataset')
image_with_explanation('./images/IPC.png', "Indian Penal Code: A comprehensive code intended to cover all substantive aspects of criminal law.", 'path_to_dataset_3.csv', 'Indian Penal Code Dataset')
image_with_explanation('./images/image.png', "Legal Procedures: Overview of the key procedures in the legal system.", 'path_to_dataset_4.csv', 'Legal Procedures Dataset')

# Footer content
st.markdown("---")
st.markdown('<div style="text-align: center;">© 2024 न्यायवाणी</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: center;">For more information, Follow us on <a href="https://github.com/ganeshmohane/NyayVaani">GitHub</a></div>', unsafe_allow_html=True)
