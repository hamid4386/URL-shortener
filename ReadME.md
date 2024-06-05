# URL Shortener with QR Code

This is a simple URL shortening application that allows users to shorten long URLs and generate QR codes for the shortened URLs.

## Features

- Shorten long URLs to short, easy-to-share URLs
- Generate QR codes for the shortened URLs
- Redirect users from the shortened URLs to the original long URLs

## Tech Stack

- Backend: Flask (Python)
- Frontend: Streamlit (Python)
- QR Code Generation: `qrcode` library

## Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
   `git clone https://github.com/hamid4386/url-shortener-with-qr-code.git`

2. Change to the project directory

3. Install the required dependencies:
   `pip install -r requirements.txt`



### Running the Application

1. Start the Flask backend:
   `python app.py`

The backend server will run at `http://localhost:5000`.

2. Start the Streamlit frontend:
   `streamlit run app.py`

The Streamlit app will open in your default web browser.

3. Use the URL Shortener:
- Enter a long URL in the input field.
- Click the "Shorten URL" button to generate a shortened URL.
- The shortened URL and its corresponding QR code will be displayed.


## License

This project is licensed under the [MIT License](LICENSE).