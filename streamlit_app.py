import streamlit as st

st.title('PyUtilities')
st.write("Hi eveyone this is my first web aplication, Pyutilities. The pyutilities web aplication is a collection of usefull mathematical tools such as perimeter, area, pythogoras and etc.")



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
          