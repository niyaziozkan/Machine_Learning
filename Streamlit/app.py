import streamlit as st

#text/file
st.title("Streamlit Tutorial")
st.text("Hello Streamlit")

#header/subheader
st.header("This is a header")
st.subheader("This is a subheader")
st.subheader("This is a second subheader")

#markdown
st.markdown("This is a markdown")
st.markdown("**This is a bold markdown**")

#colourful text
st.success("Successfull")
st.error("Stop. That give an error")

#get help
st.help(range)

#writing text
st.write("Writing example text with write function")

#importing images
from PIL import Image
img = Image.open("dog.jpg")
st.image(img, caption="cute dog")

#importing videos (if we have video file)
#my_video=open(,"rb") 
#st.video(my_video)

#importing videos (from url)
st.video("dog.mp4")

#checkbox
if st.checkbox("Hide and Seek"):
    st.text("You checked i show")
    
#radio button
status=st.radio("Select your status", ("Graduate","Student"))

if status == "Graduate":
    st.success("Congrats")
else:
    st.info("Keep working")
    
#selectbox
path=st.selectbox("your path is", ["DS","FS","AWS/DEVOPS"])
st.write("Your path is", path)

#multiselect
profession = st.multiselect("Select your profession",("engineer","teacher","nurse","it engineer"))
st.write("Your professions are", profession)

#slider
count=st.slider("How many years of experience in IT", 1,10,step=3)

#button
st.button("Press this button")

if st.button("about program"):
    st.text("Streamlit is easy and fun")
else:
    st.text("Nothing to say")
    
#text input
firstname=st.text_input("Enter your Firstname")

if st.button("Submit"):
    st.success(firstname.title())
    
#text area
message = st.text_area("Enter your message", "type right here...")

if st.button("Submit-2"):
    st.info(message.title())
    
#date input
import datetime
today = st.date_input("Today is", datetime.datetime.now())

#time input
my_time = st.time_input("The time is",datetime.time(22,15))

#raw data
st.text("display text")
st.code("import pandas as pd")

#multiple line code
with st.echo():
    import numpy as np
    import pandas as pd
    import seaborn as sns

#sidebar
st.sidebar.title("This is a sidebar")
st.sidebar.button("Submit-3")

#importing DataFrame
import pandas as pd
df = pd.read_csv("cancer_classification.csv")
st.table(df.head())

st.write(df.head())

st.dataframe(df.head())