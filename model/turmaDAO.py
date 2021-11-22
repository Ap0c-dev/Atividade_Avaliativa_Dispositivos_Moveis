from model.conexaoDB import Conexaodb
from model.turmaModel import Turma

class TurmaDAO:
    __slots__ = (
        '_con'
        )
    def __init__(self):
        self._con = Conexaodb.conectar()
    
    def inserirTurma(self, turma):
        """
        Adiciona uma turma ao banco de dados
        :param turma: Espera um objeto do tipo turma
        :return: True caso a turma seja adicionada e False caso contrario
        """
        sql = "INSERT INTO Turma(nome,turno) VALUES (?,?);"
        valores = (turma.nome, turma.turno)
        res = Conexaodb.executarSql(sql,valores)
        return res == 1

    def atualizarTurma(self, turma):
        """
Atualiza uma turma no banco de dados
:param turma: Espera um objeto do tipo turma
:return: True caso a turma seja atualizada e False caso contrario
"""
        sql = "UPDATE Turma SET nome=?, turno=? WHERE id=?;"
    
        valores = (turma.nome, turma.turno, turma.id)
        res = Conexaodb.executarSql(sql,valores)
        return res == 1

    def excluirTurma(self, id):
        """
Exclui uma turma do banco de dados
:param id: Espera o id(string) da turma a ser excluída
:return: True caso a turma seja excluída e False caso contrario
"""
        sql = "DELETE FROM turma WHERE id = " + str(id)
        cursor = self._con.cursor()
        cursor.execute(sql)
        self._con.commit()
        res = cursor.rowcount
        return res == 1

    def buscarTurma(self,id):
        """
Busca uma turma no banco de dados
:param id: Espera o id da turma a ser buscada
:return: A turma de acordo com o id informado
"""
        try:
            sql = "SELECT id,nome,turno FROM turma WHERE id ="+str(id)+ ";"
            cursor = self._con.cursor()
            cursor.execute(sql)
            res = cursor.fetchone()
            turma = Turma(res[0], res[1], res[2])
            return turma
        except Exception as e:
            print(str(e))
            return None

    def buscarTurmaPorNome (self, nome):
        try:
            sql = sql = "SELECT id,nome,turno FROM turma WHERE nome = '"+ nome +"';"
            cursor = self._con.cursor()
            cursor.execute(sql)
            res = cursor.fetchone()
            turma = Turma(res[0], res[1], res[2])
            return turma
        except Exception as e:
            print(str(e))
            return None

    def burcarTurmas(self, inico=0, quant=100):
        turmas = []
        try:
            sql = "SELECT id,nome,turno FROM turma"
            cursor = self._con.cursor()
            cursor.execute(sql)
            res = cursor.fetchmany(quant)
            turmas = self._montarResultado(res)
            return turmas
        except Exception as e:
            print(e)
            return turmas

    def _montarResultado(self, res):
        turmas = []
        for linha in res:
            turma = Turma(linha[0], linha[1], linha[2])
            turmas.append(turma)
        return turmas
