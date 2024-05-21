import streamlit as st

def main():
    # Read the contents of the HTML file
    with open("portfolio.html", "r", encoding="utf-8") as f:
        html_content = f.read()

    # Embed the HTML content within the Streamlit app
    st.components.v1.html(html_content, width=800, height=1200)

if __name__ == "__main__":
    main()
