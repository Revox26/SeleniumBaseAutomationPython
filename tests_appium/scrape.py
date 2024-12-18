import requests
from bs4 import BeautifulSoup

# Create a session object
session = requests.Session()

# URLs for login and the page you want to scrape
login_url = 'https://aws-staging.compassstarltd.com/login'
target_url = 'https://aws-staging.compassstarltd.com/suppliers-list'

# Login credentials (update these with actual values)
payload = {
    'email': 'jeremy@compassstarltd.com',
    'password': 'E4syl4ng2!'
}

try:
    # Perform the login
    response = session.post(login_url, data=payload)

    # Check if login was successful
    if response.ok:
        print("Success Login")



        # Now proceed to the target URL
        response = session.get(target_url)

        # Check if the request to the target URL was successful
        if response.ok:
            # Parse the HTML content with BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Example: Print the title of the target page
            print("Page Title:", soup.find_all('i', class_ = "fa fa-cart-plus lg-icon market-icon"))

            # You can now scrape or process the page content as needed
        else:
            print("Failed to retrieve the target page.")
    else:
        print("Failed Login")
        print("Response URL:", response.url)  # For debugging purposes
        print("Response Status Code:", response.status_code)  # For debugging purposes
        print("Response Text:", response.text)  # For debugging purposes

except Exception as e:
    print("An error occurred:", str(e))

# 'email': 'jeremy@compassstarltd.com',
    # 'password': 'E4syl4ng2!'

    #login_url = 'https://aws-staging.compassstarltd.com/login'
    # target_url = 'https://aws-staging.compassstarltd.com/suppliers-list'