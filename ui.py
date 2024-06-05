import streamlit as st
import requests

def main():
    st.title("URL Shortener with QR Code")

    long_url = st.text_input("Enter a long URL:", value="")

    if st.button("Shorten URL"):
        response = requests.post("http://localhost:5000/api/shorten", json={"url": long_url})
        if response.status_code == 200:
            short_url = response.json()["short_url"]
            st.success(f"Shortened URL: http://localhost:5000/{short_url}")

            # Fetch and display the QR code
            qr_code_url = f"http://localhost:5000/api/qrcode/{short_url}"
            qr_code_image = requests.get(qr_code_url).content
            st.subheader("QR Code for Shortened URL")
            st.image(qr_code_image, caption="QR Code for Shortened URL")
        else:
            st.error("Failed to shorten the URL. Please try again.")

if __name__ == "__main__":
    main()