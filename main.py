import requests
import streamlit as st

#Url for picture of the day
url="https://api.nasa.gov/planetary/apod?api_key="
api_key="4Mt9Yym9S5eCRshugfzyY9RbgXyfITGgVaTu1y9h"

#Net URL
url_final= url + api_key

#get response if everything is ok
response=requests.get(url_final)

#get json content from the response of URL
content=response.json()
print(content)

#Get Image URL from json content
image_url=content["url"]
print(image_url)

#Get Image Description from json content
image_description=content["explanation"]
print(image_description)

#Send Content to webpage

st.set_page_config(page_title="Image of the Day",layout="wide")

