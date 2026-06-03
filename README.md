# Employee Management System - Two Tier Web App

A modern web application for managing employees with Python Flask backend and SQL database.

## Features

✅ **Employee Management**
- Add new employees
- Update existing employee information
- Delete employees
- View all employees

✅ **Search & Filter**
- Search employees by name or email
- Filter employees by department
- Department-wise employee view

✅ **Salary Tracking**
- View salary information by department
- Average salary calculations
- Min/Max salary tracking
- Total department salary overview

## Project Structure

```
two-tier app/
├── backend/
│   ├── app.py              # Flask application & API routes
│   ├── database.py         # Database operations
│   ├── config.py          # Configuration settings
│   ├── requirements.txt    # Python dependencies
│   └── employees.db       # SQLite database (created on first run)
│
└── frontend/
    ├── index.html         # Dashboard/Home page
    ├── add-employee.html  # Add employee form
    ├── edit-employee.html # Edit employee form
    ├── style.css          # CSS styling
    ├── script.js          # Dashboard functionality
    ├── form-script.js     # Add employee form logic
    └── edit-script.js     # Edit employee form logic
```

## Requirements

- Python 3.7+
- pip (Python package manager)

## Installation & Setup

### Step 1: Install Python Dependencies

Navigate to the backend directory and install required packages:

```bash
cd backend
pip install -r requirements.txt
```

### Step 2: Run the Application

From the backend directory, start the Flask server:

```bash
python app.py
```

The application will start on `http://localhost:5000`

### Step 3: Access the Application

Open your web browser and navigate to:
```
http://localhost:5000
```

## Usage

### Dashboard (Home Page)
- View all employees in a table
- Search for employees by name or email
- Filter employees by department
- View salary tracking information by department

### Add Employee
- Click "Add Employee" in the navigation menu
- Fill in all required fields:
  - First Name
  - Last Name
  - Email
  - Phone
  - Department
  - Salary
  - Hire Date
- Click "Add Employee" to save

### Edit Employee
- Click the "Edit" button next to any employee in the table
- Modify the employee information
- Click "Update Employee" to save changes

### Delete Employee
- Click the "Delete" button next to any employee
- Confirm the deletion in the popup dialog
- Employee will be removed from the database

### Search Employee
- Use the search box on the dashboard
- Type name or email to search
- Results will appear in real-time

### Department Wise Filter
- Use the department dropdown on the dashboard
- Select a department to filter employees
- View all employees in that department with salary information

### Salary Tracking
- Click the "Salary Info" tab on the dashboard
- View department-wise salary statistics:
  - Total employees per department
  - Average salary
  - Minimum salary
  - Maximum salary
  - Total salary payroll per department

## Database

The application uses SQLite as the database. The database file (`employees.db`) is automatically created in the backend directory when you first run the application.

### Database Schema

**employees table:**
- id: INTEGER PRIMARY KEY (auto-increment)
- first_name: TEXT (required)
- last_name: TEXT (required)
- email: TEXT (unique, required)
- phone: TEXT (required)
- department: TEXT (required)
- salary: REAL (required)
- hire_date: TEXT (required)
- created_at: TIMESTAMP (auto)
- updated_at: TIMESTAMP (auto)

## API Endpoints

### Get All Employees
```
GET /api/employees
```

### Get Single Employee
```
GET /api/employees/<id>
```

### Add Employee
```
POST /api/employees
Content-Type: application/json

{
  "firstName": "John",
  "lastName": "Doe",
  "email": "john@example.com",
  "phone": "1234567890",
  "department": "IT",
  "salary": 50000,
  "hireDate": "2024-01-15"
}
```

### Update Employee
```
PUT /api/employees/<id>
Content-Type: application/json

{
  "firstName": "John",
  "lastName": "Doe",
  "email": "john@example.com",
  "phone": "1234567890",
  "department": "IT",
  "salary": 55000,
  "hireDate": "2024-01-15"
}
```

### Delete Employee
```
DELETE /api/employees/<id>
```

### Search Employees
```
GET /api/search?q=<search_query>
```

### Get All Departments
```
GET /api/departments
```

### Filter by Department
```
GET /api/filter/department/<department_name>
```

### Get Salary Info
```
GET /api/salary-info
```

## Technologies Used

### Backend
- **Python 3.7+**: Programming language
- **Flask**: Web framework for building API
- **Flask-CORS**: Handling Cross-Origin requests
- **SQLite3**: Relational database

### Frontend
- **HTML5**: Markup
- **CSS3**: Styling with responsive design
- **Vanilla JavaScript**: Frontend interactivity (no dependencies)

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## Troubleshooting

### Port Already in Use
If port 5000 is already in use, you can modify the port in `backend/app.py`:
```python
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5001)  # Change 5000 to 5001
```

### CORS Errors
The application includes CORS configuration. If you still face issues:
1. Make sure Flask-CORS is installed: `pip install Flask-CORS`
2. Restart the server

### Database Errors
If you encounter database errors:
1. Delete the `employees.db` file
2. Restart the application to create a fresh database

## Features Implemented

✅ Add Employee
✅ Update Employee
✅ Delete Employee
✅ Search Employee
✅ Department Wise Filter
✅ Salary Tracking
✅ Responsive Design
✅ Error Handling
✅ Data Validation

## Future Enhancements

- Employee performance ratings
- Attendance tracking
- Leave management
- Employee roles and permissions
- Advanced reporting and analytics
- Export data to CSV/Excel
- Email notifications
- User authentication and authorization


