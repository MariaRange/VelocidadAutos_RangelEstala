x = 130
y = 60
media = x/y

ciclo = True
while ciclo:
    try:    
        vel = int(input('Ingrese la velocidad del auto (km/hr)\n'))
        int(vel)
        num = True
        
        año = True
        print(año)
        
        if vel == 0:
            print('Nada veloz')
        elif vel in range(1,40):
            print('Poco veloz')
        elif vel in range(41,80):
            print('Velocidad media')
        elif vel in range(81,105):
            print('Veloz')
        elif vel in range(106, 130):
            print('Muy veloz')

        if vel < y:
            if vel < y:
                vel = y
                print('Se guardo el nuevo limite inferior')
                ciclo = False
            else:
                print(f'La velocidad {vel} es % veloz')
                ciclo = False

        elif vel > x:
            vel = x
            print('Se guardo el nuevo limite superior')
            ciclo = False

        else:
            print(f"La velocidad {vel}km/hr es % veloz")    
            ciclo = False
        
            
            
    except ValueError:
        num = False
        print("Numero invalido")