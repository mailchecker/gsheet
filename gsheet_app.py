import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandasql as psql

params = st.experimental_get_query_params()
golf_course_name = params.get("gname", ["sheet1"])[0]  # 'gname' 파라미터가 없는 경우 기본값
st.title("Read Google "+ golf_course_name  +" as DataFrame")

conn = st.experimental_connection("gsheets", type=GSheetsConnection)
df = conn.read(worksheet="sheet1")
st.dataframe(df)
if st.button("Update worksheet"):
  st.cache_data.clear()
  st.experimental_rerun()

df = psql.load_births()
if st.button("Create worksheet"):
    df = conn.create(
        worksheet="sheet3",
        data=df,
    )
    st.cache_data.clear()
    st.experimental_rerun()

# Display our Spreadsheet as st.dataframe
st.dataframe(df.head(10))






# streamlit_app.py
#import streamlit as st
#from streamlit_gsheets import GSheetsConnection

# Create a connection object.
#conn = st.connection("gsheets", type=GSheetsConnection)

#df = conn.read()
#df = conn.read(worksheet="sheet1")

# Print results.
#for row in df.itertuples():
#    st.write(f"{row.name} has a :{row.date}:")



#import streamlit as st
#from streamlit_gsheets import GSheetsConnection

#url = "https://docs.google.com/spreadsheets/d/1JDy9md2VZPz4JbYtRPJLs81_3jUK47nx6GYQjgU8qNY/edit?usp=sharing"

#conn = st.experimental_connection("gsheets", type=GSheetsConnection)

#data = conn.read(spreadsheet=url, usecols=[0, 1])
#st.dataframe(data)
