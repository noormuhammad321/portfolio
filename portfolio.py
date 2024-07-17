import streamlit as st
import os

import google.generativeai as genai



api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')


col1, col2 = st.columns(2)

with col1:
    st.subheader("Hi :wave:")
    st.title("I am Noor Muhammad")

with col2:
    st.image("images\\noor.jpg")

st.title(" ")


persona = """
        You are Noor Muhammad's AI bot. You help people answer questions about your self (i.e Noor Muhammad)
        Answer as if you are responding . dont answer in second or third person.
        If you don't know they answer you simply say "That's a secret"
        Here is more info about Noor Muhammad: 
        
        Murtaza Hassan is a freshie graduated and is a python developer.
        He has skills in python programming, and also data analysis and also machine learning and data scrapping and automation and also likes to teach students. 
        Noor obtained his Bachelor’s degree in computer science from bahria universiry karachi with cgpa of 3.89.
        He did his college/intermediate from Sir adamjee institute karachi.
        He is from karachi himself.
        He likes watching sports such as cricket.
        he also likes to play story mode games.
        Noor's Email: noor.muhammad2002@gmail.com 
        Noor's Linkdin: http://www.linkedin.com/in/noor-muhammad-1883bb235
        Noor's Github :https://github.com/noormuhammad321
        """

st.title("Noor's AI Bot")

user_question = st.text_input("Ask anything about me")
if st.button("ASK", use_container_width=400):
    prompt = persona +"Here is the question that the user asked: " +  user_question
    response = model.generate_content(prompt)
    st.write(response.text)




st.write(" ")
st.title("My Skills")
st.slider("Programming", 0, 100, 70)
st.slider("Teaching", 0, 100, 60)
st.slider("Logical thinking", 0, 100, 75)


st.subheader(" ")
st.write("CONTACT")
st.title("For any inquiries, email at:")
st.subheader("noor.muhammad2002@gmail.com")



