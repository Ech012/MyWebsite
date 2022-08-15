import streamlit as st 
import requests as r
from streamlit_lottie import st_lottie
def load(url):
    req = r.get(url)
    if req.status_code != 200:
        return None
    return req.json()


link = load("https://assets3.lottiefiles.com/packages/lf20_3rwasyjy.json")
st.set_page_config(page_title="Streamlit App", page_icon=":wave:", layout="wide")
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
with st.container():
    st.subheader("Hello! :wave:")
    st.title("Hey, my name is echo and im a developer")
    st.markdown("""<h4>Just a normal guy who loves to program</h4>""", unsafe_allow_html=True)


with st.container():
    st.write("---")
    right, left = st.columns((2))
    with right:
        st.header("About me")
        st.write("##")
        st.markdown("<h4>I have one year of experience in progamming</h4>", unsafe_allow_html=True)
        st.markdown("<h4>I'm using the languages Python & Java", unsafe_allow_html=True)
        st.markdown("<h4>Currenlty now I'm learning Linux", unsafe_allow_html=True)
    with left:
        st_lottie(link, height=350, width=450)

with st.container():
    st.write("---")
    st.header("Urls")
    st.write("##")
    image, text = st.columns((1 ,19))
    with image:
        st.markdown("<img src='https://cdn-icons-png.flaticon.com/512/25/25231.png' alt='linux' width='40' height='40'/>", unsafe_allow_html=True)
        st.write(" ")
        st.write(" ")
        st.markdown("<img src='https://cdn.jsdelivr.net/npm/simple-icons@3.1.0/icons/discord.svg' alt='discord' width='40' height='40'/>", unsafe_allow_html=True)
    with text:
        st.markdown("<h4><a href='https://github.com/Ech012'>My Github</a></h4>", unsafe_allow_html=True)
        st.markdown("<h4><a href='https://discord.com/users/693457409082916984'>My Discord</a></h4>", unsafe_allow_html=True)

