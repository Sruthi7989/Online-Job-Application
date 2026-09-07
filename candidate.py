from app import get_connection


def add_candidate():

    name = input("Enter candidate name: ")
    email = input("Enter email: ")
    phone = input("Enter phone: ")
    skills = input("Enter skills: ")

    connection = get_connection()
    cursor = connection.cursor()

    query = """
    insert into candidates (name, email, phone, skills)
    values (%s, %s, %s, %s)
    """

    values = (name, email, phone, skills)

    cursor.execute(query, values)
    connection.commit()

    print("Candidate added successfully.")

    cursor.close()
    connection.close()


def view_candidates():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("select * from candidates")

    records = cursor.fetchall()

    print("\n----- CANDIDATES -----")

    for record in records:
        print(record)

    cursor.close()
    connection.close()


def update_candidate():

    candidate_id = input("Enter candidate ID: ")

    name = input("Enter new name: ")
    email = input("Enter new email: ")
    phone = input("Enter new phone: ")
    skills = input("Enter new skills: ")

    connection = get_connection()
    cursor = connection.cursor()

    query = """
    update candidates
    set name=%s, email=%s, phone=%s, skills=%s
    WHERE candidate_id=%s
    """

    values = (name, email, phone, skills, candidate_id)

    cursor.execute(query, values)
    connection.commit()

    if cursor.rowcount > 0:
        print("Candidate updated successfully.")
    else:
        print("Candidate not found.")

    cursor.close()
    connection.close()


def delete_candidate():

    candidate_id = input("Enter candidate ID: ")

    connection = get_connection()
    cursor = connection.cursor()

    query = "delete from candidates Where candidate_id=%s"

    cursor.execute(query, (candidate_id,))
    connection.commit()

    if cursor.rowcount > 0:
        print("Candidate deleted successfully.")
    else:
        print("Candidate not found.")

    cursor.close()
    connection.close()