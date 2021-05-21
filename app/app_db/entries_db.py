from . import get_connection


def create(title: str, description: str, original_file_sha1):
    connection = get_connection()
    cursor = connection.cursor()

    sql = "INSERT INTO entries (title, description, original_file) VALUES (%s, %s, %s)"
    val = (title, description, original_file_sha1)

    cursor.execute(sql, val)
    connection.commit()
    connection.close()


def read_all():
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    sql = "SELECT * FROM entries"

    cursor.execute(sql)
    result_set = cursor.fetchall()

    connection.commit()
    connection.close()
    return result_set


def read_by_id(entry_id: int):
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    sql = "SELECT * FROM entries WHERE id=%s"
    val = (entry_id, )

    cursor.execute(sql, val)
    result_set = cursor.fetchall()

    connection.commit()
    connection.close()
    return result_set
