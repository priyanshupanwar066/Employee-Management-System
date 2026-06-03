// API Base URL
const API_BASE_URL = '/api';

// Load form on page load
document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('employeeForm');
    form.addEventListener('submit', addEmployee);
});

// Add employee
function addEmployee(e) {
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
    
    fetch(`${API_BASE_URL}/employees`, {
        method: 'POST',
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
            
            // Reset form
            document.getElementById('employeeForm').reset();
            
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
        messageDiv.textContent = 'Error adding employee';
    });
}
