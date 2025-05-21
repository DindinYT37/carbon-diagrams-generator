from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image
import base64
import io
import os

def create_html_file(html_content, css_content):
    # Create temporary HTML with embedded CSS
    full_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{
                margin: 0;
                padding: 20px;
                background: transparent;
            }}
            {css_content}
        </style>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """
    
    with open("temp.html", "w", encoding="utf-8") as f:
        f.write(full_html)
    
    return os.path.abspath("temp.html")

def html_to_png(html_file, output_file="carbon_table.png"):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1000,800")
    chrome_options.add_argument("--hide-scrollbars")
    chrome_options.add_argument("--transparent-background")
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    try:
        # Load the HTML file
        driver.get(f"file:///{html_file}")
        
        # Wait for the table to be visible
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(("class name", "isotope-table"))
        )
        
        # Get the table element
        table = driver.find_element("class name", "isotope-table")
        
        # Get screenshot of the table
        screenshot = table.screenshot_as_png
        
        # Convert to PIL Image
        img = Image.open(io.BytesIO(screenshot))
        
        # Create a new image with transparency
        img_with_alpha = img.convert("RGBA")
        
        # Save the image
        img_with_alpha.save(output_file, "PNG")
        
    finally:
        driver.quit()
        if os.path.exists("temp.html"):
            os.remove("temp.html")

def main():
    # Read HTML and CSS files
    with open("main.html", "r") as f:
        html_content = f.read()

    with open("style.css", "r") as f:
        css_content = f.read()
    
    # Create temporary HTML file
    html_file = create_html_file(html_content, css_content)
    
    # Convert to PNG
    html_to_png(html_file)

if __name__ == "__main__":
    main()