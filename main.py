import streamlit as st

OPTIONS = ['Translate','Dictionary','Speech Recognition']

#add columns
with st.sidebar:
    st.sidebar.selectbox('Choose Service', options=OPTIONS)



# Title of the application
st.title('AI Powered language assistant and poor learning system')



# Description of the language assistant
st.write('The solution proposed to address the challenge of languages and poor learning systems involves the integration of AI-driven technologies into educational processes')


#Input Area of the word
st.text_input(label='Type in the word')

#Submit Button
explain = st.button('Explain the word', help='Input the word here!')

if explain:
    #Show the meaning of the word
    st.text('"INQUIRY" is an act of asking for information')


    #Play the pronounciation of the word
    #st.audio()


    #Show the examples of the word in use
    st.text('''
                 Examples of the word:
                 1.He made some inquiries and discovered she had gone to the Continent.
                 2.After a brief inquiry about the Christmas holiday, he returned to the subject of music.
                 3.This is the most difficult and shocking murder inquiry I have had to open in the last 25 years.
                 4.The Democratic Party has called for an independent inquiry into the incident.
                 5.The investigation has suddenly switched to a new line of inquiry.
                 ''')