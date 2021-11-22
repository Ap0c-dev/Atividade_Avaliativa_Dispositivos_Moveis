import mysql.connector 

class ConexaoDb:
    _conn = None
    _host = "localhost"
    _user = "root"
    _password = ""
    _bd = "escolaTeste"

    @staticmethod
    def conectar ():
        if ConexaoDb._conn == None:
            try:
                ConexaoDb._con = mysql.connector.connect(
                    host = ConexaoDb._host,
                    database = ConexaoDb._bd,
                    user = ConexaoDb._user,
                    password = ConexaoDb._password )
                return ConexaoDb._conn
            except Exception as erro:
                return erro
        return ConexaoDb._conn
    
    @staticmethod
    def executarSqul(sql, dados):
        try:
            cursor = ConexaoDb._conn.cursor(prepared=true)
            cursor.execute(sql, dados)
            ConexaoDb._conn.commit()
            return cursor.rowcount
        except Exception as e:
            return e