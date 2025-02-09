import streamlit as st

st.title("Streamlit Text Display Example")
st.header("This is a Header")
st.subheader("This is a Subheader")
st.text("This is a simple text")
st.write("This is written using st.write()")
st.markdown("# This is a Markdown heading")
st.markdown("[Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)")
st.markdown("This is a Markdown paragraph with **bold** and *italic* text")
st.markdown("""
        1. step 1
        2. step 2
            
        - unordered step 1
        - step 2
            - substep 2.1    
""")
st.divider()
st.markdown("### HTML")
html_code = """
        <h1 style='color: blue;'>This is a blue heading</h1>
        <p style='color: green;'>This is a green paragraph</p>
"""
st.markdown(html_code, unsafe_allow_html=True)



