import psycopg2


class Conexion:

    def obtener_conexion(self):
        return psycopg2.connect(
            host="localhost",
            database="devtrack_3b26",
            user="postgres",
            password="1234",
            port="5432"
        )