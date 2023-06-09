import os
from flask import Flask, request

app = Flask(__name__)

# Function to increment the visit count and write IP address to file
def increment_visit_count(url):
    visits_file = 'visits.txt'  # File to store the visit count

    file_path = os.path.join(os.getcwd() + "\\" + 'visits.txt')

    print(file_path)

    # Check if the file exists
    if not os.path.exists(file_path):
        # If the file doesn't exist, create it and initialize the count to 0
        with open(file_path, 'w') as file:
            file.write('0')

    # Read the current visit count from the file
    with open(file_path, 'r') as file:
        try:
            visit_count = int(file.read())
        except ValueError:
            # Handle the case when the file contains non-integer data
            visit_count = 0

    # Increment the visit count
    visit_count += 1

    # # Write the updated visit count back to the file
    # with open(visits_file, 'w') as file:
    #     file.write(str(visit_count))

    # Retrieve the user's IP address
    user_ip = request.remote_addr

    # Write the IP address to the file
    with open(file_path, 'a') as file:
        file.write(f"\nVisit {visit_count} - User IP: {user_ip}")

    # Do further processing or logging if required
    # For example, you can log the IP address along with the visit count
    print(f"User IP: {user_ip}")

    # Redirect the user to the desired URL
    print(f"Location: {url}")
    return

@app.route('/')
def index():
    increment_visit_count('https://dev.brandemanager.com/digital-businesscard/36/Advocater/')
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True, port=7007)
