Django Book Review and Recommendation System

Overview

This project is a Django-based API that allows users to manage books, leave reviews, rate them, and receive book recommendations based on their preferences. The API includes features such as user authentication using JWT, book listing with filtering by genre, user reviews, and book suggestions based on past ratings.

Features

User Authentication: Users can register, log in, and obtain JWT tokens to authenticate API requests.
Books Management: Users can view a list of books, filter them by genre, and view details of individual books.
Reviews and Ratings: Authenticated users can leave reviews and ratings for books, update or delete their reviews.
Book Recommendations: The system suggests books to users based on their past reviews and ratings.
API Endpoints

Authentication
Method	Endpoint	Description
POST	/users/register/	Register a new user
POST	/api/token/	Obtain JWT token
POST	/api/token/refresh/	Refresh JWT token
Books
Method	Endpoint	Description
GET	/api/book/list/	List all books, optionally filter by genre (?genre=Adventure)
GET	/api/book/suggest/	Get suggested books for the authenticated user
Reviews
Method	Endpoint	Description
POST	/api/review/add/	Add a review for a book
PUT	/api/review/update/<id>/	Update an existing review
DELETE	/api/review/delete/<id>/	Delete a review
Technologies

Backend: Django 5.1, Django Rest Framework
Authentication: JWT via rest_framework_simplejwt
Database: PostgreSQL
API Documentation: DRF Spectacular
Setup Instructions

Prerequisites
Python 3.10 or higher
PostgreSQL
Pipenv or Virtualenv for environment management
Installation
Clone the repository:
bash
Copy code
git clone <repository-url>
cd <project-directory>
Set up a virtual environment:
Using virtualenv:

bash
Copy code
python3 -m venv venv
source venv/bin/activate
Using pipenv:

bash
Copy code
pipenv shell
Install the project dependencies:
bash
Copy code
pip install -r requirements.txt
Set up the database:
Make sure PostgreSQL is installed and running, then create a database:

bash
Copy code
psql
CREATE DATABASE netban;
Apply migrations:
bash
Copy code
python manage.py migrate
Create a superuser for the Django admin panel:
bash
Copy code
python manage.py createsuperuser
Run the development server:
bash
Copy code
python manage.py runserver
The project should now be running at http://127.0.0.1:8000/.

Running Tests
The project uses pytest for testing. To run tests, use the following command:

bash
Copy code
pytest
API Documentation
You can view the API documentation using the DRF Spectacular Swagger interface. Visit the following URL in your browser:

Swagger UI: http://127.0.0.1:8000/api/schema/swagger-ui/
Redoc: http://127.0.0.1:8000/api/schema/redoc/
Project Structure
plaintext
Copy code
.
├── books/                          # Books app (API, models, serializers, etc.)
├── reviews/                        # Reviews app (API, models, etc.)
├── users/                          # Users app (authentication, registration)
├── library/                        # Project settings and configuration
├── manage.py                       # Django management script
├── requirements.txt                # Python dependencies
└── README.md                       # Project documentation
Key Files
settings.py: Project settings for development and production.
urls.py: Defines all the URL routes for the project.
views.py: Handles the business logic of the API endpoints.
models.py: Defines the database models (Books, Reviews, Users).
serializers.py: Converts models into JSON for API responses.
tests/: Contains unit and integration tests for the project.
Contributing

Fork the project
Create your feature branch (git checkout -b feature/your-feature)
Commit your changes (git commit -am 'Add feature')
Push to the branch (git push origin feature/your-feature)
Create a new Pull Request
License

This project is licensed under the MIT License - see the LICENSE file for details.

