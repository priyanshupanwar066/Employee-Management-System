// API Base URL
const API_BASE_URL = 'http://localhost:5000/api';

// Load employees on page load
document.addEventListener('DOMContentLoaded', function() {
    loadEmployees();
    loadDepartmentFilter();
    setupDeleteModal();
});

// Load all employees
function loadEmployees() {
    fetch(`${API_BASE_URL}/employees`)
        .then(response => response.json())
        .then(data => {
            displayEmployees(data);
        })
        .catch(error => {
            console.error('Error loading employees:', error);
            document.getElementById('employeesTableBody').innerHTML = 
                '<tr><td colspan="8" class="text-center">Error loading employees</td></tr>';
        });
}

// Display employees in table
function displayEmployees(employees) {
    const tbody = document.getElementById('employeesTableBody');
    
    if (employees.length === 0) {
        tbody.innerHTML = '<tr><td colspan="8" class="text-center">No employees found</td></tr>';
        return;
    }
    
    tbody.innerHTML = employees.map(emp => `
        <tr>
            <td>${emp.id}</td>
            <td>${emp.first_name} ${emp.last_name}</td>
            <td>${emp.email}</td>
            <td>${emp.phone}</td>
            <td>${emp.department}</td>
            <td>$${parseFloat(emp.salary).toLocaleString('en-US', {minimumFractionDigits: 2, maximumFractionDigits: 2})}</td>
            <td>${emp.hire_date}</td>
            <td>
                <div class="action-buttons">
                    <a href="/edit/${emp.id}" class="btn btn-edit">Edit</a>
                    <button class="btn btn-delete" onclick="openDeleteModal(${emp.id})">Delete</button>
                </div>
            </td>
        </tr>
    `).join('');
}

// Search employees
function searchEmployees() {
    const query = document.getElementById('searchInput').value.trim();
    
    if (!query) {
        loadEmployees();
        return;
    }
    
    fetch(`${API_BASE_URL}/search?q=${encodeURIComponent(query)}`)
        .then(response => response.json())
        .then(data => {
            displayEmployees(data);
        })
        .catch(error => console.error('Error searching:', error));
}

// Reset search
function resetSearch() {
    document.getElementById('searchInput').value = '';
    document.getElementById('departmentFilter').value = '';
    loadEmployees();
}

// Load departments for filter
function loadDepartmentFilter() {
    fetch(`${API_BASE_URL}/departments`)
        .then(response => response.json())
        .then(departments => {
            const select = document.getElementById('departmentFilter');
            departments.forEach(dept => {
                const option = document.createElement('option');
                option.value = dept;
                option.textContent = dept;
                select.appendChild(option);
            });
        })
        .catch(error => console.error('Error loading departments:', error));
}

// Filter by department
function filterByDepartment() {
    const department = document.getElementById('departmentFilter').value;
    
    if (!department) {
        loadEmployees();
        return;
    }
    
    fetch(`${API_BASE_URL}/filter/department/${encodeURIComponent(department)}`)
        .then(response => response.json())
        .then(data => {
            displayEmployees(data);
        })
        .catch(error => console.error('Error filtering:', error));
}

// Show tab
function showTab(tabName) {
    // Hide all tabs
    const tabs = document.querySelectorAll('.tab-content');
    tabs.forEach(tab => tab.classList.remove('active'));
    
    // Remove active class from buttons
    const buttons = document.querySelectorAll('.tab-button');
    buttons.forEach(btn => btn.classList.remove('active'));
    
    // Show selected tab
    document.getElementById(tabName).classList.add('active');
    
    // Add active class to clicked button
    event.target.classList.add('active');
    
    // Load salary info if salary tab
    if (tabName === 'salary-tab') {
        loadSalaryInfo();
    }
}

// Load salary information
function loadSalaryInfo() {
    fetch(`${API_BASE_URL}/salary-info`)
        .then(response => response.json())
        .then(data => {
            displaySalaryInfo(data);
        })
        .catch(error => console.error('Error loading salary info:', error));
}

// Display salary information
function displaySalaryInfo(salaryData) {
    const tbody = document.getElementById('salaryTableBody');
    
    if (salaryData.length === 0) {
        tbody.innerHTML = '<tr><td colspan="6" class="text-center">No salary data available</td></tr>';
        return;
    }
    
    tbody.innerHTML = salaryData.map(item => `
        <tr>
            <td>${item.department}</td>
            <td>${item.total_employees}</td>
            <td>$${parseFloat(item.avg_salary).toLocaleString('en-US', {minimumFractionDigits: 2, maximumFractionDigits: 2})}</td>
            <td>$${parseFloat(item.min_salary).toLocaleString('en-US', {minimumFractionDigits: 2, maximumFractionDigits: 2})}</td>
            <td>$${parseFloat(item.max_salary).toLocaleString('en-US', {minimumFractionDigits: 2, maximumFractionDigits: 2})}</td>
            <td>$${parseFloat(item.total_salary).toLocaleString('en-US', {minimumFractionDigits: 2, maximumFractionDigits: 2})}</td>
        </tr>
    `).join('');
}

// Delete modal functions
let employeeToDelete = null;

function setupDeleteModal() {
    const modal = document.getElementById('deleteModal');
    const closeBtn = document.querySelector('.close');
    
    closeBtn.onclick = closeDeleteModal;
    
    window.onclick = function(event) {
        if (event.target == modal) {
            closeDeleteModal();
        }
    }
}

function openDeleteModal(employeeId) {
    employeeToDelete = employeeId;
    document.getElementById('deleteModal').classList.add('show');
}

function closeDeleteModal() {
    document.getElementById('deleteModal').classList.remove('show');
    employeeToDelete = null;
}

function confirmDelete() {
    if (!employeeToDelete) return;
    
    fetch(`${API_BASE_URL}/employees/${employeeToDelete}`, {
        method: 'DELETE'
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            closeDeleteModal();
            loadEmployees();
        } else {
            alert('Error deleting employee: ' + data.message);
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Error deleting employee');
    });
}
