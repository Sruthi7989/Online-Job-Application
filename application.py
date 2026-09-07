from  app import get_connection


def apply_for_job():

    candidate_id = input("Enter candidate ID: ")
    job_id = input("Enter job ID: ")
    application_date = input("Enter date (YYYY-MM-DD): ")

    connection = get_connection()
    cursor = connection.cursor()

    query = """
    insert into applications
    (candidate_id, job_id, application_date, status)
    values (%s, %s, %s, %s)
    """

    values = (
        candidate_id,
        job_id,
        application_date,
        "Applied"
    )

    cursor.execute(query, values)
    connection.commit()

    print("Application submitted successfully.")

    cursor.close()
    connection.close()


def view_applications():

    connection = get_connection()
    cursor = connection.cursor()

    query = """
    select
        applications.application_id,
        candidates.name,
        jobs.job_title,
        applications.application_date,
        applications.status
    from applications

    join candidates
    on applications.candidate_id = candidates.candidate_id

    join jobs
    on applications.job_id = jobs.job_id
    """

    cursor.execute(query)

    records = cursor.fetchall()

    print("\n----- APPLICATIONS -----")

    for record in records:
        print(record)

    cursor.close()
    connection.close()


def update_application():

    application_id = input("Enter application ID: ")

    status = input(
        "Enter new status "
        "(Applied/Shortlisted/Rejected/Selected): "
    )

    connection = get_connection()
    cursor = connection.cursor()

    query = """
    update applications
    set status=%s
    where application_id=%s
    """

    values = (status, application_id)

    cursor.execute(query, values)
    connection.commit()

    if cursor.rowcount > 0:
        print("Application status updated.")
    else:
        print("Application not found.")

    cursor.close()
    connection.close()


def delete_application():

    application_id = input("Enter application ID: ")

    connection = get_connection()
    cursor = connection.cursor()

    query = """
    delete from applications
    where application_id=%s
    """

    cursor.execute(query, (application_id,))
    connection.commit()

    if cursor.rowcount > 0:
        print("Application deleted successfully.")
    else:
        print("Application not found.")

    cursor.close()
    connection.close()