from _typeshed import Self


class Aluno:
    __slots__ = (
        '_id',
        '_nome',
        '_dt_nasc',
        '_renda_familiar',
        '_turma'
    )
    def __init__(self, id=None, nome="" , dt_nasc="", renda=0.00, turma = ""):
        self.id = id
        self.nome = nome
        self.dt_nasc = dt_nasc
        self.renda_familiar = renda
        self.turma = turma
    
    @property
    def id(self):
        return self._id

    @id.setter
    def id (self, id):
        self._id = id
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome
    
    @property
    def dt_nasc(self):
        return self._dt_nasc
    
    @dt_nasc.setter
    def det_nasc(self, dt_nasc):
        self._dt_nasc = dt_nasc

    @property
    def renda_familiar(self):
        return self._renda_familiar

    @renda_familiar.setter
    def renda_familiar (self, renda):
        self._renda_familiar = renda
    
    @property
    def turma(self):
        return self._turma
    
    @turma.setter
    def turma (self, turma):
        self.turma = turma