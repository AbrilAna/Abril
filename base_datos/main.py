from consultar_bd import pregunta_ia_con_datos

if __name__ == "__main__":
    pregunta = input("¿Qué querés saber? ")
    respuesta = pregunta_ia_con_datos(pregunta)
    print("\n🤖 IA:", respuesta)
