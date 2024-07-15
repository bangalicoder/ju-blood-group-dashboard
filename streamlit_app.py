import streamlit as st
import pandas as pd

# Load your CSV file
@st.cache
def load_data(file):
    return pd.read_csv(file)

# Main function to run the Streamlit app
def main():
    st.title('Blood Group Dashboard')

    # Upload CSV file
    st.sidebar.header('Upload your CSV file')
    uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"])

    if uploaded_file is not None:
        # Load data into a DataFrame
        df = load_data(uploaded_file)

        # Display the DataFrame
        st.subheader('Raw data')
        st.write(df)

        # Filter by blood group
        selected_blood_group = st.sidebar.selectbox('Select blood group', df['BloodGroup'].unique())
        filtered_df = df[df['BloodGroup'] == selected_blood_group]

        # Filter by city
        selected_city = st.sidebar.selectbox('Select city', df['City'].unique())
        filtered_df = filtered_df[filtered_df['City'] == selected_city]

        # Display filtered data
        st.subheader('Filtered data')
        st.write(filtered_df)

        # Basic statistics
        st.subheader('Basic statistics')
        st.write(filtered_df.describe())

if __name__ == '__main__':
    main()
