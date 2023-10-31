import ipinfo
import sys

# Get the IP address from the command line
try:
    ip_address = sys.argv[1]
except IndexError:
    print("Usage: python script.py 98.252.254.109")
    sys.exit(1)

# Replace 'your_access_token_here' with your actual IPinfo access token
access_token = 'c5f361233901bc'

# Create a client object with the access token
handler = ipinfo.getHandler(access_token)

# Get the IP info
try:
    details = handler.getDetails(ip_address)
    # Print the IP info
    for key, value in details.all.items():
        print(f"{key}: {value}")
except ipinfo.exceptions.RequestQuotaExceededError:
    print("API request quota exceeded. Please check your IPinfo account settings.")
except ipinfo.exceptions.RequestDeniedError:
    print("API request denied. Please check your access token.")
except Exception as e:
    print(f"An error occurred: {str(e)}")


