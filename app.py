import streamlit as st
import pandas as pd
import plotly.express as px

# Expanded sample data
data = {
    'Month': ['Feb', 'Mar', 'Apr', 'May'] * 3,
    'Platform': ['TikTok'] * 4 + ['Instagram'] * 4 + ['Reddit'] * 4,
    'Sentiment': ['Positive', 'Neutral', 'Positive', 'Positive',
                  'Neutral', 'Neutral', 'Negative', 'Neutral',
                  'Positive', 'Positive', 'Negative', 'Neutral'],
    'Mentions': [550, 120, 580, 600, 210, 180, 90, 100, 150, 160, 110, 130],
    'Theme': [
        'Great campaigns', 'Spicy not spicy', 'Great campaigns', 'Great campaigns',
        'Spicy not spicy', 'Sauce missing', 'Dry chicken', 'Service issues',
        'Great campaigns', 'Great campaigns', 'Dry chicken', 'Service issues'
    ]
}

df = pd.DataFrame(data)

st.set_page_config(page_title="BR Social Intelligence Dashboard", layout="wide")
st.title("🍦 Baskin Robbins Malaysia - Social Intelligence Dashboard")

# Filters
months = st.multiselect("Select Month(s):", sorted(df['Month'].unique()), default=sorted(df['Month'].unique()))
platforms = st.multiselect("Select Platform(s):", sorted(df['Platform'].unique()), default=sorted(df['Platform'].unique()))
filtered_df = df[df['Month'].isin(months) & df['Platform'].isin(platforms)]

# Sentiment Breakdown by Platform
st.subheader("📊 Sentiment Breakdown by Platform")
sentiment_by_platform = filtered_df.groupby(['Platform', 'Sentiment'])['Mentions'].sum().reset_index()
fig_sentiment = px.bar(sentiment_by_platform, x='Platform', y='Mentions', color='Sentiment',
                       barmode='group', color_discrete_map={'Positive': 'red', 'Neutral': 'black', 'Negative': 'gray'})
st.plotly_chart(fig_sentiment, use_container_width=True)

# Mentions Trend Over Time
st.subheader("📈 Mentions Trend Over Time")
trend = filtered_df.groupby(['Month'])['Mentions'].sum().reset_index()
fig_trend = px.line(trend, x='Month', y='Mentions', markers=True)
st.plotly_chart(fig_trend, use_container_width=True)

# Top Themes
st.subheader("🔥 Top Discussed Themes")
themes = filtered_df.groupby(['Theme', 'Sentiment'])['Mentions'].sum().reset_index()
fig_themes = px.bar(themes, x='Mentions', y='Theme', color='Sentiment', orientation='h',
                    color_discrete_map={'Positive': 'red', 'Neutral': 'black', 'Negative': 'gray'})
st.plotly_chart(fig_themes, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("Built for BR Malaysia · Inspired by Nando's SG Dashboard · Powered by Streamlit")
