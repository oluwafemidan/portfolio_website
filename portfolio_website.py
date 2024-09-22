import streamlit as st
import google.generativeai as genai

api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

col1, col2 = st.columns(2)

with col1:
    st.subheader("Hi :wave:")
    st.title("I am Ajala Oluwafemi Daniel")
    st.markdown("""
<a href="https://www.linkedin.com/in/oluwafemi-daniel-ajala-406911172/">
    <img src="https://brand.linkedin.com/content/dam/me/business/en-us/brand-site/v2/bg/LI-Bug.svg" width="20" height="20" />
</a>
<a href="https://x.com/ajala14055">
    <img src="X-logo.png" width="20" height="20" />
</a>
<a href="https://github.com/oluwafemidan">
    <img src="https://github.com/images/logo/github-icon.svg" width="20" height="20" />
</a>
""", unsafe_allow_html=True)



with col2:
    st.image("images/Daniel.png")

persona = """
        You are Ajala AI bot. You help people answer questions about your self (i.e Ajala)
        Answer as if you are responding . dont answer in second or third person.
        If you don't know they answer you simply say "That's a secret"
        Here is more info about Ajala: 
         
        Ajala Oluwafemi Daniel is a passionate Data Scientist, ML Engineer and AI enthusiast!
        He runs one of the largest YouTube channels in the field of Computer Vision,
        educating over 3 Million developers,
        hobbyists and students. Ajala obtained his Bachelor’s degree in
        Technology Education(Automobile Engineering) and a National Diploma in Chemical Engineering 
        and later specialized in the field of Data Scientist, ML Engineering, Natural Processing Language, 
        Computer Vision, Deep Learning Engineer. He is from Nigeria.
        He is also a serial entrepreneur having launched several
        successful ventures including CVZone, which is a one stop solution for learning 
        and building vision projects. Prior to starting his entrepreneurial career, 
        Murtaza worked as a university lecturer and a design engineer, evaluating 
        and developing rapid prototypes of US patents.
 
        
        Ajala's Email: ajalaoluwafemidaniel@gmail.com 
        Ajala's X: https://x.com/ajala14055
        Ajala's Linkedin: https://www.linkedin.com/in/oluwafemi-daniel-ajala-406911172/
        Ajala's Github : https://github.com/oluwafemidan
        """

st.title(" ")

st.title("Ajala's AI Bot")


user_question = st.text_input("Ask anything about me")
if st.button("ASK", use_container_width=400):
    prompt = persona +"Here is the question that the user asked: " + user_question
    response = model.generate_content(prompt)
    st.write(response.text)


st.title(" ")

# Animated Elements
st.write("Scroll down to learn more about me!")
st.animation("images/scroll.gif", width=50, height=50)

# Custom Fonts and Colors
st.markdown("""
<style>
    .font-custom {
        font-family: 'Montserrat', sans-serif;
        color: #333;
    }
</style>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.subheader("Youtube Channel")
    st.write("- Largest Computer Vision Channel")
    st.write("- 400K+ Subscribers")
    st.write("- Over 150 Free Tutorials")
    st.write("- 1.5 Million+ Views")
    st.write("- 1.5 Million Hours+ Watch time")

with col2:
    st.video("https://youtu.be/16S2InYp4nI")

st.title(" ")

st.title("My Setup")
st.image("images/workspace.jpg")

st.write(" ")
st.title("My Skills")
programming = st.slider("Programming", 0, 100, 70)
Teaching = st.slider("Teaching", 0, 100, 89)
Robotics = st.slider("Robotics", 0, 100, 60)

st.write()

st.title("Gallery")

col1, col2, col3 = st.columns(3)

with col1:
    st.image("images/g1.jpg")
    st.image("images/g2.jpg")
    st.image("images/g3.jpg")

with col2:
    st.image("images/g4.jpg")
    st.image("images/g5.jpg")
    st.image("images/g6.jpg")

with col3:
    st.image("images/g7.jpg")
    st.image("images/g8.jpg")
    st.image("images/g9.jpg")

st.write(" ")
st.write("CONTACT")
st.title("For any inquiries, email at:")
st.subheader("ajalaoluwafemidaniel@gmail.com ")





