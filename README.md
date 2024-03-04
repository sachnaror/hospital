# Django User Authentication Project

This project is a Django-based web application that implements custom user authentication, handling different types of users: Patients and Doctors. Each user type has its own dashboard, which they are redirected to upon login. The project utilizes Django's authentication system, custom user models, and Bootstrap.

## Features

- Custom User Model supporting two types of users: Patient and Doctor.
- User signup and login system with profile picture upload.
- Separate dashboards ("view details" for now for this task's purpose only) for Patients and Doctors
- Password and Confirm Password match validation.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6 or higher installed on your machine.
- Django 3.1 or higher installed in your Python environment.
- Basic understanding of Django project structure and operations.

## Installation

To install the project, follow these steps:

1. Clone the repository to your local machine:

   ```
   git clone https://github.com/sachnaror/hospital.git

   ```

2. Navigate to the project directory:

```
   cd hospital
```

3. Install the required dependencies:

```
   pip install -r requirements.txt
```

3. Apply the migrations to create the database schema:

```
   python manage.py makemigrations
   python manage.py migrate
```

4. Run the Django development server:

```
   python manage.py runserver
```

5. Visit <https://hospital-tzoco.ondigitalocean.app/> in your web browser to view the application.

## Usage

  The application supports the following operations:

1. User Signup: New users can sign up as either a Patient or a Doctor by filling out the signup form, which includes uploading a profile picture.

2. User Login: Users can log in using their credentials. Upon successful login, users are redirected to their respective dashboards based on their user type.

3. Dashboards: Users can view their profile information on their dashboard.

## Built With

- Django - The web framework used
- Bootstrap CDN - Used for responsive frontend design

## Fork the repository

1. Create a new branch: git checkout -b master
2. Make your changes and commit them: git commit -m '<commit_message>'.
3. Push to the original branch: git push origin hospital/master
4. Create the pull request.
5. Alternatively, see the GitHub documentation on creating a pull request.

## Database

- Check this table for the data poured when signup form is submitted. For the tasks purpose, i have one table for all save and retrieve data :

<img width="999" alt="image" src="https://github.com/sachnaror/hospital/assets/9551754/b5437b34-8a7e-4a30-8894-6dcc5461b580">

<img width="383" alt="Screenshot 2024-03-04 at 10 08 24 AM" src="https://github.com/sachnaror/hospital/assets/9551754/2dc5e360-0966-465f-9ab6-0bfd0004613b">

<img width="1292" alt="image" src="https://github.com/sachnaror/hospital/assets/9551754/ca73252b-742b-41b7-864d-9259db8393db">

## Contact

- If you have any questions or feedback, please contact me at:

```
Email: <schnaror@gmail.com>
Phone: 95603-30483
Address: Sector 108, Noida
```
