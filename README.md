# Django User Authentication Project

This project is a Django-based web application that implements custom user authentication, handling different types of users: Patients and Doctors. Each user type has its own dashboard, which they are redirected to upon login. The project utilizes Django's authentication system, custom user models, and Bootstrap for front-end styling.

## Features

- Custom User Model supporting two types of users: Patient and Doctor.
- User signup and login system with profile picture upload.
- Separate dashboards for Patients and Doctors.
- Password and Confirm Password match validation.
- Use of Bootstrap CDN for responsive design.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6 or higher installed on your machine.
- Django 3.1 or higher installed in your Python environment.
- Basic understanding of Django project structure and operations.

## Installation

To install the project, follow these steps:

1. Clone the repository to your local machine:

   ```
   git clone https://your-repository-url.git
   cd your_project_name
   ```

2. Navigate to the project directory:

   cd your-project-name

3. Install the required dependencies:

   pip install -r requirements.txt

3. Apply the migrations to create the database schema:

   python manage.py makemigrations
   python manage.py migrate

4. Run the Django development server:

   python manage.py runserver

5. Visit <http://127.0.0.1:8000/> in your web browser to view the application.

## Usage

  The application supports the following operations:

1. User Signup: New users can sign up as either a Patient or a Doctor by filling out the signup form, which includes uploading a profile picture.

2. User Login: Users can log in using their credentials. Upon successful login, users are redirected to their respective dashboards based on their user type.

3. Dashboards: Users can view their profile information on their dashboard.

## Built With

- Django - The web framework used
- Bootstrap CDN - Used for responsive frontend design

## Contributing

- To contribute to this project, follow these steps:

## Fork the repository

1. Create a new branch: git checkout -b <branch_name>.
2. Make your changes and commit them: git commit -m '<commit_message>'.
3. Push to the original branch: git push origin <project_name>/<location>.
4. Create the pull request.
5. Alternatively, see the GitHub documentation on creating a pull request.

## License

- This project is licensed under the MIT License - see the LICENSE.md file for details.

## Contact

- If you have any questions or feedback, please contact me at:

Email: <schnaror@gmail.com>
Phone: 95603-30483
Address: Sector 108, Noida
