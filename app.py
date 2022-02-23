import streamlit as st
import pickle
import numpy as np

with open('artifacts/encoder.pkl', 'rb') as f:
    encoder = pickle.load(f)

with open('artifacts/model.pkl', 'rb') as f:
    model = pickle.load(f)

def predict(x):
    x = np.array(x).reshape(1, -1)
    x[:, :-1] = encoder.transform(x[:, :-1])
    x = np.float32(x)
    y = model.predict(x)
    return round(y[0],2)

st.header("Developer Salary Estimator")
emp_options = ['freelance', 'full-time','part-time','other']
country_options = ['Australia', 'Brazil', 'Canada', 'France', 'Germany', 'India',
        'Italy', 'Netherlands', 'Poland', 'Russia', 'Spain', 'Sweden',
        'Switzerland', 'Turkey', 'UK', 'USA', 'other']
edu_options = ['Associate degree', 'Bachelor’s degree', 'Doctoral degree',
        'Master’s degree', 'Professional degree', 'School',
        'Secondary school', 'Some college','Other']
age_options = ['below 18', '18-24', '25-34', '35-44', '45-54', '55-64', 'above 65']
gen_options = ['man', 'other', 'woman']

col1, col2, col3 = st.columns(3)
with col1:
    emp = st.selectbox("Employment", emp_options)
    country = st.selectbox("Country", country_options)
with col2:
    edu = st.selectbox("Education", edu_options)
    age = st.selectbox("Age", age_options)
with col3:
    gender = st.selectbox("Gender", gen_options)
exp = st.slider("Experience", 0, 50)

x = [emp, country, edu, age, gender, exp]
y = predict(x)
st.subheader(f"Your's Estimated Salary: $ {y}")
