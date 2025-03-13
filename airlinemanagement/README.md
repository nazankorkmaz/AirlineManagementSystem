# Airline Management System API

This project is a backend system for managing airplanes, flights, and reservations in an airline. The API allows users to manage airplane details, flight schedules, and make reservations.

## Table of Contents

- [Technologies](#technologies)
- [Setup Instructions](#setup-instructions)
- [API Endpoints](#api-endpoints)
  - [Airplanes](#airplanes)
  - [Flights](#flights)
  - [Reservations](#reservations)
- [Validation](#validation)
- [Testing with Postman](#testing-with-postman)
- [Postman Collection](#postman-collection)
- [Requirements](#requirements)

## Technologies

This project uses the following technologies:

- **Django** - A high-level Python web framework
- **Django Rest Framework** - Toolkit for building Web APIs
- **SQLite** - A lightweight database used for development
- **Postman** - For testing the API endpoints

## Setup Instructions

Follow the steps below to set up the project locally:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/airline-management-system.git
   cd airline-management-system

2. **Create and activate a virtual environment:**

        python -m venv venv
  
      For Windows

        venv\Scripts\activate
      For Mac/Linux

        source venv/bin/activate

3. **Install dependencies:**

    pip install -r requirements.txt

4. **Apply migrations:**

    python manage.py migrate

5. **Run the development server:**

    python manage.py runserver

6. **Visit the API:**

    The API should now be available at http://127.0.0.1:8000/.

**API Endpoints**

    Airplanes :

        GET /airplanes/ - Get all airplanes
        GET /airplanes/{id}/ - Get airplane details by ID
        POST /airplanes/ - Create a new airplane
        PUT /airplanes/{id}/ - Update an existing airplane
        DELETE /airplanes/{id}/ - Delete an airplane

    Flights:

        GET /flights/ - Get all flights
        GET /flights/{id}/ - Get flight details by ID
        POST /flights/ - Create a new flight
        PUT /flights/{id}/ - Update an existing flight
        DELETE /flights/{id}/ - Delete a flight

    Reservations:

        GET /reservations/ - Get all reservations
        GET /reservations/{id}/ - Get reservation details by ID
        POST /reservations/ - Create a new reservation
        DELETE /reservations/{id}/ - Delete a reservation


7. **Validation**

    The API includes basic validation:

    When creating a reservation, the system checks if the flight is fully booked. If the number of reservations exceeds the airplane's capacity, a validation error is raised.


8. **Testing with Postman**
    
      The API can be tested using Postman. Below are the steps to test the API:

      #### Import Postman Collection:

          Download the Postman collection file (airline_management_system.postman_collection.json).
          Open Postman and click Import.
          Select the downloaded collection file to import.
          Set Up Environment Variables:

          In Postman, go to Manage Environments and create a new environment.
          Add the following variables:
          base_url: http://127.0.0.1:8000/
          id: This will be dynamically replaced in the URL (for GET/PUT requests).
      
      #### Test Endpoints:

          Use the collection to test the available endpoints (GET, POST, PUT, DELETE).
          Replace the {{id}} variable in the URL with an actual ID value for requests that require it.


      #### Postman Collection
        
        The Postman collection is included to test all the API endpoints. You can find the collection file in the project root directory. Import the collection into Postman and use the environment settings to dynamically replace variables in the URLs.

      #### Requirements
      The project dependencies are listed in the requirements.txt file. You can install them using the following command:

        pip install -r requirements.txt



