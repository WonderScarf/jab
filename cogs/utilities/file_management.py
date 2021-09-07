
# A class i made because I wanted to learn how to read and write stuff in Python.
class Txt:
    
    @staticmethod
    def read(path: str):
        data = []
        file = None

        try:
            file = open(path, "r")
            data = file.read().splitlines()
        except Exception as error:
            print(error)
            raise
        finally:
            if file is not None:
                file.close
        return data
    
    @staticmethod
    def write(path: str, data: str or list, overwrite:bool ):
        file = None
        
        try:

            if overwrite:
                writeMode = "w"
            else:
                writeMode = "a"
                
            file = open(path, writeMode)
            
            if file.writable:
                if(isinstance(data, list)):
                    data = '\n'.join(data)
                file.write(data + "\n")
        
        except Exception as error:
            print(error)
            raise
        
        finally:
            if file is not None:
                file.close
    
    
    