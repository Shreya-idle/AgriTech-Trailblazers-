import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Welcome to AgriTech! 👋",
    page_icon="👋",
    layout="wide"
)

# Custom CSS for styling
custom_css = """
<style>

h1, h2, h3, h4, h5 {
    text-align: center;
    color: #96aa2e;
}

hr {
    border: 2px solid #96aa2e;
    
}

main {
    font-size: 20px;
    font-family: Arial, sans-serif;
}

a {
    color: #007BFF;
    text-decoration: none;
}

</style>
"""

# Apply custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

# Header
st.markdown("<h1>Welcome to AgriTech! 👋</h1>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# Introduction
st.markdown("""
<div style="font-size: 20px;">
Welcome to AgriTech, your go-to tool for modern farming success! Explore data-driven crop suggestions, mixed cropping optimization, and government schemes information.

<strong style = "font-size:25px ; color: #FBB917 " ><u>Data-Driven Crop Suggestions:</u></strong>
<ul>
<li style = "font-size:20px " >Leverage data analysis for crop suggestions based on soil parameters like nitrogen, phosphorus, potassium, temperature, humidity, pH, and rainfall levels.</li>
<li style = "font-size:20px" >Provide insights into the consequences of growing each suggested crop, aiding informed land use decisions.</li>

<strong style = "font-size:25px ; color: #FBB917"><u>Mixed Cropping Optimization:</u></strong>
<li style = "font-size:20px" >Explore mixed cropping options to enhance soil health and manage pests effectively.</li>

<strong style = "font-size:25px ; color: #FBB917"><u>Government Schemes Information:</u></strong>
<li style = "font-size:20px" >Stay updated on available subsidies and grants through our app, ensuring enhanced agricultural productivity.</li>
<ul>
</div>
""", unsafe_allow_html=True)

# Resources
st.markdown("<h3>Our Resources:</h3>", unsafe_allow_html=True)
st.markdown("""
<div style = "border: 1px solid yellow;padding: 10px;border-radius: 25px">
<ul>
    <li style = "font-size:20px" ><a href='https://www.kaggle.com/datasets/aksahaha/crop-recommendation'>Dataset</a></li>
    <li style = "font-size:20px" >Crop Rotation Dataset: Generated through Bard</li>
    <li style = "font-size:20px" >Consequences dataset: Generated through Bard</li>
</ul>
<div>
""", unsafe_allow_html=True)
