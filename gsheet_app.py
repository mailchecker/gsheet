import streamlit as st
from streamlit_gsheets import GSheetsConnection

st.title("Read Google Sheet as DataFrame")

conn = st.experimental_connection("gsheets", type=GSheetsConnection)
df = conn.read(worksheet="sheet 1")

st.dataframe(df)





# streamlit_app.py
#import streamlit as st
#from streamlit_gsheets import GSheetsConnection

# Create a connection object.
#conn = st.connection("gsheets", type=GSheetsConnection)

#df = conn.read()

# Print results.
#for row in df.itertuples():
#    st.write(f"{row.name} has a :{row.date}:")



#import streamlit as st
#from streamlit_gsheets import GSheetsConnection

#url = "https://docs.google.com/spreadsheets/d/1JDy9md2VZPz4JbYtRPJLs81_3jUK47nx6GYQjgU8qNY/edit?usp=sharing"

#conn = st.experimental_connection("gsheets", type=GSheetsConnection)

#data = conn.read(spreadsheet=url, usecols=[0, 1])
#st.dataframe(data)
