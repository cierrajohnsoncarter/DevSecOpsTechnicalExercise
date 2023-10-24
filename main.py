import requests
import threading
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

# Creating an instance of the fast api application
app = FastAPI()

# Starting api server
def start_server():
    uvicorn.run(app, host="127.0.0.1", port=8001)


# Pydantic model for the DTO to validate data inputs
class JsonDTO(BaseModel):
    name: str
    type: str
    description: str
    date: str


# Starter data for GET request
starter_data = [
    JsonDTO(
        name="Elevation of Privilege",
        type="Platform",
        description="Security Feature Bypass",
        date="2022-01-01",
    ),
    JsonDTO(
        name="Broken Authentication",
        type="Platform",
        description="Identity Verification Issues",
        date="2021-05-11"
      ),
    JsonDTO(
        name="Excessive Data Exposure",
        type="Platform",
        description="Sensitive Data Leaks",
        date="2020-03-21"
      ),
    JsonDTO(
        name="Rate Limiting",
        type="Platform",
        description="Throttle Request Rate",
        date="2018-11-16"
      ),
    JsonDTO(
        name="Broken Authorization",
        type="Platform",
        description="Inadequate Access Control",
        date="2005-06-23"
      ),
    JsonDTO(
        name="Mass Assignment",
        type="Platform",
        description="Data Manipulation Risk",
        date="2022-08-08"
      ),
    JsonDTO(
        name="Security Misconfiguration",
        type="Platform",
        description="Setup Errors Lead",
        date="2020-12-04"
      ),
    JsonDTO(
        name="Injection Vulnerabilities",
        type="Platform",
        description="Code injection risks",
        date="2022-07-14"
      ),
    JsonDTO(
        name="Asset Management",
        type="Platform",
        description="Resource Control Gaps",
        date="2017-09-19"
      ),
    JsonDTO(
        name="Logging & Monitoring",
        type="Platform",
        description="Inadequate Tracking",
        date="2013-02-13"
      ),
    JsonDTO(
        name="Broken Object Authorization",
        type="Platform",
        description="Unauthorized Access Risk",
        date="2010-10-25"
      )
]

"""
    API ROUTES
"""

# Route for GET request (at least 10 records, in desc order by date)
@app.get("/api/data", response_model=List[JsonDTO])
def get_data():
    sorted_by_date = sorted(starter_data, key=lambda x: x.date, reverse=True)
    return sorted_by_date[:10]


# Route for POST request
@app.post("/api/data", response_model=List[JsonDTO])
def post_data(data: List[JsonDTO]):
    starter_data.extend(data)
    return data

"""
    THIS BOTTOM PORTION IS FOR COMMAND LINE APPLICATION
"""

# Base URL for FastApi server
BASE_URL = "http://127.0.0.1:8001"


def request_data():
    url = f"{BASE_URL}/api/data"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        for item in data:
            print(item)
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")


def submit_data(new_objects):
    url = f"{BASE_URL}/api/data"
    response = requests.post(url, json=new_objects)

    if response.status_code == 200:
        print("Data added successfully.")
    else:
        print(f"Failed to add data. Status code: {response.status_code}")

if __name__ == "__main__":
    import uvicorn

# Threading
    server_thread = threading.Thread(target=start_server)
    server_thread.start()

    while True:
        print("Welcome! Choose an option:")
        print("1. GET Data")
        print("2. POST Data")
        print("3. Exit")

        option = input("Enter the option number of the action you would like to take: ")

        if option == "1":
            request_data()
        elif option == "2":
            try:
                num_objects = int(input("How many objects would you like to add: "))
                new_objects = []

                for i in range(num_objects):
                    name = input("Enter the name: ")
                    type = input("Enter the type: ")
                    description = input("Enter the description: ")
                    date = input("Enter the date (YYYY-MM-DD): ")

                    input_object = {
                        "name": name,
                        "type": type,
                        "description": description,
                        "date": date
                    }
                    new_objects.append(input_object)

                submit_data(new_objects)
            except ValueError:
                print("Please enter a valid number.")
        elif option == "3":
            break
        else:
            print("Invalid option. Please enter 1, 2, or 3.")
