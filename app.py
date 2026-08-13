import streamlit as st

def main():
  st.header("This is title")
  name = st.text_input("Enter your name")

  col1, col2 = st.columns(2, gap="xsmall")

  with col1:
   if st.button("Display my name", type="primary", key="btn1", width="stretch"):
    print("Hi", name)

  with col2:
   if st.button("Display my name", type="secondary", key="btn2", width="stretch"):
    print("Bye", name)


  st.markdown("""
    <div>
       <h1>Hello</h1>
    </div>

    <style>
        button{
            background:blue !important;
        }
    </style>

  """, unsafe_allow_html=True)

main()