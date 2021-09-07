
class ListTools:

    @staticmethod
    def listType(array: list):
        'Checks if all items in a list are the same type, if so it returns the type if not it returns a False boolean.'
        
        firstType = type(array[0])
            
        if all((type(x) is firstType) for x in array): 
            return firstType  
        else:    
            return False

        
          
