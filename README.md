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

5. **Configure Database Settings**: 
   ```bash
     Open the settings.py file of the project and configure the database settings.

   ```
   

6. **Migrate Without Signals**: 
   ```bash
   The "accounts/signals.py" must be removed (or made as a comment) before the first migration to the database.
   Then added again for the next migration to apply the groups after the permissions have been created for the models.

   ```

7. **Apply migrations**:
   ```bash
    python manage.py makemigrations
    python manage.py migrate
   ```

8. **Run the server**:
   ```bash
   
    python manage.py runserver
   ```

9. **Access the app**:
   ```bash

    Open your browser and visit http://127.0.0.1:8000/
   ```

---

Short Introduction of the available options: 
1. **Home Page - accessible when you click the main title of the page**:

![image](https://github.com/user-attachments/assets/bf162666-0392-40a1-b021-69bdd8bd2406)
---

2. **Login and Register Page**:

![image](https://github.com/user-attachments/assets/49b876e2-e40a-453a-b96a-c421665abe7c)
![image](https://github.com/user-attachments/assets/08094e07-c675-4f5c-b68f-5beb7412db31)
---

3. **Specified navigation for the available options of each user**:

- If the user is a Freelancer: 
![image](https://github.com/user-attachments/assets/871f49d6-582b-4488-9c8f-10438f1df975)

- If the user is Job Poster:
![image](https://github.com/user-attachments/assets/a7f02848-3a1b-4bbc-ad03-ac099b0a90c2)
---

4. **Title changes dynamically based on the URL of the page**:

![image](https://github.com/user-attachments/assets/cf33fa5d-134c-43f8-9f91-c4cb4f2a9624)
---

5. **Profile Details and changes can be done from the Profile page**:

![image](https://github.com/user-attachments/assets/65bcaf94-9cb3-41c5-95ca-10adba720377)
---

6. **My Jobs displays only the posted job by the Job Poster if there are any and shows the candidates for it with their contact and an option to mark the job as Taken in order for it to be removed from the dashboard**:

![image](https://github.com/user-attachments/assets/a9ccd133-62ab-4493-b486-b84eb71bee8a)
---

7.**News - Updates from the creators of the website. Can be updated only from the admin**

![image](https://github.com/user-attachments/assets/a4b68a68-3554-4787-a87a-277c1bc194de)
---

8.**Dashboard where all jobs are displayed. 
If the user is the creator, he can edit/delete it. 
If the user is Freelancer he can apply for jobs. 
If the user is in the Group Editors he can edit all jobs as displayed below but delete only his owns. **

![image](https://github.com/user-attachments/assets/8e4e49b3-99c9-4dbe-ae8d-198e0f6fefcb)
---

9.**Dashboard where all jobs are displayed**. 
If the user is the creator, he can edit/delete it. 
If the user is Freelancer he can apply for jobs. 
If the user is in the Group Editors he can edit all jobs as displayed below but delete only his owns. **

![image](https://github.com/user-attachments/assets/8e4e49b3-99c9-4dbe-ae8d-198e0f6fefcb)
---

10.**Feedback can be submitted only by logged users and it is displayed in the admin panel**. 

![image](https://github.com/user-attachments/assets/7e962397-7c70-4f75-b48d-d879584be79b)
---



