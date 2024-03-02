
# Company Stock Visualizer

Welcome to the Company Stock Visualizer! This Streamlit web application allows you to visualize the stock data of various companies.

## Overview

The Company Stock Visualizer enables users to select a company from a list of options and specify the date range for which they want to analyze the stock data. Once the user selects a company and specifies the date range, they can click on the "Scrape" button to retrieve and visualize the stock data for the selected company within the specified date range.

## Features

- Select from a list of companies including Apple, Google, Tesla, Amazon, and more.
- Specify a custom date range for analyzing the stock data.
- Visualize the stock data with interactive charts.

## Installation

To run the Company Stock Visualizer locally, follow these steps:

1. Clone this repository to your local machine.

2. Install the required dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

4. Access the web application in your web browser at http://localhost:8501.

## Usage

1. Select a company from the dropdown list.
2. Choose a starting date and ending date for analyzing the stock data.
3. Click on the "Scrape" button to retrieve the stock data.
4. Visualize the stock data using the interactive charts.

## Technologies Used

- Python
- Streamlit
- Pandas DataReader

## Credits

- This project utilizes the Pandas DataReader library to retrieve stock data.
- Company stock data is sourced from Stooq (https://stooq.com/).

## Contributions

Contributions are welcome! If you have any suggestions, feature requests, or bug reports, feel free to open an issue or submit a pull request on GitHub.

## Credits

- This project utilizes the Pandas DataReader library to retrieve stock data.
- Company stock data is sourced from Stooq (https://stooq.com/).
- Special thanks to my teacher Nitish Singh for his invaluable guidance on pandas datetime and time series. You can find him on GitHub: [Nitish Singh](https://github.com/campusx-official).
