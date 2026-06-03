# QUICK START GUIDE

## ⚡ 30-Second Setup

### Windows Users:
1. Double-click `run.bat`
2. Wait for the server to start
3. Open browser → http://localhost:5000

### Mac/Linux Users:
1. Open terminal in this folder
2. Run: `chmod +x run.sh && ./run.sh`
3. Open browser → http://localhost:5000

---

## 📋 Manual Setup (If Automatic Fails)

### Step 1: Open Terminal/Command Prompt
Navigate to the `backend` folder

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Start Server
```bash
python app.py
```

### Step 4: Open Browser
Go to: **http://localhost:5000**

---

## ✨ Features Available

| Feature | How to Use |
|---------|-----------|
| **View Employees** | Open dashboard, see all employees |
| **Add Employee** | Click "Add Employee" → Fill form → Submit |
| **Edit Employee** | Click "Edit" button → Modify → Update |
| **Delete Employee** | Click "Delete" → Confirm deletion |
| **Search** | Use search box on dashboard |
| **Filter by Dept** | Select department from dropdown |
| **Salary Info** | Click "Salary Info" tab for statistics |

---

## 🎯 Sample Employee Data to Add

Try adding this employee to test:
- **First Name**: John
- **Last Name**: Doe
- **Email**: john.doe@company.com
- **Phone**: 555-0101
- **Department**: IT
- **Salary**: 75000
- **Hire Date**: 2024-01-15

---

## 🔧 Troubleshooting

### "Port 5000 already in use"
- Close other applications using port 5000, or
- Edit `backend/app.py` line with `port=5000` → change to `port=5001`

### "Python not found"
- Install Python from https://www.python.org/downloads/
- Make sure to check "Add Python to PATH" during installation

### "ModuleNotFoundError"
- Run: `pip install -r requirements.txt` again
- Restart Python if already running

### "CORS Error"
- Restart the server
- Clear browser cache
- Try in incognito/private mode

---

## 📚 API Endpoints (For Advanced Users)

```
GET    /api/employees                  - Get all employees
GET    /api/employees/<id>             - Get single employee
POST   /api/employees                  - Add employee
PUT    /api/employees/<id>             - Update employee
DELETE /api/employees/<id>             - Delete employee
GET    /api/search?q=query             - Search employees
GET    /api/departments                - Get all departments
GET    /api/filter/department/<dept>   - Filter by department
GET    /api/salary-info                - Get salary statistics
```

---

## 💾 Database Location

Database file: `backend/employees.db`
- Created automatically on first run
- SQLite format
- Stores all employee data

---

## ⚙️ Technology Stack

```
Backend:  Python + Flask + SQLite
Frontend: HTML + CSS + JavaScript (Vanilla)
Database: SQLite (No external database needed!)
```

---

## 🚀 Next Steps

1. Add some sample employees
2. Try searching and filtering
3. Check salary information
4. Explore the dashboard

Enjoy managing your employees! 😊

---

## 📞 Need Help?

- Check the full README.md for detailed documentation
- Review code comments in Python files
- Check browser console (F12) for any errors
