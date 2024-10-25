# tracking


# Tracking Number Generator API

This project is a RESTful API built with Django Rest Framework (DRF) that generates unique tracking numbers for parcels. The API ensures scalability, efficiency, and can handle high concurrency.

## Features

- Generates unique tracking numbers based on query parameters.
- Ensures tracking numbers match the regex pattern: `^[A-Z0-9]{1,16}$`.
- Handles concurrent requests efficiently.
- Scalable and designed to work with load balancers and multiple instances.

## Project Structure

```
tracking_api/
│
├── manage.py              # Django's command-line utility
├── tracking_api/          # Django project configuration files
│   ├── __init__.py
│   ├── settings.py        # Project settings and configurations
│   ├── urls.py            # URL routing for the project
│   └── wsgi.py            # Entry point for WSGI-compatible web servers
└── tracking/              # Django app for tracking API
    ├── __init__.py
    ├── urls.py            # URL routing for the tracking app
    └── views.py           # API view for generating tracking numbers
```

## Installation

### Prerequisites

- Python 3.8 or higher
- Django 4.x
- Django Rest Framework

### Step-by-Step Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-repo/tracking-api.git
   cd tracking-api
   ```

2. **Set up a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Start the Django development server:**

   ```bash
   python manage.py runserver
   ```

## API Documentation

### Endpoint

**GET /api/next-tracking-number/**

This endpoint generates a unique tracking number based on the provided query parameters.

### Query Parameters

- `origin_country_id` (required): ISO 3166-1 alpha-2 format of the order’s origin country (e.g., "MY").
- `destination_country_id` (required): ISO 3166-1 alpha-2 format of the destination country (e.g., "ID").
- `weight` (required): The weight of the parcel in kilograms (e.g., "1.234").
- `created_at` (required): Timestamp in RFC 3339 format (e.g., "2018-11-20T19:29:32+08:00").
- `customer_id` (required): UUID of the customer (e.g., "de619854-b59b-425e-9db4-943979e1bd49").
- `customer_name` (required): The customer’s name (e.g., "RedBox Logistics").
- `customer_slug` (required): The customer’s name in slug-case/kebab-case (e.g., "redbox-logistics").

### Example Request

```bash
GET /api/next-tracking-number/?origin_country_id=MY&destination_country_id=ID&weight=1.234&created_at=2024-01-01T12:00:00+08:00&customer_id=de619854-b59b-425e-9db4-943979e1bd49&customer_name=RedBox%20Logistics&customer_slug=redbox-logistics
```

### Example Response

```json
{
  "tracking_number": "ABC123XYZ4567890",
  "created_at": "2024-10-25T14:00:00+08:00"
}
```

## Running Tests

To run the tests for the project:

```bash
python manage.py test
```

## Deployment

For deployment in a production environment, consider using a WSGI server such as Gunicorn:

```bash
pip install gunicorn
gunicorn tracking_api.wsgi:application --bind 0.0.0.0:8000 --workers 4

local:python manage.py runserver 9003
```

## Concurrency and Scalability

To handle high concurrency and scale horizontally:
- Use a load balancer (e.g., Nginx) to distribute the traffic across multiple instances.
- Consider deploying with Docker and Kubernetes for containerized environments.
