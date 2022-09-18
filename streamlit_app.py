import streamlit
import pandas

streamlit.title("Snowflake, GitHub, Streamlit, and Python")
streamlit.header("Love coding")
streamlit.text("In a beautiful Sunday morning!")
streamlit.text("Enjoy!")
streamlit.text("Well it is also time for breakfast 🍌🥭  :-)")

# add fruit list from S3
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
## move below streamlit.dataframe(my_fruit_list)
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Orange','Peach'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
# Display the table on the page.
streamlit.dataframe(my_fruit_list)
