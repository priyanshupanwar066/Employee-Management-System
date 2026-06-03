import sqlite3
from datetime import datetime
import os

DB_PATH = 'employees.db'

def init_db():
    """Initialize the database with schema"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Create employees table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            phone TEXT NOT NULL,
            department TEXT NOT NULL,
            salary REAL NOT NULL,
            hire_date TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()

def add_employee(first_name, last_name, email, phone, department, salary, hire_date):
    """Add a new employee to the database"""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO employees 
            (first_name, last_name, email, phone, department, salary, hire_date)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (first_name, last_name, email, phone, department, salary, hire_date))
        
        conn.commit()
        employee_id = cursor.lastrowid
        conn.close()
        
        return {'success': True, 'id': employee_id, 'message': 'Employee added successfully'}
    except sqlite3.IntegrityError as e:
        return {'success': False, 'message': f'Error: {str(e)}'}
    except Exception as e:
        return {'success': False, 'message': f'Error: {str(e)}'}

def get_all_employees():
    """Retrieve all employees"""
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM employees ORDER BY id DESC')
        rows = cursor.fetchall()
        conn.close()
        
        return [dict(row) for row in rows]
    except Exception as e:
        return {'error': str(e)}

def get_employee_by_id(employee_id):
    """Retrieve a specific employee by ID"""
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM employees WHERE id = ?', (employee_id,))
        row = cursor.fetchone()
        conn.close()
        
        return dict(row) if row else None
    except Exception as e:
        return {'error': str(e)}

def search_employees(query):
    """Search employees by name or email"""
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        search_param = f'%{query}%'
        cursor.execute('''
            SELECT * FROM employees 
            WHERE first_name LIKE ? OR last_name LIKE ? OR email LIKE ?
            ORDER BY id DESC
        ''', (search_param, search_param, search_param))
        
        rows = cursor.fetchall()
        conn.close()
        
        return [dict(row) for row in rows]
    except Exception as e:
        return {'error': str(e)}

def filter_by_department(department):
    """Filter employees by department"""
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT * FROM employees 
            WHERE department = ?
            ORDER BY salary DESC
        ''', (department,))
        
        rows = cursor.fetchall()
        conn.close()
        
        return [dict(row) for row in rows]
    except Exception as e:
        return {'error': str(e)}

def get_all_departments():
    """Get list of all departments"""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        cursor.execute('SELECT DISTINCT department FROM employees ORDER BY department')
        rows = cursor.fetchall()
        conn.close()
        
        return [row[0] for row in rows]
    except Exception as e:
        return {'error': str(e)}

def get_salary_info():
    """Get salary tracking information"""
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT 
                department,
                COUNT(*) as total_employees,
                AVG(salary) as avg_salary,
                MIN(salary) as min_salary,
                MAX(salary) as max_salary,
                SUM(salary) as total_salary
            FROM employees
            GROUP BY department
            ORDER BY total_salary DESC
        ''')
        
        rows = cursor.fetchall()
        conn.close()
        
        return [dict(row) for row in rows]
    except Exception as e:
        return {'error': str(e)}

def update_employee(employee_id, first_name, last_name, email, phone, department, salary, hire_date):
    """Update an existing employee"""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        cursor.execute('''
            UPDATE employees
            SET first_name = ?, last_name = ?, email = ?, phone = ?, 
                department = ?, salary = ?, hire_date = ?, updated_at = CURRENT_TIMESTAMP
            WHERE id = ?
        ''', (first_name, last_name, email, phone, department, salary, hire_date, employee_id))
        
        conn.commit()
        conn.close()
        
        return {'success': True, 'message': 'Employee updated successfully'}
    except sqlite3.IntegrityError as e:
        return {'success': False, 'message': f'Error: {str(e)}'}
    except Exception as e:
        return {'success': False, 'message': f'Error: {str(e)}'}

def delete_employee(employee_id):
    """Delete an employee"""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        cursor.execute('DELETE FROM employees WHERE id = ?', (employee_id,))
        
        conn.commit()
        conn.close()
        
        return {'success': True, 'message': 'Employee deleted successfully'}
    except Exception as e:
        return {'success': False, 'message': f'Error: {str(e)}'}
