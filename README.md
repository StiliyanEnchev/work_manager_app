# **Workify**

**Description**:  
Workify connects freelancers with job posters seeking skilled professionals for various projects.


---

## **How It Works**:
- **Job Posters**: Create job listings and manage them.
- **Freelancers**: Apply for jobs that match their bio or skills.
- **Feedback System**: Ensures quality and trust.
- **News Panel**: Keeps users updated with platform announcements and opportunities.

---

## **Installation Steps**:

1. **Clone the repository**:
   ```bash
   
   git clone https://github.com/StiliyanEnchev/work_manager_app.git
   ```
2. **Navigate to the project directory**:
   ```bash
   
   cd work_manager_app
    ```

3. **Set up a virtual environment**:
   ```bash

    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

4. **Install dependencies**:
   ```bash
    pip install -r requirements.txt
  
   ```

5. **Apply migrations**:
   ```bash
    python manage.py makemigrations
    python manage.py migrate
   ```

6. **Run the server**:
   ```bash
   
    python manage.py runserver
   ```

6. **Access the app**:
   ```bash

    Open your browser and visit http://127.0.0.1:8000/
   ```
