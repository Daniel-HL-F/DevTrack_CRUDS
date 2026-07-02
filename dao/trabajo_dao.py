from database.conexion import Conexion
from models.trabajo import Trabajo


class TrabajoDAO:

    def __init__(self):
        self.db = Conexion()



    # Ver todos
    def obtener_todo(self):
        conn = self.db.obtener_conexion()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM trabajo")
        rows = cursor.fetchall()

        trabajos = []
        for r in rows:
            trabajos.append(Trabajo(r[0], r[1], r[2], r[3], r[4], r[5]))

        cursor.close()
        conn.close()
        return trabajos


    # Agregar
    
    def insertar(self, trabajo):
        conn = self.db.obtener_conexion()
        cursor = conn.cursor()

        sql = """
        INSERT INTO trabajo (titulo, descripcion, fecha_inicio, fecha_final, estado)
        VALUES (%s, %s, %s, %s, %s)
        """

        cursor.execute(sql, (
            trabajo.titulo,
            trabajo.descripcion,
            trabajo.fecha_inicio,
            trabajo.fecha_final,
            trabajo.estado
        ))

        conn.commit()
        cursor.close()
        conn.close()



    # Actualizar
   
    def actualizar(self, trabajo):
        conn = self.db.obtener_conexion()
        cursor = conn.cursor()

        sql = """
        UPDATE trabajo
        SET titulo=%s,
            descripcion=%s,
            fecha_inicio=%s,
            fecha_final=%s,
            estado=%s
        WHERE id=%s
        """

        cursor.execute(sql, (
            trabajo.titulo,
            trabajo.descripcion,
            trabajo.fecha_inicio,
            trabajo.fecha_final,
            trabajo.estado,
            trabajo.id
        ))

        conn.commit()
        cursor.close()
        conn.close()


    # Eliminar

    def eliminar(self, id):
        conn = self.db.obtener_conexion()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM trabajo WHERE id=%s", (id,))

        conn.commit()
        cursor.close()
        conn.close()