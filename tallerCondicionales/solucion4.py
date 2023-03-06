# 4. En el Sena un grupo de estudiantes pretende estudiar ADSI, para ello se
"""
les pregunta la cantidad de interesados en el programa. Si la cantidad
supera los 25 se abre el curso, de lo contrario no. Responder al grupo
"""
cantidad= int( input( "¿Cuantos quieren estudiar en adsi?:\n" ) )

if cantidad<25:
    print("se abre nuevo curso de adsi.")
else:
    print("No abrá nuevo grupo de adsi.")
    
