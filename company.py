from app import get_connection


def add_company():

    company_name = input("Enter company name: ")
    location = input("Enter location: ")
    email = input("Enter company email: ")

    connection = get_connection()
    cursor = connection.cursor()

    query = """
    insert into companies (company_name, location, email)
    values (%s, %s, %s)
    """

    values = (company_name, location, email)

    cursor.execute(query, values)
    connection.commit()

    print("Company added successfully.")

    cursor.close()
    connection.close()


def view_companies():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("select * from companies")

    records = cursor.fetchall()

    print("\n----- COMPANIES -----")

    for record in records:
        print(record)

    cursor.close()
    connection.close()


def update_company():

    company_id = input("Enter company ID: ")

    company_name = input("Enter new company name: ")
    location = input("Enter new location: ")
    email = input("Enter new email: ")

    connection = get_connection()
    cursor = connection.cursor()

    query = """
    update companies
    set company_name=%s, location=%s, email=%s
    where company_id=%s
    """

    values = (company_name, location, email, company_id)

    cursor.execute(query, values)
    connection.commit()

    if cursor.rowcount > 0:
        print("Company updated successfully.")
    else:
        print("Company not found.")

    cursor.close()
    connection.close()


def delete_company():

    company_id = input("Enter company ID: ")

    connection = get_connection()
    cursor = connection.cursor()

    query = "delete from companies Where company_id=%s"

    cursor.execute(query, (company_id,))
    connection.commit()

    if cursor.rowcount > 0:
        print("Company deleted successfully.")
    else:
        print("Company not found.")

    cursor.close()
    connection.close()