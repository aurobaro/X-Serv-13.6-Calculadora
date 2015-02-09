#!/usr/bin/python
#-*-coding:utf-8-*-

import sys

#print 'Number of arguments:', len(sys.argv), 'arguments.'
#print 'Argument List:', str(sys.argv)

operacion = str(sys.argv[1])
operando1 = int(sys.argv[2])
operando2 = int(sys.argv[3])

	
try:
	if __name__ == "__main__":
		if operacion == "sumar":
			suma = operando1+operando2
			print "La suma es", suma, "\n"
        
		elif operacion == "restar":
			resta = operando1-operando2
			print "La resta es", resta, "\n"

		elif operacion == "multiplicar":
			mult = operando1*operando2
			print "La multiplicación es", mult, "\n"

		elif operacion == "dividir":
			div = operando1/operando2
			print "La división es", div, "\n"

except:
	print "Error: [python calculadora.py función operando1 operando2]"
	print "función --> sumar restar multiplicar dividir" 


        
        
            

    

    
    
