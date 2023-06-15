import os
from flask import Flask, request

app = Flask(__name__)

# Function to increment the visit count and write IP address to file
def increment_visit_count(url):
    visits_file = 'visits.txt'  # File to store the visit count

    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Path to the visits.txt file
    file_path = os.path.join(current_dir, visits_file)

    # Retrieve the user's IP address and User-Agent
    user_ip = request.remote_addr
    user_agent = request.headers.get('User-Agent')

    # Check if the user's IP address is already present in the file
    with open(file_path, 'r') as file:
        ip_addresses = file.read()

    if user_ip in ip_addresses:
        # User with the same IP address has already visited
        print(f"User IP: {user_ip} - Already visited.")

        # Write the IP address and User-Agent to the file
        with open(file_path, 'a') as file:
            file.write(f"\nUser IP: {user_ip} - User-Agent: {user_agent}")
    else:
        # Read the current visit count from the file
        with open(file_path, 'r') as file:
            try:
                visit_count = int(file.read())
            except ValueError:
                # Handle the case when the file contains non-integer data
                visit_count = 0

        # Increment the visit count
        visit_count += 1

        # Write the updated visit count back to the file
        with open(file_path, 'w') as file:
            file.write(str(visit_count))

        # Write the IP address and User-Agent to the file
        with open(file_path, 'a') as file:
            file.write(f"\nVisit {visit_count} - User IP: {user_ip} - User-Agent: {user_agent}")

        # Do further processing or logging if required
        # For example, you can log the IP address along with the visit count and User-Agent
        print(f"User IP: {user_ip} - User-Agent: {user_agent}")

    # Redirect the user to the desired URL
    print(f"Location: {url}")
    return

@app.route('/')
def index():
    increment_visit_count('https://madhavplastomould.com/assets/img/madhav/my_mould.png')
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=7007)