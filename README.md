# Hotel_Recommendation_AI
Hotel Recommendation AI is an intelligent hotel recommendation system that leverages multiple data sources and AI-driven insights to help users find the perfect hotel stay. The project integrates data from online booking platforms, processes search queries and results and generates comprehensive trip reports—all accessible through an interactive Streamlit web application.

Table of Contents
  Overview
  Project Structure
  Features
  Installation and Setup
  Usage
  Google Colab Integration
  Contributing
  License

Overview
Trip Adviser AI is designed to streamline the process of searching for, analyzing, and recommending hotels based on user-defined parameters such as destination, budget, trip duration, and travel type. The system gathers search queries and results from multiple platforms, processes hotel packages data, and then generates a detailed final report that highlights the best options. The interactive Streamlit interface allows users to easily input trip details, upload generated JSON/HTML files, and explore the results across different tabs.

Project Structure
  Hotel_adviser.ipynb
  Contains the exploratory analysis, data processing, and AI-engineering steps necessary for generating search queries, processing search results, and preparing    hotel package data.

  streamlit_app.py
  The main Streamlit application provides an intuitive user interface. Users can enter trip parameters, upload JSON report files, and view hotel search queries,    results, hotel packages, and the final report.
  (Refer to)

  step_1_search_queries.json
  JSON file with predefined search queries used to fetch hotel deals from various platforms.
  (Refer to )

  step_2_search_results.json
  JSON file that contains search results from online booking platforms with details like titles, URLs, snippets, and relevance scores.
  (Refer to ​)

  step_3_trip_packages.json
  JSON file with detailed hotel package data, including hotel name, location, price, amenities, and agent recommendations.
  (Refer to )

  step_4_trip_report.html
  A professionally formatted HTML report (using Bootstrap) summarizing the hotel recommendations and detailed analysis.
  (Refer to ​)

  trip_summary.json
  JSON file summarizing trip details (destination, budget, duration, etc.) and listing the top recommended hotel(s) based on the analysis.
  (Refer to ​)​

Features
  Customizable Trip Parameters:
  Users can specify destination country, city, budget, trip type, and duration via the interactive sidebar.

  Multi-Tab Interface:
  Search Queries: View the list of generated search queries.
  Search Results: Browse search results with detailed snippets and relevance scores.
  Hotel Packages: Examine hotel package details presented in card layouts with key information (name, location, rating, price, etc.).
  Final Report: View the final HTML report summarizing the recommendation analysis.

  Data Validation:
  Input validation functions to ensure that user inputs (such as budget and duration) adhere to expected formats.

  Google Colab Integration:
  Instructions provided within the app guide users on how to generate and export JSON output from Google Colab for seamless integration with the Streamlit app.

Installation and Setup
  1. Clone the Repository:
  git clone https://github.com/your_username/trip-adviser-ai.git
  cd trip-adviser-ai

2. Create and Activate a Virtual Environment:
  python -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate

3.Install Dependencies:
  pip install -r requirements.txt

Required libraries include:
  streamlit
  pandas
  requests
  pillow
  json
re

4. Run the Application:
  streamlit run streamlit_app.py

Usage
1. Set Trip Parameters:
  Use the sidebar in the Streamlit app to enter your desired destination, city, budget range, trip type, and duration.

2. Upload Files:
  Upload the required JSON files (search queries, search results, hotel packages) and the HTML report generated from your Google Colab session via the sidebar.

3. Navigate Through Tabs:
  Search Queries Tab: Review the search queries used.
  Search Results Tab: Expand and explore individual search results.
  Hotel Packages Tab: View detailed hotel package information presented in card format.
  Final Report Tab: See the final recommendation report rendered directly within the app.

4. Review and Book:
  Based on the recommendations, users can click through the hotel cards to visit booking pages and make reservations.

Google Colab Integration
For users who generate their data using Google Colab:
1. Run the hotel adviser script in Google Colab.
2. Export and download the output JSON files along with the HTML report.
3. Upload these files to the Streamlit app as per the instructions provided.
4. View and interact with the final analysis within the app.

Contributing
Contributions are welcome! If you would like to improve this project or add new features:
  Fork the repository.
  Create a new branch for your feature or bug fix.
  Submit a pull request with a detailed description of your changes.

License
This project is licensed under the MIT License. See the LICENSE file for details.
