def characterCounter(string: str):
    return len(string)
        
def calculateTokenCount(num_of_characters: int):
    tokenCount = num_of_characters // 4
    if num_of_characters % 4 > 0:
        tokenCount +=1
    return tokenCount

def calculateTokenPriceInput(tokenCount:int):
   return tokenCount/100000

def calculateTokenPriceOutput(tokenCount:int):
   return tokenCount/300000


