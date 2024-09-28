import streamlit as st

st.set_page_config(page_title="न्यायवाणी", page_icon="👩🏼‍⚖️")
st.title("🤔 Frequently Asked Questions")
st.markdown("")

# SideBar
st.sidebar.markdown('<div style="text-align: center;"><span style="font-size: 10.5rem;">👩🏼‍⚖️</span></div>', unsafe_allow_html=True)
st.sidebar.markdown('<div style="text-align: center;"><span style="font-size: 2.5rem;">न्यायवाणी</span></div>', unsafe_allow_html=True)
st.sidebar.markdown('<div style="text-align: center;"><span style="font-size: 1.5rem;">"An AI LawBot: He Answers Your Legal Questions..."</span></div>', unsafe_allow_html=True)

# Question 1
st.subheader("Q1: What is IPC?")
st.write("A1: The Indian Penal Code (IPC) is the main criminal code of India. It defines various crimes and their punishments.")

# Question 2
st.subheader("Q2: What is the purpose of IPC?")
st.write("A2: The IPC aims to provide a comprehensive and standardized framework for defining offenses and prescribing penalties to maintain law and order in society.")

# Question 3
st.subheader("Q3: What is bailable and non-bailable offense?")
st.write("A3: A bailable offense allows the accused to secure bail and be released from custody before trial, while a non-bailable offense does not offer this option, requiring the accused to remain in custody until the trial concludes.")

# Question 4
st.subheader("Q4: Can I get bail for all offenses?")
st.write("A4: No, bail is not granted for all offenses. Non-bailable offenses, which are usually more serious, do not allow for bail unless specified by the law.")

# Question 5
st.subheader("Q5: How can I find out more about a specific IPC section?")
st.write("A5: You can ask NyayVaani about any specific IPC section, and it will provide detailed information including the definition, punishment, and whether it is bailable or non-bailable.")

# Footer
st.markdown("---")
st.markdown('<div style="text-align: center;">© 2024 न्यायवाणी</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: center;">For more information, Follow us on <a href="https://github.com/ganeshmohane/NyayVaani">GitHub</a></div>', unsafe_allow_html=True)
