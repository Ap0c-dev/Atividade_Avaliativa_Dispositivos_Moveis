class Util:
    @staticmethod
    
    def validaData(data):
        dt = data.split("/")
    
        if len(dt) == 3:
            return True
        else:
            return False