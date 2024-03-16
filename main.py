import streamlit as st

OPTIONS = ['Translate','Dictionary','Speech Recognition']


######################
st.title('AI Powered language assistant and poor learning system')
# Description of the language assistant
st.write('The solution proposed to address the challenge of languages and poor learning systems involves the integration of AI-driven technologies into educational processes')


#add columns
with st.sidebar:
    service = st.sidebar.selectbox('Choose Service', options=OPTIONS)


if service == 'Translate':
    st.text_input(label='Type in the Sentence to Translate')

    translate = st.button('Translate', help='Input the word here!')

    if translate:
        st.write('Translated Text:')
        st.write("Iperereza ryahindutse ku murongo mushya w'iperereza.")


if service == 'Dictionary':
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
        
if service == 'Speech Recognition':
    st.file_uploader('Upload Audio File')
    #Submit Button
    explain = st.button('Transcribe', help='Input the word here!')

    if explain:
    #Show the meaning of the word
        st.text('"INQUIRY" is an act of asking for information')


    #Play the pronounciation of the word
    #st.audio()








