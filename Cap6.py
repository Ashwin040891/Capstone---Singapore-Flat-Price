import streamlit as st
import datetime as dt
import json
import numpy as np
import pickle

def regression_model(test_data):
    #with open(r'Decision_Tree_Cap6.pkl', 'rb' ) as file:
    with open(r'XGBRegressor_Cap6.pkl', 'rb' ) as file:
        model = pickle.load(file)
        data = model.predict(test_data)[0] ** 2
        return data
    
with open(r'Category_Columns_Encoded_Data.json', 'r') as file:
    data = json.load(file)

st.set_page_config(page_title = "Singapore Resale Flat Prices Predicting",
                   page_icon = "",
                   layout = "wide",
                   initial_sidebar_state = "expanded",
                   menu_items = None)

st.title(":red[Singapore Resale] :blue[Flat Prices] :orange[Prediction]")

col1, col2 = st.columns(2, gap='large')

with col1:

    date = st.date_input("Select the **Item Date**", min_value= dt.date(1990, 1, 1))

    town = st.selectbox('Select the **Town**', data['town'])

    flat_type = st.selectbox('Select the **Flat Type**', data['flat_type'])

    block = st.selectbox('Select the **Block Type**', data['block']) 

    street_name = st.selectbox('Select the **Street Name**', data['street_name'])

with col2:

    storey_range = st.selectbox('Select the **Storey Range**', data['storey_range'])

    floor_area_sqm = st.number_input('Enter the **Floor Area** in square meter', min_value = 1.0)

    flat_model	= st.selectbox('Select the **flat_Model**', data['flat_model'])

    lease_commence_date	= st.number_input('Enter the **Lease Commence Year**', min_value = 1966.0, max_value= 2022.0)
        
    remaining_lease	= st.selectbox('Select the **Remainig Lease**', data['remaining_lease'])

storey = storey_range.split(' TO ')

#if remaining_lease == 'Not Specified':
#    is_remaining_lease = 0
#else:
#    is_remaining_lease = 1

test_data =[[date.month, data['town'][town], data['flat_type'][flat_type], data['block'][block], data['street_name'][street_name],
             data['flat_model'][flat_model], lease_commence_date, data['remaining_lease'][remaining_lease], date.year,
             int(storey[0]), int(storey[1]), np.sqrt(floor_area_sqm)]]

st.markdown('Click below button to predict the **Flat Resale Price**')
prediction = st.button('**Predict**')

if prediction and test_data:
  st.markdown(f"### :bule[Flat Resale Price is] :green[$ {round(regression_model(test_data),3)}]")

  st.markdown(f"### :bule[Flat Resale Price in INR] :green[₹ {round(regression_model(test_data)*61.32,3)}]")