import streamlit as st
from repos import trends
from topics import topics

st.title("Github Web Scrapping")

#get dataframe
trends_df = trends()
topics_df = topics()

#create coloumns
# cols = st.columns([1,1])

#create df to show data in df
# with cols[0]:
check1 = st.checkbox("Show github trending Repositories")
if check1:
    st.dataframe(trends_df)
    st.markdown("""<br>""",unsafe_allow_html= True)
# with cols[1]:
check2 = st.checkbox("Show github trending Topics")
if check2:
    st.dataframe(topics_df)