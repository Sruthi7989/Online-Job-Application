from pymysql import connect


def get_connection():
    connection =connect(
        host="localhost",
        user="root",
        password="sruthipuchakayala@123",
        database="job_portal"
    )

    return connection