a = [1, 2, 3, 4, 5, 6]

b = a[1:3:2]
print(b)

lenguajes = [ " Python " , " Java " , " Kotlin " ,
            " Python2 " , " Python3 " , " python -dev " ,
            " Ruby " , " C " , " python " , " php " , "Perl "
            " PyThoN " , " pytHON " , " pYTHON " ,
            " Pyth@n " ]
resultado = filter ( lambda x : x . upper () .
startswith ( " PYTHON " ) ,
lenguajes )


for i in resultado :
    print ( i )