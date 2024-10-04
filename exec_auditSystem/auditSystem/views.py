from django.contrib.auth import login, authenticate
from django.db import connection
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Employee


# Create your views here.

def index(request):
    return render(request, 'begin.html')

@csrf_exempt
def signin(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main')

    return render(request, 'login.html')

def main(request):
    sql="""SELECT
    risk_status.st_color,
    risk_status.st_description,
    COUNT(employee.emp_id) AS Total_Employees
FROM
    risk_status
LEFT JOIN
    employee ON risk_status.status_id = employee.status_id
GROUP BY
    risk_status.st_color;
    """

    with connection.cursor() as cursor:
        cursor.execute(sql)
        result=cursor.fetchall()
    result_list = [{'st_color': row[0], 'st_description': row[1], 'Total_Employees': row[2]} for row in result]
    return render(request, 'main.html', {'result': result_list})

def statusReview(request):
    sql="""SELECT
    risk_status.st_color,
    employee.degree,
    employee.emp_name,
    department.dept_name
FROM
    employee
JOIN
    department ON employee.dept_id = department.dept_id
JOIN
    risk_status ON employee.status_id = risk_status.status_id;
    """
    with connection.cursor() as cursor:
        cursor.execute(sql)
        result=cursor.fetchall()

    return render(request, 'statusReview.html', {'sql': result})

def profile(request):
    sql="""SELECT
    risk_status.st_description,
    employee.emp_name,
    department.dept_name,
    department_position.position,
    employee.address,
    employee.phone_number,
    employee.email,
    employee.emp_id
FROM
    employee
JOIN
    department ON employee.dept_id = department.dept_id
JOIN
    risk_status ON employee.status_id = risk_status.status_id
JOIN
	department_position ON employee.position_id = department_position.position_id;"""
    with connection.cursor() as cursor:
        cursor.execute(sql)
        result=cursor.fetchall()

    return render(request, 'profile.html', {'sql': result})

def personal(request, emp_id):
    employee=Employee.objects.get(emp_id=emp_id)
    sql = """
        SELECT
            employee.emp_name,
            risk_status.st_description AS description,
            employee.emp_id,
            department.dept_name,
            department_position.position,
            employee.degree,
            employee.gender,
            personal_history.loan_overdue,
            personal_history.crime_history,
            personal_history.gambling_history
        FROM
            employee
        LEFT JOIN
            department ON employee.dept_id = department.dept_id
        LEFT JOIN
            department_position ON department_position.position_id = employee.position_id
        LEFT JOIN
            risk_status ON employee.status_id = risk_status.status_id
        LEFT JOIN
            personal_history ON employee.emp_id = personal_history.emp_id
        WHERE
            employee.emp_id = %s
        """

    with connection.cursor() as cursor:
        cursor.execute(sql,[emp_id])
        result=cursor.fetchone()
    return render(request, "personal.html", {'employee': result})

def admin(request):
    return render(request, 'admin.html')

def signout(request):
    return redirect('index')

def search(request):
    query = request.GET.get('name', '')

    # Modify the SQL to search for records containing the input query
    sql = """
    SELECT
        risk_status.st_description,
        employee.emp_name,
        department.dept_name,
        department_position.position,
        employee.address,
        employee.phone_number,
        employee.email,
        employee.emp_id
    FROM
        employee
    JOIN
        department ON employee.dept_id = department.dept_id
    JOIN
        risk_status ON employee.status_id = risk_status.status_id
    JOIN
        department_position ON employee.position_id = department_position.position_id
    WHERE
        employee.emp_name LIKE %s
    """

    with connection.cursor() as cursor:
        cursor.execute(sql, ['%' + query + '%'])
        result = cursor.fetchall()
    return render(request, 'result.html', {'results': result})

def result(request):
    return render(request, 'result.html')