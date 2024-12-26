import streamlit as st
import pandas as pd
import plotly.express as px


def main_page():
    st.title("Streamlit IRIARTICO")
    st.write("This is a simple example of a Streamlit app.")
    st.write("Use the left sidebar to select a page to view.")


def data_visualization():
    st.title("Data Visualization")
    st.write("Please, upload a CSV file to visualize the data.")
    file = st.file_uploader("Upload a file (.csv)", type=["csv"])

    if file is not None:
        df = pd.read_csv(file)
        st.write("Data of the uploaded file:")
        st.write(df)

        st.write("Descriptive statistics:")
        st.write(df.describe())


def interactive_widgets():
    st.title("Interactive Widgets")
    st.write("Please, upload a CSV file to visualize the data.")
    file = st.file_uploader("Upload a file (.csv)", type=["csv"], key="2")

    if file is not None:
        df = pd.read_csv(file)
        st.write("Data of the uploaded file:")
        x_axis = st.selectbox("Select x-axis", df.columns)
        y_axis = st.selectbox("Select y-axis", df.columns)

        if st.button("Create Plot"):
            fig = px.bar(df, x=x_axis, y=y_axis, title=f"{y_axis} by {x_axis}")
            st.plotly_chart(fig)


st.sidebar.title("Navigation")
page = st.sidebar.selectbox(
    "Choose a page", ["Home", "Data Visualization", "Interactive Widgets"]
)

if page == "Home":
    main_page()
elif page == "Data Visualization":
    data_visualization()
elif page == "Interactive Widgets":
    interactive_widgets()
