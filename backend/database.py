from datetime import datetime
from sqlalchemy import (
    create_engine, Column, Integer, String, Float, Date, DateTime, func
)
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import IntegrityError
from config import Config

Base = declarative_base()


class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, nullable=False)
    department = Column(String, nullable=False)
    salary = Column(Float, nullable=False)
    hire_date = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())


engine = create_engine(Config.SQLALCHEMY_DATABASE_URI, echo=False, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)


def init_db():
    """Create database tables if they don't exist."""
    Base.metadata.create_all(bind=engine)

def add_employee(first_name, last_name, email, phone, department, salary, hire_date):
    """Add a new employee to the database."""
    with SessionLocal() as session:
        try:
            emp = Employee(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                department=department,
                salary=float(salary),
                hire_date=hire_date
            )
            session.add(emp)
            session.commit()
            session.refresh(emp)
            return {'success': True, 'id': emp.id, 'message': 'Employee added successfully'}
        except IntegrityError as e:
            session.rollback()
            return {'success': False, 'message': f'Error: {str(e.orig)}'}
        except Exception as e:
            session.rollback()
            return {'success': False, 'message': f'Error: {str(e)}'}

def get_all_employees():
    """Retrieve all employees ordered by id desc."""
    try:
        with SessionLocal() as session:
            rows = session.query(Employee).order_by(Employee.id.desc()).all()
            return [{
                'id': r.id,
                'first_name': r.first_name,
                'last_name': r.last_name,
                'email': r.email,
                'phone': r.phone,
                'department': r.department,
                'salary': r.salary,
                'hire_date': r.hire_date,
                'created_at': r.created_at.isoformat() if r.created_at else None,
                'updated_at': r.updated_at.isoformat() if r.updated_at else None
            } for r in rows]
    except Exception as e:
        return {'error': str(e)}

def get_employee_by_id(employee_id):
    """Retrieve a specific employee by ID."""
    try:
        with SessionLocal() as session:
            r = session.get(Employee, int(employee_id))
            if not r:
                return None
            return {
                'id': r.id,
                'first_name': r.first_name,
                'last_name': r.last_name,
                'email': r.email,
                'phone': r.phone,
                'department': r.department,
                'salary': r.salary,
                'hire_date': r.hire_date,
                'created_at': r.created_at.isoformat() if r.created_at else None,
                'updated_at': r.updated_at.isoformat() if r.updated_at else None
            }
    except Exception as e:
        return {'error': str(e)}

def search_employees(query):
    """Search employees by first name, last name, or email."""
    try:
        like = f"%{query}%"
        with SessionLocal() as session:
            rows = session.query(Employee).filter(
                (Employee.first_name.ilike(like)) |
                (Employee.last_name.ilike(like)) |
                (Employee.email.ilike(like))
            ).order_by(Employee.id.desc()).all()
            return [
                {
                    'id': r.id,
                    'first_name': r.first_name,
                    'last_name': r.last_name,
                    'email': r.email,
                    'phone': r.phone,
                    'department': r.department,
                    'salary': r.salary,
                    'hire_date': r.hire_date,
                    'created_at': r.created_at.isoformat() if r.created_at else None,
                    'updated_at': r.updated_at.isoformat() if r.updated_at else None
                }
                for r in rows
            ]
    except Exception as e:
        return {'error': str(e)}

def filter_by_department(department):
    """Filter employees by department ordered by salary desc."""
    try:
        with SessionLocal() as session:
            rows = session.query(Employee).filter(Employee.department == department).order_by(Employee.salary.desc()).all()
            return [
                {
                    'id': r.id,
                    'first_name': r.first_name,
                    'last_name': r.last_name,
                    'email': r.email,
                    'phone': r.phone,
                    'department': r.department,
                    'salary': r.salary,
                    'hire_date': r.hire_date,
                    'created_at': r.created_at.isoformat() if r.created_at else None,
                    'updated_at': r.updated_at.isoformat() if r.updated_at else None
                }
                for r in rows
            ]
    except Exception as e:
        return {'error': str(e)}

def get_all_departments():
    """Get list of all departments."""
    try:
        with SessionLocal() as session:
            rows = session.query(Employee.department).distinct().order_by(Employee.department).all()
            return [r[0] for r in rows]
    except Exception as e:
        return {'error': str(e)}

def get_salary_info():
    """Get salary tracking information grouped by department."""
    try:
        from sqlalchemy import func
        with SessionLocal() as session:
            rows = session.query(
                Employee.department,
                func.count().label('total_employees'),
                func.avg(Employee.salary).label('avg_salary'),
                func.min(Employee.salary).label('min_salary'),
                func.max(Employee.salary).label('max_salary'),
                func.sum(Employee.salary).label('total_salary')
            ).group_by(Employee.department).order_by(func.sum(Employee.salary).desc()).all()

            result = []
            for r in rows:
                result.append({
                    'department': r[0],
                    'total_employees': int(r[1]),
                    'avg_salary': float(r[2]) if r[2] is not None else None,
                    'min_salary': float(r[3]) if r[3] is not None else None,
                    'max_salary': float(r[4]) if r[4] is not None else None,
                    'total_salary': float(r[5]) if r[5] is not None else None,
                })
            return result
    except Exception as e:
        return {'error': str(e)}

def update_employee(employee_id, first_name, last_name, email, phone, department, salary, hire_date):
    """Update an existing employee."""
    try:
        with SessionLocal() as session:
            emp = session.get(Employee, int(employee_id))
            if not emp:
                return {'success': False, 'message': 'Employee not found'}
            emp.first_name = first_name
            emp.last_name = last_name
            emp.email = email
            emp.phone = phone
            emp.department = department
            emp.salary = float(salary)
            emp.hire_date = hire_date
            session.commit()
            return {'success': True, 'message': 'Employee updated successfully'}
    except IntegrityError as e:
        return {'success': False, 'message': f'Error: {str(e.orig)}'}
    except Exception as e:
        return {'success': False, 'message': f'Error: {str(e)}'}

def delete_employee(employee_id):
    """Delete an employee by id."""
    try:
        with SessionLocal() as session:
            emp = session.get(Employee, int(employee_id))
            if not emp:
                return {'success': False, 'message': 'Employee not found'}
            session.delete(emp)
            session.commit()
            return {'success': True, 'message': 'Employee deleted successfully'}
    except Exception as e:
        return {'success': False, 'message': f'Error: {str(e)}'}
