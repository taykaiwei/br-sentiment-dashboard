import streamlit as st
import pandas as pd
import plotly.express as px

# Sample sentiment data
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    'Positive': [60, 55, 50, 65, 55],
    'Neutral': [35, 40, 30, 30, 35],
    'Negative': [5, 5, 20, 5, 10],
    'Highlight': [
        "Flavor-of-the-month excitement",
        "Snowman creations & CNY promos",
        "Dubai Chocolate Cake buzz",
        "Project 2025 engagement",
        "Kunafa trend & Raya treats"
    ],
    'Trending Topics': [
        "Club 31 app, new flavor",
        "CNY packaging, dry ice",
        "Dubai cake complaints",
        "Sundaes, community drive",
        "Kunafa, Ramadan promos"
    ]
}

df = pd.DataFrame(data)

st.set_page_config(page_title="Baskin Robbins MY Sentiment Tracker", layout="wide")
st.title("🇲🇾 Baskin Robbins Malaysia - Social Sentiment Dashboard (Jan–May 2025)")

# Sentiment Line Chart
fig_line = px.line(df, x='Month', y=['Positive', 'Neutral', 'Negative'],
                  markers=True, title="Monthly Sentiment Trends")
st.plotly_chart(fig_line, use_container_width=True)

# Sentiment Pie Chart for Selected Month
month_choice = st.selectbox("Select a Month for Breakdown:", df['Month'])
selected = df[df['Month'] == month_choice].iloc[0]
fig_pie = px.pie(
    names=['Positive', 'Neutral', 'Negative'],
    values=[selected['Positive'], selected['Neutral'], selected['Negative']],
    title=f"Sentiment Distribution - {month_choice} 2025"
)
st.plotly_chart(fig_pie, use_container_width=True)

# Monthly Highlights Table
st.subheader("📌 Monthly Highlights & Topics")
st.dataframe(df[['Month', 'Highlight', 'Trending Topics']], use_container_width=True)

# Footer
st.markdown("---")
st.markdown("Built by Head of Marketing | BR Malaysia · Powered by OpenAI + Streamlit")