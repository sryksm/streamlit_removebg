import streamlit as st
import time

st.title('Streamlit Text Input Examples')

name = st.text_input('enter your name:', '') # the second argument is the default value of the input field
feedback= st.text_area('enter your feedback:', '')
age = st.number_input('enter your age:', min_value=17, max_value=60, step=1)
date = st.date_input('select a date:')
timer = st.time_input('select a time:')

color = st.color_picker('pick a color')

st.write('Name:', name)
st.write('Feedback:', feedback)
st.write('Age:', age)
st.write('Date:', date)
st.write('Time:', time)
st.write('Color:', color)

html_code = """
        <h1 style='color: {};'>This is a color heading</h1>
        <p style='color: green;'>This is a green paragraph</p>
""".format(color)
st.markdown(html_code, unsafe_allow_html=True)

multiselect = st.multiselect('select multiple options:', ['apple', 'banana', 'orange', 'grape', 'watermelon']) 
st.write('You selected:', multiselect)

rating = st.slider('Rate our service:', min_value=0.0, max_value=10.0, step=0.25)  
st.write('Rating:', rating)


st.divider()

empty = st.empty()
empty.text('This is an empty container will be replaced in 7 seconds')    
time.sleep(7)
empty.text('This is a new text after 7 seconds')


progress = st.progress(0) # 0 means it starts the progress from 0
status = st.empty()

for i in range(100):
    time.sleep(0.05)
    progress.progress(i)
    status.text('Progress: {}%'.format(i))

with st.spinner('This is a spinner'):
    time.sleep(5)
    st.success('Done!')

st.snow()
st.balloons()

    
    