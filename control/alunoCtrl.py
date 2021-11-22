import locale
from kivy.uix.button import Button
from kivy.uix.label import Label
from control.util import Util
from model.alunoDAO import AlunoDAO
from model.alunoModel import Aluno
from model.turmaDAO import TurmaDAO

class AlunoCtrl:

    def salvarAtualizarAluno(self,id=None, nome="", dtNasc="", renda_fam="",turma=""):
        daoTurma = TurmaDAO()
        daoAluno = AlunoDAO()
    
        if len(nome) > 3:
            inseriuAtualizou = False
            dataNasc = self._dtNascTelaBanco(dtNasc)
            renda = self._rendaTelaBanco(renda_fam)
            turmaBanco = daoTurma.buscarTurmaPorNome(turma)
            aluno = Aluno(nome=nome, dt_nasc=dataNasc, renda=renda, turma=turmaBanco)

            if id:
                aluno.id = id
                inseriuAtualizou = daoAluno.atualizarAluno(aluno)
            else:
                inseriuAtualizou = daoAluno.inserirAluno(aluno)
            if inseriuAtualizou:
                return "Aluno inserido ou atualizado com sucesso!!!"
            else:
                return "O aluno não pôde ser inserido ou atualizado!"
        else:
            return "O nome deve ter mais de 3 caracteres"

    def _dtNascTelaBanco(self, dtNasc):
        """
Converte a data no formato "dd/mm/aaaa" para "aaaa-mm-dd"
:param dtNasc: a data de nascimento da tela
:return: a data de nascimento no formato aceito pelo banco
"""
        if Util.validaData(dtNasc):
            d = dtNasc.split("/") #converte a string em list
            dataBanco = d[2] + "-" + d[1] + "-" + d[0]
            return dataBanco #retorna a data formatada
        else:
            return ""

    def _rendaTelaBanco(self, renda_fam):
        """
Converte a renda no formato "9.999,99" para 9999.99
:param renda_fam: a renda da família
:return: a renda no formato aceito pelo BD
"""
        renda = renda_fam.replace(".","")
        renda = renda.replace(",",".")
        return float(renda)
    
    def excluirAluno(self,id):
        dao = AlunoDAO()