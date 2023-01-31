import pyodbc
import pycgrlib.utils

class Cgr_db():
    """
    Clase Utilizada para la conexion a la base de datos
    """

    def __init__(self, p_db_username, p_db_password, p_db_server, p_db):
        """
        En el constructor se establece el usuario, password y servidor al cual se conecta

        Args:
            p_bd ([str]): String con el nombre de la base de datos a utilizar, debe estar incluido en el diccionario DB
        """
        self.USERNAME = p_db_username
        self.PASSWORD = p_db_password
        self.SERVER = p_db_server
        self.DATABASE = p_db
        self.isConected = False
        self.obtenerConexion()


    def __str__(self):
        """Funcion toString para imprimir los datos del objeto

        Returns:
            [str]: String con el nombre del servidor base de datos, cursor y si esta conectado
        """
        return "Servidor: " + self.SERVER + "\n" + "Base de datos: " + self.DATABASE + "\n"+"Cursor: " + str(self.cursor) + "\n"+" Conectado: " + str(self.isConected)


    def obtenerConexion(self):
        """Obtener Conexion
        Utiliza los parametros de servidor, password y usuario para conectarse a la base de datos
        Si se conecta correctamente establece el atributo isConected como True
        """

        try:
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                                  self.SERVER+';DATABASE='+self.DATABASE+';UID='+self.USERNAME+';PWD=' + self.PASSWORD)
            self.cursor = cnxn.cursor()
            self.isConected = True
            cgr_utils.imprimir(
                f"Conexion correcta a la base de datos: {self.DATABASE}")
        except Exception as e:
            self.cursor = None
            self.isConected = False
            cgr_utils.imprimir(f"Ocurrio un error al conectarse: {e}")


    def ejecutarSelect(self, consulta, *params):
        """Ejecuta una consulta tipo Select a la base de datos

        Args:
            consulta ([string]): Es el query del select a ejecutar en la BD
            params ([tuple]): Es una tupla con los parametros a ejecutar en el query anterior. Este parametro es opcional

        Returns:
            [cursor]: Si se ejecuta correctamente retorna el cursor con los datos, sino devuelve None
        """
        try:
            if self.isConected:
                if params is None:
                    self.cursor.execute(consulta)
                else:
                    self.cursor.execute(consulta, *params)

                return self.cursor
            else:
                cgr_utils.imprimir(
                    "No se puede conectar a la base de datos. No se pueden realizar consultas en este momento")
                return None
        except Exception as e:
            cgr_utils.imprimir(f"No se puede realizar la consulta. {str(e)}")
            return None


    def ejecutarSelect_api(self, consulta, *params):
        """Ejecuta una consulta tipo Select a la base de datos

        Args:
            consulta ([string]): Es el query del select a ejecutar en la BD
            params ([tuple]): Es una tupla con los parametros a ejecutar en el query anterior. Este parametro es opcional

        Returns:
            [cursor]: Si se ejecuta correctamente retorna el cursor con los datos, sino devuelve None
        """
        try:
            if self.isConected:
                if params is None:
                    self.cursor.execute(consulta)
                else:
                    self.cursor.execute(consulta, *params)

                data = []
                columns = [column[0] for column in self.cursor.description]

                for row in self.cursor.fetchall():
                    row = [str(x) for x in row]
                    data.append(dict(zip(columns, row)))
                return {"resultado": True, "mensaje": "", "datos": data}
            else:
                cgr_utils.imprimir(
                    "No se puede conectar a la base de datos. No se pueden realizar consultas en este momento")
                return {"resultado": False, "mensaje": "No se puede conectar a la base de datos. No se pueden realizar consultas en este momento", "datos": None}
        except Exception as e:
            cgr_utils.imprimir(f"No se puede realizar la consulta. {str(e)}")
            return {"resultado": False, "mensaje": "No se puede realizar la consulta", "datos": None}


    def ejecutarInsert(self, consulta, *params):
        """Ejecuta una consulta tipo Insert a la base de datos

        Args:
            consulta ([string]): Es el query del insert a ejecutar en la BD
            params ([tuple]): Es una tupla con los parametros a ejecutar en el query anterior. Este parametro es obligatorio

        Returns:
            [boolean]: Retorna True si se ejecuto la consulta, False si ocurrio un error
        """
        try:
            if self.isConected:
                self.cursor.execute(consulta, *params)
                self.cursor.commit()
                return True
            else:
                cgr_utils.imprimir(
                    "No se puede conectar a la base de datos. No se pueden realizar consultas en este momento")
                return False
        except Exception as e:
            cgr_utils.imprimir(f"No se puede realizar la consulta. {e}")
            return False


    def ejecutarInsert_devuelve_id(self, consulta, *params):
        """Ejecuta una consulta tipo Insert a la base de datos

        Args:
            consulta ([string]): Es el query del insert a ejecutar en la BD
            params ([tuple]): Es una tupla con los parametros a ejecutar en el query anterior. Este parametro es obligatorio

        Returns:
            [boolean]: Retorna True si se ejecuto la consulta, False si ocurrio un error
        """
        try:
            if self.isConected:
                self.cursor.execute(consulta, *params)
                self.cursor.execute("SELECT @@IDENTITY AS ID;")
                id = self.cursor.fetchone()[0]
                self.cursor.commit()

                return id
            else:
                cgr_utils.imprimir(
                    "No se puede conectar a la base de datos. No se pueden realizar consultas en este momento")
                return -1
        except Exception as e:
            cgr_utils.imprimir(f"No se puede realizar la consulta. {e}")
            return -1


    def ejecutarInsert_api(self, consulta, *params):
        """Ejecuta una consulta tipo Insert o update a la base de datos y devuelve un JSON
        Args:
            consulta ([string]): Es el query del insert a ejecutar en la BD
            params ([tuple]): Es una tupla con los parametros a ejecutar en el query anterior. Este parametro es obligatorio

        Returns:
            [boolean]: Retorna True si se ejecuto la consulta, False si ocurrio un error
        """
        try:
            if self.isConected:
                if params is None:
                    self.cursor.execute(consulta)
                    self.cursor.commit()
                else:
                    self.cursor.execute(consulta, *params)
                    self.cursor.commit()

                if self.cursor.rowcount >= 1:
                    return {"resultado": True, "mensaje": "El registro se actualizó correctamente", "datos": self.cursor.rowcount}
                else:
                    return {"resultado": False, "mensaje": "No se pudo actualizar el dato", "datos": "0"}
            else:
                cgr_utils.imprimir(
                    "No se puede conectar a la base de datos. No se pueden realizar consultas en este momento")
                return {"resultado": False, "mensaje": "No se puede conectar a la base de datos. No se pueden realizar consultas en este momento", "datos": None}
        except Exception as e:
            cgr_utils.imprimir(f"No se puede realizar la consulta. {str(e)}")
            return {"resultado": False, "mensaje": "No se puede realizar la consulta", "datos": None}
