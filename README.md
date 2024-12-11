# **Workify**

**Description**:  
- Workify connects freelancers with job posters seeking skilled professionals for various projects.


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

---

Short Introduction of the available options: 
1. **Home Page - accessible when you click the main title of the page**:

![image](https://github.com/user-attachments/assets/bf162666-0392-40a1-b021-69bdd8bd2406)
---

2. **Login and Register Page**:
3. 
![image](https://github.com/user-attachments/assets/49b876e2-e40a-453a-b96a-c421665abe7c)
![image](https://github.com/user-attachments/assets/08094e07-c675-4f5c-b68f-5beb7412db31)
---

3.**Specified navigation for the available options of each user**:

- If the user is a Freelancer: 
![image](https://github.com/user-attachments/assets/871f49d6-582b-4488-9c8f-10438f1df975)

- If the user is Job Poster:
![image](https://github.com/user-attachments/assets/a7f02848-3a1b-4bbc-ad03-ac099b0a90c2)
---

4.**Title changes dynamically based on the URL of the page**:

![image](https://github.com/user-attachments/assets/cf33fa5d-134c-43f8-9f91-c4cb4f2a9624)
---

5.**Profile Details and changes can be done from the Profile page**:

![image](https://github.com/user-attachments/assets/65bcaf94-9cb3-41c5-95ca-10adba720377)
---

5.**My Jobs displays only the posted job by the Job Poster if there are any and shows the candidates for it with their contact and an option to mark the job as Taken in order for it to be removed from the dashboard**:

![image](https://github.com/user-attachments/assets/024fda95-ac55-4f0f-bc70-4b53d21deee4)
---
