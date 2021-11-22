class Turma:
    __slots__= (
        '_id',
        '_nome',
        '_turno'
    )

    def __init__(self, id=None, nome="", turno=""):
        self.id = id
        self.nome = nome
        self.turno = turno

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        self._id = id

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome
    
    @property
    def turno(self):
        return self._turno

    @turno.setter
    def turno(self,nome):
        self._turno = turno
        