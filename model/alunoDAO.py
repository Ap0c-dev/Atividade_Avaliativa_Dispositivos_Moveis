from model.conexaoDB import Conexaodb
from model.alunoModel import Aluno
from model.turmaDAO import TurmaDAO

class AlunoDAO:
    __slots__ = (
    '_con'
    )
    def __init__(self):
        self._con = Conexaodb.conectar()

    def inserirAluno(self, aluno):
        """
Adiciona uma turma ao banco de dados
:param aluno: Espera um objeto do tipo aluno
:return: True caso o aluno seja adicionado e False caso contrario
"""
        sql = "INSERT INTO aluno(nome,dt_nasc,renda_familiar,Turma_id) "
        sql += "VALUES (?,?,?,?);"
        valores = (aluno.nome,
        aluno.dt_nasc,
        aluno.renda_familiar,
        aluno.turma.id
        )
        res = Conexaodb.executarSql(sql, valores)
        return res == 1

    def atualizarAluno(self, aluno):
        """
Atualiza um aluno no banco de dados
:param aluno: Espera um objeto do tipo aluno
:return: True caso o aluno seja atualizado e False caso contrario
"""
        sql = "UPDATE Aluno SET nome=?, dt_nasc=?, " \
        "renda_familiar=?, Turma_id=? WHERE id=?;"
        valores = (aluno.nome, aluno.dt_nasc,
        aluno.renda_familiar, aluno.turma.id,
        aluno.id)
        res = Conexaodb.executarSql(sql, valores)
        return res == 1

    def excluirAluno(self, idAluno):
        """
Exclui um aluno do banco de dados
:param id: Espera o id(string) do aluno a ser excluído
:return: True caso o aluno seja excluído e False caso contrario
"""
        sql = "DELETE FROM Aluno WHERE id = " + str(idAluno)
        cursor = self._con.cursor()
        cursor.execute(sql)
        self._con.commit()
        res = cursor.rowcount
        return res == 1

    def buscarAlunoId(self, id):
        """
Busca um aluno no banco de dados
:param id: Espera o id do aluno a ser buscado
:return: O aluno, de acordo com o id informado
62 """
        try:
            sql = "SELECT id,nome,dt_nasc,renda_familiar,Turma_id" \
            " FROM Aluno WHERE id =" + str(id) + ";"
            cursor = self._con.cursor()
            cursor.execute(sql)
            res = cursor.fetchone()
            aluno = self.montarAlunoBanco(res)
            return aluno
        except Exception as e:
            print(str(e))
            return None

    def montarAlunoBanco(self, res):
        aluno = Aluno(id=res[0], nome=res[1], dt_nasc=res[2], renda=res[3])
        if res[4]:
            turma = TurmaDAO().buscarTurma(res[4])
            aluno.turma = turma
        return aluno

    def buscarAlunos(self, quant=100, nome=""):
        """
Busca os alunos do banco de dados
:param quant: Espera a quantidade de alunos a serem buscados
:return: diversas Turmas de acordo com a quantidade informada
"""
        alunos = []
        try:
            sql = "SELECT id,nome,dt_nasc,renda_familiar,Turma_id" \
            " FROM Aluno"
            sql += " WHERE nome LIKE '%"+ nome +"%';"
            cursor = self._con.cursor()
            cursor.execute(sql)
            res = cursor.fetchmany(quant)
            alunos = self._montarResultado(res)
            return alunos
        except Exception as e:
            print(e)
            return(alunos)

        def _montarResultado(self, res):
            alunos = []
            for linha in res:
                aluno = self.montarAlunoBanco(linha)
                alunos.append(aluno)
            return alunos

