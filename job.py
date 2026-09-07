from app import get_connection


def add_job():

    company_id = input("Enter company ID: ")
    job_title = input("Enter job title: ")
    job_type = input("Enter job type: ")
    salary = input("Enter salary: ")

    connection = get_connection()
    cursor = connection.cursor()

    query = """
    insert into jobs
    (company_id, job_title, job_type, salary)
    values (%s, %s, %s, %s)
    """

    values = (company_id, job_title, job_type, salary)

    cursor.execute(query, values)
    connection.commit()

    print("Job added successfully.")

    cursor.close()
    connection.close()


def view_jobs():

    connection = get_connection()
    cursor = connection.cursor()

    query = """
    select jobs.job_id,
           companies.company_name,
           jobs.job_title,
           jobs.job_type,
           jobs.salary
    from jobs
    join companies
    on jobs.company_id = companies.company_id
    """

    cursor.execute(query)

    records = cursor.fetchall()

    print("\n----- JOBS -----")

    for record in records:
        print(record)

    cursor.close()
    connection.close()


def update_job():

    job_id = input("Enter job ID: ")

    job_title = input("Enter new job title: ")
    job_type = input("Enter new job type: ")
    salary = input("Enter new salary: ")

    connection = get_connection()
    cursor = connection.cursor()

    query = """
    update jobs
    set job_title=%s, job_type=%s, salary=%s
    where job_id=%s
    """

    values = (job_title, job_type, salary, job_id)

    cursor.execute(query, values)
    connection.commit()

    if cursor.rowcount > 0:
        print("Job updated successfully.")
    else:
        print("Job not found.")

    cursor.close()
    connection.close()


def delete_job():

    job_id = input("Enter job ID: ")

    connection = get_connection()
    cursor = connection.cursor()

    query = "delete  from jobs where job_id=%s"

    cursor.execute(query, (job_id,))
    connection.commit()

    if cursor.rowcount > 0:
        print("Job deleted successfully.")
    else:
        print("Job not found.")

    cursor.close()
    connection.close()