import streamlit as st
import pandas as pd

#sidebar
st.sidebar.write(
'''Find the bydel which fits you''')


st.sidebar.write('Author: [Thibaud Freyd](www.thibaudfreyd.com) in collaboration with Markus Fuchner and Baptiste Clément')


st.sidebar.write('''Version 1.0''')
#loading of the data

st.title('Find your Bydel')


#import data
df = pd.read_excel('1645692041728.xls')
#fix columns
df.columns = ['Bydel','Gender','Age',"2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019"]
#clean columns
df['Bydel'] = df['Bydel'].apply(lambda x: x.replace('Bydel ',''))



#df[df['Age']=='25-34 år'][['Bydel','2019']]
#list of bydels
bydels = df['Bydel'].unique()
bydels = list(bydels)
#list of age categories
age_categories= df['Age'].unique()
age_categories = list(age_categories)
#genders
genders = df['Gender'].unique()
genders = list(genders)

#selection box
st1, st2 = st.columns(2)

with st1:
    age_selected = st.selectbox('Your age', age_categories)
with st2:
    gender_selected = st.selectbox('Your Gender', genders)

#filtering df
df_temp = df[df['Age']==age_selected]
df_temp = df_temp[df_temp['Gender']==gender_selected]
df_temp = df_temp[['Bydel','2019']]

df_temp =df_temp.set_index('Bydel')

df_temp

st.bar_chart(df_temp,
             width=600,
             height=500)





#in order to hide the Menu
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

#st.markdown(hide_streamlit_style, unsafe_allow_html=True)