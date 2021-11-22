from kivy.uix.button import Button
from kivy.uix.label import Label
from model.turmaModel import Turma
from model.turmaDAO import TurmaDAO
class TurmaCtrl:

    def salvarAtualizarTurma(self,id=None, nome="", turno=""):
        if len(nome) > 3:
            inseriuAtualizou = False
            turma = Turma(nome=nome, turno=turno);
            dao = TurmaDAO()
            if id:
                turma.id = id
                inseriuAtualizou = dao.atualizarTurma(turma)
            else:
                inseriuAtualizou = dao.inserirTurma(turma)

            if inseriuAtualizou:
                return "Turma inserida ou atualizada com sucesso!!!"
            else:
                return "A turma não pode ser inserida ou atualizada!"
        else:
            return "O nome deve ter mais de 3 caracteres"

    def excluirTurma(self,id):
        dao = TurmaDAO()
        excluiu = dao.excluirTurma(str(id))
        if excluiu:
            return "Turma excluida com sucesso!!!"
        else:
            return "A turma não pôde ser excluída!"

    def buscarTurma(self, id="", inicio=0, quant=10):
        dao = TurmaDAO()
        res=""
        if id != "":
            res = dao.buscarTurma(id)
        else:
            res = dao.buscarTurmas(inicio=inicio,quant=quant)
        itens=[]
        if type(res) is Turma:
            minhaturma = []
            minhaturma.append(self._criarLabel(res.id, 0.2))
            minhaturma.append(self._criarLabel(res.nome, 0.6))
            minhaturma.append(self._criarLabel(res.turno, 0.2))
            minhaturma.append(self._criarBotao("Atualizar", res.id))
            minhaturma.append(self._criarBotao("Excluir", res.id))
            itens.append(minhaturma)

        if type(res) is list:
            for turma in res:
                minhaturma = []
                minhaturma.append(self._criarLabel(turma.id, 0.2))
                minhaturma.append(self._criarLabel(turma.nome, 0.6))
                minhaturma.append(self._criarLabel(turma.turno, 0.2))
                minhaturma.append(self._criarBotao("Atualizar",turma.id))
                minhaturma.append(self._criarBotao("Excluir",turma.id))
                itens.append(minhaturma)
        return itens
    
    def _criarLabel(self, texto, tam):
        label = Label()
        label.text = str(texto)
        label.size_hint_y = None
        label.size_hint_x = tam
        label.height = '30dp'
        return label

    def _criarBotao(self, texto, id):
        botao = Button()
        botao.text = texto
        botao.id = "bt"+str(id)
        botao.font_size = '10sp'
        botao.size_hint_y = None
        botao.height = '30dp'
        botao.size_hint_x = .1
        return botao