import streamlit as st
st.title('PyUtilities')
st.write("Hi eveyone this is my first web aplication, Pyutilities. The pyutilities web aplication is a collection of usefull mathematical tools such as perimeter, area, pythogoras and etc.")
with st.form("my_form_rect"):
   st.subheader('Rectangle')
   rectangle_height =st.number_input("Height", min_value=None, max_value=None, value="min",  label_visibility="visible")
   rectangle_width =st.number_input("Width", min_value=None, max_value=None, value="min",  label_visibility="visible")
   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
       rect_area = rectangle_height*rectangle_width
       st.write("Area is: ",rect_area)
       rect_perimeter = (rectangle_width*2)+(rectangle_height*2)
       st.write("perimeter  is: ",rect_perimeter)
with st.form("my_form"):
   st.subheader('Square')
   square_side =st.number_input("Side length", min_value=None, max_value=None, value="min",  label_visibility="visible")
   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
       square_area = square_side**2
       st.write("Area is: ",square_area)
       square_perimeter = square_side*4
       st.write("perimeter  is: ",square_perimeter)
          
