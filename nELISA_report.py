import streamlit as st
import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv('simulated_nELISA_data.csv')  # Change to your actual file path

# Streamlit UI
st.title("📊 nELISA Data Interactive Report")
st.write("Explore and analyze nELISA data dynamically.")

# Dropdown for selecting a protein
protein = st.selectbox("🔬 Select a Protein:", df.columns[3:])

# Boxplot visualization
fig = px.box(df, x="Group", y=protein, color="Group",
             title=f"{protein} Concentration by Group", points="all")

st.plotly_chart(fig)

# Show dataset table (optional)
if st.checkbox("📂 Show Data Table"):
    st.dataframe(df)

# Add summary statistics
st.subheader("📊 Summary Statistics")
st.write(df.groupby("Group")[protein].describe())

st.sidebar.header("🔍 Filter Options")
if st.sidebar.checkbox("Filter by Time Point"):
    time_points = df["Time_Point"].unique()
    selected_time = st.sidebar.multiselect("Select Time Points:", time_points, default=time_points)
    df = df[df["Time_Point"].isin(selected_time)]
    st.write(f"Showing data for selected time points: {selected_time}")

# Re-display the filtered boxplot
fig_filtered = px.box(df, x="Group", y=protein, color="Group", title=f"{protein} Concentration by Group (Filtered)", points="all")
st.plotly_chart(fig_filtered)

st.write("Developed with ❤️ using Streamlit & Plotly")

