import streamlit as st

st.image('https://play-lh.googleusercontent.com/ZyWNGIfzUyoajtFcD7NhMksHEZh37f-MkHVGr5Yfefa-IX7yj9SMfI82Z7a2wpdKCA=w240-h480-rw')
st.title("String App")
message = st.text_area("Enter some text")
button = st.button("Process text")

if button:
    st.write(message)
if st.sidebar.checkbox("Show words"):
    words = message.split()
    st.write(words)
if st.sidebar.checkbox("character count"):
    for char in message:
        st.write(f'{char} : {message.count(char)}')
