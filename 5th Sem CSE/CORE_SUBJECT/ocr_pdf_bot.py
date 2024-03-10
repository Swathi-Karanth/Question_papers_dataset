from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time

# Function to upload files to the online OCR tool
def upload_files(driver, file_paths):
    # Find the file input element
    file_input = driver.find_element_by_xpath("//input[@type='file']")
    
    # Upload each file
    for file_path in file_paths:
        file_input.send_keys(file_path)
        time.sleep(1)  # Wait for the upload to complete

# Function to convert the uploaded files
def convert_files(driver, output_format):
    # Select the desired output format
    output_format_select = driver.find_element_by_id("outputformat")
    output_format_select.send_keys(output_format)
    
    # Submit the form to start the conversion
    submit_button = driver.find_element_by_id("uploadbutton")
    submit_button.click()

# Main function
def main():
    # Path to the folder containing PDF files
    pdf_folder_path = "path/to/your/pdf/folder"
    
    # List all PDF files in the folder
    pdf_files = [os.path.join(pdf_folder_path, file) for file in os.listdir(pdf_folder_path) if file.endswith('.pdf')]
    
    # URL of the online OCR tool
    ocr_tool_url = "javascript:;"
    
    # Desired output format (e.g., "txt", "docx", "xlsx", etc.)
    output_format = "desired_format"
    
    # Initialize the WebDriver (replace "chrome" with "firefox" if using Firefox)
    driver = webdriver.Chrome()
    
    # Open the online OCR tool
    driver.get(ocr_tool_url)
    
    # Upload PDF files
    upload_files(driver, pdf_files)
    
    # Convert files to the desired format
    convert_files(driver, output_format)
    
    # Close the WebDriver
    driver.quit()

# Execute the main function
if __name__ == "__main__":
    main()
