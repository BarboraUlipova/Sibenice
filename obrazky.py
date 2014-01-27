# pokud chci udělat řetězec, který je na víc řádků, nemůžu dělat nový řádek enter. Musím udělat buď trojité uvozovky nebo \n 
# r je tam proto, že když dám zpětné lomítko, tak to interpretuje jako cosi jiného. r z toho udělá raw
obrazky=[]

seznam_obrazku = [
    r"""
        0
        |
       /|\
        |
       / \
      """,
    r"""
        0
        |
       /|\
        |
       / 
      """,
    r"""
        0
        |
       /|\
        |
       
      """,
    r"""
        0
        |
       /|
        |
       
      """,
    r"""
        0
        |
        |
        |
       
      """,
    r"""
        0
        
        
        
       
      """
    
]

