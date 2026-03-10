# Selenium Google Patents Automation Task

This project automates searching and downloading a patent document from Google Patents using Selenium WebDriver in Python.

## Steps Automated

1. Launch Google Chrome using Selenium.
2. Navigate to Google Patents.
3. Search for the keyword **"stent"**.
4. Open the first patent result.
5. Download the patent PDF.
6. Verify that the PDF download was successful.

## Technologies Used

* Python
* Selenium WebDriver
* WebDriver Manager

## How to Run the Project

1. Install required dependencies:

pip install -r requirements.txt

2. Run the script:

python task.py

## Output

The script automatically downloads the patent PDF into a **downloads** folder and verifies the download.
