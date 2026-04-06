# ExamApp

A Django-based online examination system that allows students to take multiple-choice exams and view their results.

## Features

### For Students
- **User Authentication**: Secure login/logout system
- **Exam Taking**: Take exams by subject with multiple-choice questions
- **Real-time Scoring**: Immediate feedback on answers during the exam
- **Result Viewing**: View exam scores and detailed answer reviews
- **Session Management**: Persistent sessions during exam taking

### For Administrators
- **Question Management**: Add, view, update, and delete exam questions
- **Student Management**: Manage student accounts
- **Subject Organization**: Organize questions by subject areas
- **Result Tracking**: Track and view student performance

## Models

### Questions
- Question text and four multiple-choice options
- Correct answer tracking
- Subject categorization

### Student Info
- Username and password authentication
- Mobile number storage

### Results
- Links students to their exam scores
- Subject-specific scoring
- Historical result tracking

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd examapp
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install django
   ```

4. **Run migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser** (optional, for admin access):
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the application**:
   - Open your browser and go to `http://127.0.0.1:8000/login/`

## Usage

### Student Workflow
1. **Login**: Use your username and password to log in
2. **Select Subject**: Choose from available exam subjects
3. **Take Exam**: Answer multiple-choice questions sequentially
4. **View Results**: See your score and review answers after completion

### Admin Workflow
1. **Add Questions**: Create new exam questions with multiple choices
2. **Manage Students**: Add and view student accounts
3. **View Results**: Monitor student performance across subjects

## Project Structure

```
examapp/
├── exam/                    # Main Django app
│   ├── models.py           # Database models (Questions, Student_info, Result)
│   ├── views.py            # Business logic and request handlers
│   ├── urls.py             # URL routing
│   ├── admin.py            # Django admin configuration
│   └── migrations/         # Database migrations
├── examapp/                # Django project settings
│   ├── settings.py         # Project configuration
│   ├── urls.py             # Main URL configuration
│   └── wsgi.py             # WSGI configuration
├── templates/              # HTML templates
│   ├── Question/           # Question-related templates
│   ├── Result/             # Result display templates
│   └── Student/            # Student authentication templates
├── db.sqlite3              # SQLite database
└── manage.py               # Django management script
```

## Key URLs

- `/login/` - Student login page
- `/subject/` - Subject selection for exams
- `/starttest/<subject>/` - Begin exam for selected subject
- `/addquestion/` - Add new questions (admin)
- `/showquestions/` - View all questions (admin)
- `/myresults/` - View student results

## Technologies Used

- **Backend**: Django 6.0.2
- **Database**: SQLite3
- **Frontend**: HTML templates with Django template language
- **Styling**: CSS (integrated with templates)
- **Session Management**: Django sessions for exam state

## Security Features

- Session-based authentication
- CSRF protection on forms
- Secure password handling
- User session management during exams

## Development Notes

- Uses Django's built-in admin interface for data management
- Implements session-based exam flow to prevent cheating
- Stores answers temporarily in session for result calculation
- Foreign key relationships ensure data integrity

## Future Enhancements

- User registration system
- Password hashing and security improvements
- Timer functionality for exams
- Question randomization
- Advanced reporting and analytics
- REST API for mobile app integration

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the MIT License.