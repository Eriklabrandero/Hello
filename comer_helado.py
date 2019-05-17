
apetece_helado_input = input("¿te apetece un helado? (Si / No):").upper()

if apetece_helado_input == "SI":
    apetece_helado_input = True
elif apetece_helado_input == "NO":
    apetece_helado_input = False
else:
    print("Te dije que digas si o no, no se que has dicho pero cuento como que no")
    apetece_helado_input = False

tiene_dinero_input = input("¿Tienes dinero? (Si / No):").upper()
esta_el_senor_helados_input = input("¿Esta el señor de los helados? (Si / No):").upper()
esta_tu_tia_input = input("¿Estás con tu tía? (Si / No):").upper()

apetece_helado = apetece_helado_input == "SI"
puede_permitirselo = tiene_dinero_input == "SI" or esta_tu_tia_input == "SI"
esta_el_senor_helados = esta_el_senor_helados_input == "SI"

if apetece_helado and puede_permitirselo and esta_el_senor_helados:
    print("Pues comete un helado")

else:
    print("Pues nada")
