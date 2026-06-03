// API Base URL
const API_BASE_URL = 'http://localhost:5000/api';

// Get employee ID from URL
let employeeId = null;

// Load employee on page load
document.addEventListener('DOMContentLoaded', function() {
    // Extract employee ID from URL
    const pathParts = window.location.pathname.split('/');
    employeeId = pathParts[pathParts.length - 1];
    
    if (employeeId) {
        loadEmployeeData();
    }
    
    const form = document.getElementById('employeeForm');
    form.addEventListener('submit', updateEmployee);
});

// Load employee data
function loadEmployeeData() {
    fetch(`${API_BASE_URL}/employees/${employeeId}`)
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert('Employee not found');
                window.location.href = '/';
                return;
            }
            
            // Fill form with employee data
            document.getElementById('firstName').value = data.first_name;
            document.getElementById('lastName').value = data.last_name;
            document.getElementById('email').value = data.email;
            document.getElementById('phone').value = data.phone;
            document.getElementById('department').value = data.department;
            document.getElementById('salary').value = data.salary;
            document.getElementById('hireDate').value = data.hire_date;
        })
        .catch(error => {
            console.error('Error loading employee:', error);
            alert('Error loading employee data');
        });
}

// Update employee
function updateEmployee(e) {
    e.preventDefault();
    
    const formData = {
        firstName: document.getElementById('firstName').value,
        lastName: document.getElementById('lastName').value,
        email: document.getElementById('email').value,
        phone: document.getElementById('phone').value,
        department: document.getElementById('department').value,
        salary: parseFloat(document.getElementById('salary').value),
        hireDate: document.getElementById('hireDate').value
    };
    
    fetch(`${API_BASE_URL}/employees/${employeeId}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
        const messageDiv = document.getElementById('message');
        if (data.success) {
            messageDiv.className = 'message success show';
            messageDiv.textContent = data.message;
            
            // Redirect to dashboard after 2 seconds
            setTimeout(() => {
                window.location.href = '/';
            }, 2000);
        } else {
            messageDiv.className = 'message error show';
            messageDiv.textContent = data.message;
        }
    })
    .catch(error => {
        console.error('Error:', error);
        const messageDiv = document.getElementById('message');
        messageDiv.className = 'message error show';
        messageDiv.textContent = 'Error updating employee';
    });
}
