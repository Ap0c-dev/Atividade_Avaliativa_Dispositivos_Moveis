from kivy.uix.label import Label
from kivy.uix.popup import Popup
from control.alunoCtrl import AlunoCtrl

class ViewAluno:
    def __init__(self, gerencTela):
        self._gerencTela = gerencTela

    def cadAtualAluno(self):
        result = ""
    
        try:
            tela = self._gerencTela.get_screen("CadastroAluno")
            idAluno = tela.ids.lblIdAluno.text
            nomeAluno = tela.ids.txtNomeAluno.text
            dataNasc = tela.ids.txtNascAluno.text
            renda = tela.ids.txtRendaAluno.text
            turma = tela.ids.spTurma.text
            control = AlunoCtrl()

            if tela.ids.btCadAtualAluno.text == "Excluir":
                result = control.excluirAluno(idAluno)
            else:
                result = control.salvarAtualizarAluno(id=idAluno,nome=nomeAluno,dtNasc=dataNasc,renda_fam=renda,turma=turma)

                self._popJanela(result)
                self._limparTela(tela)
        except Exception as e:
            print(str(e))
            self._popJanela(f"Não foi possível {tela.ids.btCadAtualAluno.text} o aluno!!!")

    def _limparTelaListar(self,tela):
        cabecalho = [
            tela.ids.colIdAluno,
            tela.ids.colNomeAluno,
            tela.ids.colDtNasc,
            tela.ids.colRenda,
            tela.ids.colTurma,
            tela.ids.lblAtual,
            tela.ids.lblExcluir
        ]
        
        tela.ids.listaAlunos.clear_widgets()

        for c in cabecalho:
            tela.ids.listaAlunos.add_widget(c)

    def buscaAlunos(self, nome=""):
        control = AlunoCtrl()
        tela = self._gerencTela.get_screen("ListarAlunos")
        idPesq = tela.ids.inputIdAluno.text
        resultado = control.buscarAluno(id=idPesq, nome=nome)
        self._limparTelaListar(tela)
        for res in resultado:
            for r in res:
                if r.text == "Atualizar" or r.text == "Excluir":
                    r.bind(on_release= self.montarTelaAt)
                tela.ids.listaAlunos.add_widget(r)

    def montarTelaAt(self,botao):
        telaCad = self._gerencTela.get_screen("CadastroAluno")
        telaCad.ids.spTurma.values = self._montarSpinner()
        alunos=[]
        
        if botao.id:
            id = str(botao.id).replace("bt", "")
            control = AlunoCtrl()
            alunos = control.buscarAluno(id=id)
        
        for a in alunos:
            telaCad.ids.lblIdAluno.text = a[0].text
            telaCad.ids.txtNomeAluno.text = a[1].text
            telaCad.ids.txtNascAluno.text = a[2].text
            telaCad.ids.txtRendaAluno.text = a[3].text
            telaCad.ids.spTurma.text = a[4].text
            telaCad.ids.btCadAtualAluno.text = botao.text
        self._limparTelaListar(self._gerencTela.get_screen("ListarAlunos"))
        self._gerencTela.telaCadastroAluno()

    def _montarSpinner(self):
        listaValores = self._buscarTurmasTela()
        return listaValores

    def _buscarTurmasTela(self):
        control = AlunoCtrl()
        turmas = control.buscarTurmas()
        nomesTurmas =[]

        for turma in turmas:
            nomesTurmas.append(turma.nome)
        return nomesTurmas

    def _limparTela(self, tela):
        tela.ids.lblIdAluno.text = ""
        tela.ids.txtNomeAluno.text = ""
        tela.ids.txtNascAluno.text = ""
        tela.ids.txtRendaAluno.text = ""
        tela.ids.spTurma.text = "Selecione..."
        tela.ids.btCadAtualAluno.text = "Cadastrar"

    def _popJanela(self, texto=""):
        popup = Popup(title='Informação', content=Label(text=texto),auto_dismiss=True)
        popup.size_hint = (0.98, 0.4)
        popup.open()

    def alternarPesq(self, tipo):
        tela = self._gerencTela.get_screen("ListarAlunos")

        if tela.ids.inputIdAluno is not None:
            tela.ids.inputIdAluno.text = ""

        if tela.ids.inputPesqNome is not None:
            tela.ids.inputPesqNome.text = ""
            pesqNome = tela.ids.pesqNome
            pesqId = tela.ids.pesqId
            tela.ids.pesquisas.remove_widget(pesqNome)
            tela.ids.pesquisas.remove_widget(pesqId)

        if tipo == "id":
            pesqId.active = True