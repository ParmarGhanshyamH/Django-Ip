# import os
# from flask import Flask, request
#
# app = Flask(__name__)
#
# # Function to increment the visit count and write IP address to file
# def increment_visit_count(url):
#     visits_file = 'visits.txt'  # File to store the visit count
#
#     current_dir = os.path.dirname(os.path.abspath(__file__))
#
#     # Path to the visit.txt file
#     file_path = os.path.join(current_dir, visits_file)
#
#     # Check if the file exists
#     if not os.path.exists(file_path):
#         # If the file doesn't exist, create it and initialize the count to 0
#         with open(file_path, 'w') as file:
#             file.write('0')
#
#     # Read the current visit count from the file
#     with open(file_path, 'r') as file:
#         try:
#             visit_count = int(file.read())
#         except ValueError:
#             # Handle the case when the file contains non-integer data
#             visit_count = 0
#
#     # Increment the visit count
#     visit_count += 1
#
#     # # Write the updated visit count back to the file
#     # with open(visits_file, 'w') as file:
#     #     file.write(str(visit_count))
#
#     # Retrieve the user's IP address
#     user_ip = request.remote_addr
#
#     # Write the IP address to the file
#     with open(file_path, 'a') as file:
#         file.write(f"\nVisit {visit_count} - User IP: {user_ip}")
#
#     # Do further processing or logging if required
#     # For example, you can log the IP address along with the visit count
#     print(f"User IP: {user_ip}")
#
#     # Redirect the user to the desired URL
#     print(f"Location: {url}")
#     return
#
#
# @app.route('/')
# def index():
#     increment_visit_count('https://madhavplastomould.com/assets/img/madhav/my_mould.png')
#     return 'Hello, World!'
#
# if __name__ == '__main__':
#     app.run(host="localhost",debug=True, port=7007)




import os
from flask import Flask, request

app = Flask(__name__)

# Function to increment the visit count and write IP address to file
def increment_visit_count(url):
    visits_file = 'visits.txt'  # File to store the visit count

    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Path to the visit.txt file
    file_path = os.path.join(current_dir, visits_file)

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

    # Retrieve the user's IP address
    user_ip = request.remote_addr

    # Check if the user's IP address is already present in the file
    with open(file_path, 'r') as file:
        ip_addresses = file.read()

    if user_ip in ip_addresses:
        # User with the same IP address has already visited
        print(f"User IP: {user_ip} - Already visited.")
    else:
        # Increment the visit count
        visit_count += 1

        # Write the updated visit count back to the file
        with open(file_path, 'w') as file:
            file.write(str(visit_count))

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
    increment_visit_count('https://madhavplastomould.com/assets/img/madhav/my_mould.png')
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=7007)