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

# Function to create a download link for a file
def create_download_link(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    b64 = base64.b64encode(data).decode('utf-8')
    return f"data:application/octet-stream;base64,{b64}"

# Section for downloading documents
st.markdown("### Downloadable Documents")

# Presentation PDF
st.markdown("#### LawBot Presentation")
st.markdown("This presentation provides an overview of the LawBot project, including its features, objectives, and implementation details. It serves as an introductory resource for understanding how the LawBot operates.")
if st.button("Download the Presentation PDF"):
    ppt_link = create_download_link("D:\Desktop\PROJs\न्यायवाणी\AI-LawBot\Docs\न्यायवाणी.pdf")
    st.markdown(f'<a href="{ppt_link}" download="न्यायवाणी.pdf">Click here to download the presentation</a>', unsafe_allow_html=True)

st.markdown("---")  # Separator

# IPC Data CSV
st.markdown("#### IPC Data CSV")
st.markdown("This CSV file contains cleaned data from the Indian Penal Code (IPC). It includes various sections, articles, and relevant details useful for legal analysis and understanding.")
if st.button("Download IPC Data CSV"):
    ipc_data_link = create_download_link("D:\Desktop\PROJs\न्यायवाणी\AI-LawBot\Data\cleaned_ipc_data.csv")
    st.markdown(f'<a href="{ipc_data_link}" download="cleaned_ipc_data.csv">Click here to download IPC Data</a>', unsafe_allow_html=True)

st.markdown("---")  # Separator

# Questions & Answers CSV
st.markdown("#### Questions & Answers CSV")
st.markdown("This file contains a collection of question-answer pairs related to legal topics that the LawBot can use to provide accurate responses to user queries.")
if st.button("Download Q&A CSV"):
    qa_data_link = create_download_link("D:\Desktop\PROJs\न्यायवाणी\AI-LawBot\Data\lawbot_qa_pairs.csv")
    st.markdown(f'<a href="{qa_data_link}" download="lawbot_qa_pairs.csv">Click here to download Q&A Data</a>', unsafe_allow_html=True)

st.markdown("---")  # Separator

# IPC PDF
st.markdown("#### IPC Document")
st.markdown("The Indian Penal Code (IPC) document provides comprehensive coverage of criminal law in India. This PDF outlines various offenses and penalties as defined in the IPC.")
if st.button("Download IPC Document"):
    ipc_pdf_link = create_download_link("Data/Indian Penal Codes.pdf")
    st.markdown(f'<a href="{ipc_pdf_link}" download="Indian_Penal_Codes.pdf">Click here to download IPC Document</a>', unsafe_allow_html=True)

# Footer content
st.markdown("---")
st.markdown('<div style="text-align: center;">© 2024 न्यायवाणी</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: center;">For more information, Follow us on <a href="https://github.com/ganeshmohane/NyayVaani">GitHub</a></div>', unsafe_allow_html=True)
