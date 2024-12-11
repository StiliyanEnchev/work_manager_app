# Workify

Description: Workifty connects freelancers with job posters seeking skilled professionals for various projects.

How It Works:

Job posters create new jobs on the website, and freelancers apply for jobs that match their bio or skills. 

The platform includes a feedback system to ensure quality and trust.

A news panel keeps users updated with the latest platform announcements and opportunities.

Installation Steps for my Work Manager App

Clone the repository:

git clone https://github.com/StiliyanEnchev/work_manager_app.git

Navigate to the project directory:
cd work_manager_app

Set up a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

Install dependencies:

pip install -r requirements.txt

Apply migrations:

python manage.py makemigrations
python manage.py migrate

Run the development server:
python manage.py runserver

Access the app: 

Open your browser and visit http://127.0.0.1:8000/
