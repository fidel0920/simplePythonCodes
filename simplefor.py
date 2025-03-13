def jam():
        lista=[]
        for valor in range(10):
            valor = int(input("Ingrese el valor: "));
            lista.append(valor);
            juan = sum(lista);
            orden = lista.sort();
        print("La lista quedo así: ",lista);
        print("La suma de todos los numeros es: ",juan);
jam();
