# Meeting Organiser

This is a Django-based project for organizing meetings using Google Calendar API.

## Project Structure

The project consists of two main directories:

1. `meeting_api`: Contains the core components of the application (models, views, serializers, etc.)

2. `meeting_organiser`: Contains the project settings, URLs, and ASGI configuration

## Setup Instructions

Follow these steps to set up and run the project:

1. Clone the repository/Extact the zip file:

`git clone https://github.com/theyvraj/`
`RightClick => Extract Zip File => Extract Files`

2. cd meetging_organiser.
3. Create a virtual environment:

`python -m venv .venv`
`.venv\Scripts\activate`

4. Install the required dependencies:

`pip install -r requirements.txt`

5. Make migrations:

`python manage.py makemigrations`
`python manage.py migrate`

5. Run the django server:

`python manage.py runserver`