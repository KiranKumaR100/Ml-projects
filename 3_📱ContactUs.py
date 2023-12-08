import webbrowser

import streamlit as st


st.set_page_config(
    page_title="ContactUs",
    page_icon='📱',
)

st.title('Contact')
st.write('Click Below to Contact')

if st.button('Click here'):
    link_url = ''
    webbrowser.open(link_url)
