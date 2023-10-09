import streamlit as st
import requests
from bs4 import BeautifulSoup

# Function to scrape data from the URL
def scrape_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup

# Streamlit app
def main():
    # Set the title and description
    st.title("EV Charging Station Data Scraper")
    st.write("Enter the URL of the charging station page to scrape data.")

    # Input URL
    url = st.text_input("Enter URL:")

    if url:
        try:
            # Scrape data
            soup = scrape_data(url)

            # Find the HTML elements that contain the data you want to scrape.
            type_of_socket = soup.find_all('h6', class_='text-blue text-center')
            address_charging_station = soup.find_all('h6', class_='text-blue d-flex align-items-start')
            name = soup.find('h1')

            # Extract the data from the HTML elements.
            type_of_socket = [name.text for name in type_of_socket]
            address_charging_station = [place.text for place in address_charging_station]
            name = name.text

            # Display the data in Streamlit
            st.header("Scraped Data:")
            st.subheader("Name of Charging Station:")
            st.write(name)
            st.subheader("Type of Socket:")
            st.write(type_of_socket)
            st.subheader("Address of Charging Station:")
            st.write(address_charging_station)

        except Exception as e:
            st.error("An error occurred while scraping the data. Please check the URL and try again.")

if __name__ == '__main__':
    main()