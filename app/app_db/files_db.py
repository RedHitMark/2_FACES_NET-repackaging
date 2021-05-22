from . import get_connection


def create(file_sha1: str, file_size: int):
    connection = get_connection()
    cursor = connection.cursor()

    sql = "INSERT INTO apk_files (sha1_hash, file_size) VALUES (%s, %s)"
    val = (file_sha1, file_size)

    cursor.execute(sql, val)
    connection.commit()
    connection.close()


def delete():
    return


def read_all():
    return


def read(sha1: str):
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    sql = "SELECT * FROM apk_files WHERE sha1_hash = %s"
    val = (sha1, )

    cursor.execute(sql, val)
    result_set = cursor.fetchall()

    connection.commit()
    connection.close()
    return result_set

