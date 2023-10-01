import streamlit as sl

sl.set_page_config(page_title='Amaan',layout='centered')
sl.title('Hello Welcome')
name = sl.text_input('Enter your Name:')
age = sl.text_input('Enter Your Age:')
gender = sl.selectbox('Select your Gender',('Male','Female'))
submit = sl.button('Submit')



# values = {'Name':name,'Age':age,'Gender':gender}
# sl.download_button(label='Download Data',data = values.items() )
if submit:
    sl.write('NAME:',name)
    sl.write('AGE:',age)
    sl.write('GENDER:',gender)
pic = sl.camera_input("Click a picture")
if pic:
    sl.download_button(label='Download Image',data=pic ,mime='image/png')