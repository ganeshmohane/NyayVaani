import streamlit as st


st.set_page_config(page_title="न्यायवाणी", page_icon="👩🏼‍⚖️")
st.title("☎️Contact Us")



# SideBar
st.sidebar.markdown('<div style="text-align: center;"><span style="font-size: 10.5rem;">👩🏼‍⚖️</span></div>', unsafe_allow_html=True)
st.sidebar.markdown('<div style="text-align: center;"><span style="font-size: 2.5rem;">न्यायवाणी</span></div>', unsafe_allow_html=True)
st.sidebar.markdown('<div style="text-align: center;"><span style="font-size: 1.5rem;">"An AI LawBot: He Answers Your Legal Questions..."</span></div>', unsafe_allow_html=True)


# Embed Google Form using an iframe
google_form_url = "https://docs.google.com/forms/d/e/1FAIpQLSeElVKdMJjDsp7GaRpqOTJv5CDMiXvp4tRo_cNXl8lvMcgPPQ/viewform?embedded=true"
st.components.v1.iframe(google_form_url, width=640, height=910, scrolling=False)



# Footer
st.markdown("---")
st.markdown('<div style="text-align: center;">© 2024 न्यायवाणी</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: center;">For more information, Follow us on <a href="https://github.com/ganeshmohane/NyayVaani">GitHub</a></div>', unsafe_allow_html=True)

