try:
    # 0 = falso, desligado, inativo | 1 = verdadeiro, ligado, ativo
    alarme_incendio_piso1 = True
    alarme_incendio_piso2 = True
    alarme_incendio_piso3 = False
    if alarme_incendio_piso1 == True or alarme_incendio_piso2 == True or alarme_incendio_piso3 == True:
        print("ALARME! CCOOOORREEEEE")

except Exception as e:
    print(str(e))