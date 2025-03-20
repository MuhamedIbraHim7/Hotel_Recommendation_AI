import streamlit as st
import pandas as pd
import json
import os
import requests
from PIL import Image
import base64
import re

# Set page config
st.set_page_config(
    page_title="Trip Adviser AI",
    page_icon="🏨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1E88E5;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #424242;
        margin-bottom: 1rem;
    }
    .card {
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 1rem;
        background-color: #f8f9fa;
    }
    .highlight {
        background-color: #e3f2fd;
        padding: 0.5rem;
        border-radius: 5px;
    }
    .hotel-card {
        border: 1px solid #e0e0e0;
        border-radius: 10px;
        padding: 1rem;
        margin-bottom: 1rem;
    }
    .price-tag {
        background-color: #4CAF50;
        color: white;
        padding: 0.3rem 0.6rem;
        border-radius: 5px;
        font-weight: bold;
    }
    .rating-star {
        color: #FFC107;
    }
</style>
""", unsafe_allow_html=True)

# Function to load JSON data
def load_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        st.error(f"Error loading data: {e}")
        return None

# Function to validate budget format
def validate_budget(budget):
    return bool(re.match(r'^\$?\d+\s*-\s*\$?\d+$', budget))

# Function to validate duration
def validate_duration(duration):
    try:
        days = int(duration)
        return days > 0
    except ValueError:
        return False

# Function to display hotel packages
def display_hotel_packages(packages_data):
    if not packages_data or "packages" not in packages_data:
        st.warning("No hotel packages found.")
        return
    
    # Create columns for hotel cards
    col1, col2 = st.columns(2)
    
    for i, package in enumerate(packages_data["packages"]):
        with col1 if i % 2 == 0 else col2:
            with st.container():
                st.markdown(f"""
                <div class="hotel-card">
                    <h3>{package.get('hotel_name', 'Unknown Hotel')}</h3>
                    <p>📍 {package.get('location', 'Location not specified')}</p>
                    <p><span class="price-tag">${package.get('price', 'Price not available')}</span></p>
                    <p>⭐ Rating: {package.get('rating', 'N/A')}/5</p>
                    <p>🍽️ Meals: {package.get('included_meals', 'Not specified')}</p>
                    <a href="{package.get('booking_url', '#')}">Book Now</a>
                </div>
                """, unsafe_allow_html=True)
                
                if package.get('activities'):
                    with st.expander("Activities"):
                        for activity in package.get('activities', []):
                            st.markdown(f"- {activity}")

# Function to render HTML content
def render_html_report(html_content):
    st.components.v1.html(html_content, height=600, scrolling=True)

# Main function
def main():
    st.markdown("<h1 class='main-header'>Trip Adviser AI</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Find your perfect hotel stay with AI assistance</p>", unsafe_allow_html=True)
    
    # Sidebar for inputs
    st.sidebar.header("Trip Parameters")
    
    country_name = st.sidebar.text_input("Destination Country", "Thailand")
    city_name = st.sidebar.text_input("Desired City", "Bangkok")
    
    budget = st.sidebar.text_input("Budget (e.g., $200-$1000)", "$200-$800")
    if budget and not validate_budget(budget):
        st.sidebar.error("Invalid budget format. Please use format like $200-$1000")
    
    trip_type = st.sidebar.selectbox(
        "Trip Type",
        ["luxury", "adventure", "family", "business", "romantic", "budget"]
    )
    
    trip_duration = st.sidebar.number_input("Trip Duration (days)", min_value=1, max_value=30, value=5)
    
    # File uploader for JSON data
    st.sidebar.markdown("---")
    st.sidebar.header("Upload Results")
    st.sidebar.markdown("Upload JSON files from Google Colab output:")
    
    uploaded_search_queries = st.sidebar.file_uploader("Search Queries JSON", type="json", key="search_queries")
    uploaded_search_results = st.sidebar.file_uploader("Search Results JSON", type="json", key="search_results")
    uploaded_trip_packages = st.sidebar.file_uploader("Trip Packages JSON", type="json", key="trip_packages")
    uploaded_html_report = st.sidebar.file_uploader("HTML Report", type="html", key="html_report")
    
    # Create tabs
    tab1, tab2, tab3, tab4 = st.tabs(["Search Queries", "Search Results", "Hotel Packages", "Final Report"])
    
    with tab1:
        st.markdown("<h2 class='sub-header'>Search Queries</h2>", unsafe_allow_html=True)
        if uploaded_search_queries:
            search_queries = json.load(uploaded_search_queries)
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            for i, query in enumerate(search_queries.get("queries", [])):
                st.markdown(f"<p><b>Query {i+1}:</b> {query}</p>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.info("Upload search queries JSON file to view results")
    
    with tab2:
        st.markdown("<h2 class='sub-header'>Search Results</h2>", unsafe_allow_html=True)
        if uploaded_search_results:
            search_results = json.load(uploaded_search_results)
            for i, result in enumerate(search_results.get("results", [])):
                with st.expander(f"{i+1}. {result.get('title', 'No Title')}"):
                    st.markdown(f"**URL:** {result.get('url', 'No URL')}")
                    st.markdown(f"**Snippet:** {result.get('snippet', 'No Snippet')}")
                    st.markdown(f"**Score:** {result.get('score', 'N/A')}")
                    st.markdown(f"**Search Query:** {result.get('search_query', 'No Query')}")
        else:
            st.info("Upload search results JSON file to view results")
    
    with tab3:
        st.markdown("<h2 class='sub-header'>Hotel Packages</h2>", unsafe_allow_html=True)
        if uploaded_trip_packages:
            trip_packages = json.load(uploaded_trip_packages)
            display_hotel_packages(trip_packages)
        else:
            st.info("Upload trip packages JSON file to view hotel options")
    
    with tab4:
        st.markdown("<h2 class='sub-header'>Final Report</h2>", unsafe_allow_html=True)
        if uploaded_html_report:
            html_content = uploaded_html_report.read().decode("utf-8")
            render_html_report(html_content)
        else:
            st.info("Upload HTML report file to view the final report")
    
    # Instructions for Colab integration
    st.markdown("---")
    with st.expander("How to use with Google Colab"):
        st.markdown("""
        1. Run the original Trip Adviser script in Google Colab
        2. Download the output JSON files from the Colab output directory
        3. Upload the files to this Streamlit app using the sidebar
        4. View the results in the respective tabs
        """)

if __name__ == "__main__":
    main()
