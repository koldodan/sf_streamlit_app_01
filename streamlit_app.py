import streamlit
import pandas

streamlit.title("Snowflake, GitHub, Streamlit, and Python")
streamlit.header("Love coding")
streamlit.text("In a beautiful Sunday morning!")
streamlit.text("Enjoy!")
streamlit.text("Well it is also time for breakfast 🍌🥭  :-)")

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
