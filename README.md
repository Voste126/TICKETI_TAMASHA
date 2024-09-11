# TICKETI_TAMASHA

**TICKETI_TAMASHA** is an event ticketing and management platform, designed to provide users with a seamless experience for booking, purchasing, and managing event tickets. This project serves as a capstone for the **ALX Software Engineering Program**.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation and Setup](#installation-and-setup)
- [Environment Variables](#environment-variables)
- [Running Locally](#running-locally)
- [API Documentation](#api-documentation)
- [Deployment on Render](#deployment-on-render)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

TICKETI_TAMASHA is an online platform where users can browse events, purchase tickets using multiple payment methods (including MPESA), and manage their bookings. Event organizers can create and manage events, while users can search for events by location, category, and other filters.

This project marks the culmination of the foundation phase of the ALX Software Engineering Program.

## Features

- **Event Management**: Create, update, and delete events.
- **Ticket Booking**: Users can book tickets for events.
- **MPESA STK Push Payment Integration**: Integrated mobile payment for ticket purchases using MPESA.
- **JWT Authentication**: Secure login and signup functionality for users and event organizers.
- **Search Events**: Search for events by categories, tags, or location.
- **Responsive Design**: Frontend built using React with Material UI for a modern, responsive user experience.
- **Role-Based Access Control**: Different user roles (admin, organizer, attendee) with defined permissions.

## Tech Stack

### Frontend

- **ReactJS**: For building the user interface.
- **Material UI (MDB React Kit)**: For frontend styling and components.
- **Axios**: For making HTTP requests to the backend API.
- **React Router**: For client-side routing.

### Backend

- **Django**: Backend framework to manage the API and business logic.
- **Django Rest Framework (DRF)**: For building RESTful APIs.
- **Django Daraja**: For integrating MPESA payments via STK push.
- **PostgreSQL**: Relational database for storing event and booking information.

### Deployment

- **Render**: The platform used for deploying both the frontend and backend of this project.

## Installation and Setup

To get started with the project locally, follow these steps:

### 1. Clone the Repository

```bash
git clone https://github.com/username/ticketi_tamasha.git
cd ticketi_tamasha
```

### 2. Frontend Setup (React)

Navigate to the frontend directory:

```bash
cd frontend
```

Install frontend dependencies:

```bash
npm install
```

Set up environment variables in the frontend/.env file (create one if it doesn't exist):

```bash

REACT_APP_BACKEND_API_URL=http://localhost:8000
```

Start the React development server:

```bash
npm start
```

The frontend will be accessible at:

```bash
http://localhost:3000.
```

### 3. Backend Setup (Django)

Navigate to the backend directory:

```bash
cd ../backend
```

Create a virtual environment:

```bash
python3 -m venv env
source env/bin/activate
```

Install backend dependencies:

```bash
pip install -r requirements.txt
```

Apply migrations to set up the database:

```bash
python manage.py migrate
```

## environment-variables

Set up environment variables in the backend/.env file (create one if it doesn't exist):

```bash
DEBUG=True
SECRET_KEY=your_secret_key
DATABASE_URL=postgresql://your_db_url
MPESA_CONSUMER_KEY=your_mpesa_consumer_key
MPESA_CONSUMER_SECRET=your_mpesa_consumer_secret
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
```

Run the Django development server:

```bash
python manage.py runserver
```

The backend server will be accessible at:

```bash
http://localhost:8000.
```

Environment Variables
Frontend (.env)
In the frontend/.env file, add:

```bash
REACT_APP_BACKEND_API_URL=http://localhost:8000
```

Backend (.env)
In the backend/.env file, add:

```bash
DEBUG=True
SECRET_KEY=your_secret_key
DATABASE_URL=postgresql://your_db_url
MPESA_CONSUMER_KEY=your_mpesa_consumer_key
MPESA_CONSUMER_SECRET=your_mpesa_consumer_secret
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
```

## Running Locally

After setting up the environment variables, follow these steps:

### 1. Start Backend (Django)

Run the backend server:

```bash
cd backend
python manage.py runserver
```

This starts the backend server at:

```bash
 http://localhost:8000.
```

### 2. Start Frontend (React)

Run the frontend server:

```bash
cd ../frontend
npm start
```

The frontend will be available at:

```bash
http://localhost:3000.
```

## api-documentation

Base URL
The API is accessible at:

```bash
http://localhost:8000/api/
```

Endpoints
Authentication
Login: /auth/login/
Signup: /auth/register/
Events
List all events: /events/
Get details of an event: /events/{event_id}/
Create an event (Admin/Organizer): /events/create/
Update an event (Admin/Organizer): /events/{event_id}/update/
Delete an event (Admin/Organizer): /events/{event_id}/delete/
Tickets
List tickets for an event: /events/{event_id}/tickets/
Create a ticket (Organizer): /events/{event_id}/tickets/create/
Book a ticket: /events/{event_id}/tickets/book/
Payments
Initiate MPESA STK Push: /payments/mpesa/
Verify Payment: /payments/verify/
Bookings
View bookings (User): /bookings/
Cancel a booking: /bookings/{booking_id}/cancel/

## Contributing

We welcome contributions from the open-source community. To contribute:

Fork the repository.
Create a new branch for your feature or fix.
Push your changes to your fork.
Open a pull request on the main repository.

## Deployment on Render

To deploy the project to Render, follow these steps:

### 1. Create a Render Account

Sign up at Render.

### 2. Deploy the Backend (Django)

Create a new Web Service for the Django backend.

Connect the Render service to your GitHub repository.

Add the necessary environment variables under the Settings tab.

Set the Build Command to:

```bash

pip install -r requirements.txt
python manage.py migrate
```

Set the Start Command to:

```bash

gunicorn backend.wsgi
```

### 3. Deploy the Frontend (React)

Create another Web Service for the React frontend.

Connect this service to the same GitHub repository.

Add the necessary environment variables for the frontend.

Set the Build Command to:

```bash
npm install && npm run build
```

Set the Publish Directory to:

```bash
frontend/build
```

### 4. Configure Custom Domains (Optional)

If you have custom domains for your services, configure them under the Domains section of Render for both the frontend and backend.

## License

This project is licensed under the MIT License.

This version of the `README.md` provides everything in one place, including setup instructions, local running steps, environment variables, API documentation, and deployment on Render. You can copy and paste it as needed for your project.
