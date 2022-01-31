import streamlit as st
import numpy as np 
import pandas as pd 
#from PIL import Image
import time

st.title('Streamlit introduction')

st.write('DataFrame')

df = pd.DataFrame({
    '1st Row': [1,2,3,4],
    '2nd Row': [10,20,30,40]
})

st.dataframe(df.style.highlight_max(axis=0), width=300, height=200)

df = pd.DataFrame(
    np.random.rand(20,3),
    columns=['a', 'b', 'c']
)

st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)

df = pd.DataFrame(
    np.random.rand(100,2)/[50,50] + [35.69, 139.70],
    columns=['lat', 'lon']
)
st.map(df)

st.write('Interactive Widgets')

#if st.checkbox('Show Image'):
    #img = Image.open('sample.jpeg')
    #st.image(img, caption='picture', use_column_width=True)

option = st.selectbox(
    'what is your favorite number?', 
    list(range(1,10))
)
'your favorite number is', option

text = st.text_input('what is your favorite word?')
'your favorite word is', text

condition = st.slider('your mood is', 0, 100, 1)
'your mood:', condition

left_column, right_column = st.columns(2)
button = left_column.button('print on right')
if button:
    right_column.write('this is right')

expander = st.expander('inquiry')
expander.write('this is inquiry')


st.write('show progress bar')
'start!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!'

