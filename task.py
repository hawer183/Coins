Values = [1, 2, 5, 10, 20, 50, 100, 200]
Pieces = [160, 138, 172, 146, 38, 25, 180, 107]
Price = 7607

def main():
    #do some magic, initialize arrays
    jsonValues = Values
    jsonPieces = Pieces
    jsonPrice = Price
    
    try:
        lst = GetCoins(jsonValues, jsonPieces, jsonPrice)
        print str(lst) + " Sum: " + str(Sum(lst, jsonValues))
    except Exception as e:
        print(e)
    
def GetCoins(values, pieces, price):
    lst = GetWithMostCoins(price, pieces, values)
    difference = Sum(lst, values) - price
    if (difference == 0): return lst
    
    pieces = Subtract(pieces, lst)
    tmp = [0] * len(pieces)
    
    for _ in range(0, sum(pieces)):
        tmp = GetWithLeastCoins(difference, lst, values)
        difference = Sum(tmp, values) - difference
        if (difference == 0): break
        result = AddNextCoin(lst, pieces)
        lst = result['pieces']
        pieces = result['availablePieces']
        
    if (difference != 0):
        raise Exception("Not enough coins or some other shit happened.")
    
    return Subtract(lst, tmp)
    

def GetWithMostCoins(amount, pieces, values):
    tmp = [0] * len(pieces)

    for i in range(len(tmp)):
        for _ in range(0, pieces[i]):
            if (amount <= 0 or tmp[i] >= pieces[i]): break
            amount -= values[i]
            tmp[i] += 1

    return tmp

def GetWithLeastCoins(amount, pieces, values):
    tmp = [0] * len(pieces)

    for i in reversed(range(len(tmp))):
        for _ in range(0, pieces[i]):
            if (amount <= 0 or tmp[i] >= pieces[i] or (amount / values[i]) < 1): break
            amount -= values[i]
            tmp[i] += 1

    return tmp

def AddNextCoin(pieces, availablePieces):
    for i in range(0, len(availablePieces)):
        if (availablePieces[i] > 0):
            availablePieces[i] -= 1;
            pieces[i] += 1;
            return {'pieces':pieces, 'availablePieces':availablePieces}

def Sum(lst, values):
    sumq = 0

    for i in range(len(lst)):
        sumq += lst[i]*values[i]

    return sumq

def Subtract(a, b):
    for i in range(len(a)):
        a[i] -= b[i]

    return a
     
if __name__ == "__main__": main()