import streamlit as st
from streamlit_gsheets import GSheetsConnection

st.title("Read Google Sheet as DataFrame")

conn = st.experimental_connection("gsheets", type=GSheetsConnection)

#sheet_data = [{'Timestamp': '2024-01-03', 'User_Input': 'input', 'User_Output': 'output'}]
#conn.update(worksheet="sheet1", data=sheet_data)

df = conn.read(worksheet="sheet1")
st.dataframe(df)


if st.button('Refresh Data'):
    st.experimental_rerun()


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
