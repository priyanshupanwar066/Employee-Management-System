from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from database import (
    init_db, add_employee, get_all_employees, get_employee_by_id,
    search_employees, filter_by_department, get_all_departments,
    get_salary_info, update_employee, delete_employee
)
import os

app = Flask(__name__, template_folder='templates', static_folder='static')
CORS(app)

# Initialize database on startup
if not os.path.exists('employees.db'):
    init_db()

# ============= Frontend Routes =============

@app.route('/')
def index():
    """Render the dashboard page"""
    return render_template('index.html')

@app.route('/add')
def add_page():
    """Render the add employee page"""
    return render_template('add-employee.html')

@app.route('/edit/<int:employee_id>')
def edit_page(employee_id):
    """Render the edit employee page"""
    return render_template('edit-employee.html')

# ============= API Routes =============

@app.route('/api/employees', methods=['GET'])
def api_get_employees():
    """Get all employees"""
    employees = get_all_employees()
    return jsonify(employees)

@app.route('/api/employees/<int:employee_id>', methods=['GET'])
def api_get_employee(employee_id):
    """Get a specific employee"""
    employee = get_employee_by_id(employee_id)
    if employee:
        return jsonify(employee)
    return jsonify({'error': 'Employee not found'}), 404

@app.route('/api/employees', methods=['POST'])
def api_add_employee():
    """Add a new employee"""
    data = request.json
    
    # Validate required fields
    required_fields = ['firstName', 'lastName', 'email', 'phone', 'department', 'salary', 'hireDate']
    if not all(field in data for field in required_fields):
        return jsonify({'success': False, 'message': 'Missing required fields'}), 400
    
    result = add_employee(
        data['firstName'],
        data['lastName'],
        data['email'],
        data['phone'],
        data['department'],
        data['salary'],
        data['hireDate']
    )
    
    return jsonify(result), 201 if result['success'] else 400

@app.route('/api/employees/<int:employee_id>', methods=['PUT'])
def api_update_employee(employee_id):
    """Update an existing employee"""
    data = request.json
    
    # Validate required fields
    required_fields = ['firstName', 'lastName', 'email', 'phone', 'department', 'salary', 'hireDate']
    if not all(field in data for field in required_fields):
        return jsonify({'success': False, 'message': 'Missing required fields'}), 400
    
    result = update_employee(
        employee_id,
        data['firstName'],
        data['lastName'],
        data['email'],
        data['phone'],
        data['department'],
        data['salary'],
        data['hireDate']
    )
    
    return jsonify(result), 200 if result['success'] else 400

@app.route('/api/employees/<int:employee_id>', methods=['DELETE'])
def api_delete_employee(employee_id):
    """Delete an employee"""
    result = delete_employee(employee_id)
    return jsonify(result), 200 if result['success'] else 400

@app.route('/api/search', methods=['GET'])
def api_search():
    """Search employees"""
    query = request.args.get('q', '')
    if not query:
        return jsonify({'error': 'Search query required'}), 400
    
    employees = search_employees(query)
    return jsonify(employees)

@app.route('/api/departments', methods=['GET'])
def api_get_departments():
    """Get all departments"""
    departments = get_all_departments()
    return jsonify(departments)

@app.route('/api/filter/department/<department>', methods=['GET'])
def api_filter_department(department):
    """Filter employees by department"""
    employees = filter_by_department(department)
    return jsonify(employees)

@app.route('/api/salary-info', methods=['GET'])
def api_salary_info():
    """Get salary tracking information"""
    salary_info = get_salary_info()
    return jsonify(salary_info)

# ============= Error Handlers =============

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
