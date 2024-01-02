import streamlit as st
from streamlit_gsheets import GSheetsConnection

# Create a connection object.
conn = st.experimental_connection("gsheets", type=GSheetsConnection)

df = conn.read(worksheet="시트1")
st.dataframe(df)

# Print results.
#for row in df.itertuples():
#    st.write(f"{row.name} has a :{row.date}:")



#import streamlit as st
#from streamlit_gsheets import GSheetsConnection

#url = "https://docs.google.com/spreadsheets/d/1JDy9md2VZPz4JbYtRPJLs81_3jUK47nx6GYQjgU8qNY/edit?usp=sharing"

#conn = st.experimental_connection("gsheets", type=GSheetsConnection)

#data = conn.read(spreadsheet=url, usecols=[0, 1])
#st.dataframe(data)
