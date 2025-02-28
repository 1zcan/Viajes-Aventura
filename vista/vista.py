from controlador.usuarios_controlador import autenticar_usuario, registrar_usuario
from controlador.reservas_controlador import (
    agregar_reserva,
    mostrar_reservas,
    eliminar_reserva,
)
from controlador.paquetes_controlador import (
    agregar_paquete,
    mostrar_paquetes,
    eliminar_paquete,
    modificar_paquete,
    mostrar_paquetes_disponibles,
)
from controlador.destinos_controlador import (
    agregar_destino,
    mostrar_destinos,
    eliminar_destino,
    modificar_destino,
)
from pwinput import pwinput


def inicio():
    exit = False
    while not exit:
        print("*****************************************************⋆⭒˚｡⋆✈︎")
        print("************  Bienvenido a Viajes Aventura  ***************")
        print("***********************************************************")
        print("")
        print("1. Iniciar sesión")
        print("2. Registrarse")
        print("s. Salir")
        print("")

        opcion = input()

        if opcion == "1":
            email = input("ingrese su email: ")
            print("")
            contraseña = pwinput("Ingrese su contraseña: ")
            print("")
            usuario = autenticar_usuario(email, contraseña)

            if usuario:
                print(f"Bienvenido, {usuario.nombre}")
                print("")
                print("Seleccione una opción:")
                print("")
                print("1. Vista destinos")
                print("2. Vista paquetes")
                print("3. Vista reservas")
                print("s. Salir")
                print("")

                op = input()

                if op == "1":
                    print("Destinos:")
                    print("")
                    print("1. Ver destinos")
                    print("2. Agregar destino")
                    print("3. Eliminar destino")
                    print("4. Modificar destino")
                    print("s. Salir")

                    print("")
                    op = input()

                    if op == "1":
                        mostrar_destinos()

                    elif op == "2":
                        print("Ingrese el nombre del destino:")
                        nombre = input()
                        print("Ingrese la descripción del destino:")
                        descripcion = input()
                        print("Ingrese las actividades del destino:")
                        actividades = input()
                        print("Ingrese el costo del destino:")
                        costo = input()
                        agregar_destino(nombre, descripcion, actividades, costo)

                    elif op == "3":
                        nombre = input("Ingrese el nombre del destino a eliminar: ")
                        eliminar_destino(nombre)

                    elif op == "4":
                        print("Ingrese el nombre del destino a modificar:")
                        nombre = input()
                        print("Ingrese el nuevo nombre del destino:")
                        nuevo_nombre = input()
                        print("Ingrese la nueva descripción del destino:")
                        nueva_descripcion = input()
                        print("Ingrese las nuevas actividades del destino:")
                        nuevas_actividades = input()
                        print("Ingrese el nuevo costo del destino:")
                        nuevo_costo = input()
                        modificar_destino(
                            nombre,
                            nuevo_nombre,
                            nueva_descripcion,
                            nuevas_actividades,
                            nuevo_costo,
                        )

                elif op == "2":
                    print("Paquetes:")
                    print("")
                    print("1. Agregar paquete")
                    print("2. Ver paquetes disponibles ")
                    print("3. Mostar paquetes con destinos")
                    print("4. Modificar paquete")
                    print("5. Eliminar paquete")
                    print("s. Salir")
                    print("")
                    op = input()

                    if op == "1":
                        print("Ingrese el nombre del paquete:")
                        nombre = input()
                        print("Ingrese la descripción del paquete:")
                        descripcion = input()
                        print("Ingrese el id de los destinos separados por una ',':")
                        destinos = input()
                        print("Ingrese la fecha de inicio del paquete (yyyy-mm-dd):")
                        fecha_inicio = input()
                        print("Ingrese la fecha de fin del paquete(yyyy-mm-dd):")
                        fecha_fin = input()
                        print("Ingrese el precio total del paquete:")
                        precio_total = input()
                        agregar_paquete(
                            nombre,
                            descripcion,
                            destinos,
                            fecha_inicio,
                            fecha_fin,
                            precio_total,
                        )
                        
                    elif op == "2":
                        mostrar_paquetes_disponibles()
                    elif op == "3":
                        mostrar_paquetes()
                    elif op == "4":
                        print("Ingrese el id del paquete a modificar:")
                        paquete_id = input()
                        print("Ingrese el nuevo nombre del paquete:")
                        nuevo_nombre = input()
                        print("Ingrese la nueva descripción del paquete:")
                        nueva_descripcion = input()
                        print("Ingrese los nuevos destinos del paquete separados por una ',':")
                        nuevos_destinos = input()
                        print("Ingrese la nueva fecha de inicio del paquete (yyyy-mm-dd):")
                        nueva_fecha_inicio = input()
                        print("Ingrese la nueva fecha de fin del paquete (yyyy-mm-dd):")
                        nueva_fecha_fin = input()
                        print("Ingrese el nuevo precio total del paquete:")
                        nuevo_precio_total = input()
                        modificar_paquete(
                            paquete_id,
                            nuevo_nombre,
                            nueva_descripcion,
                            nuevos_destinos,
                            nueva_fecha_inicio,
                            nueva_fecha_fin,
                            nuevo_precio_total,
                            )
                        
                    elif op == "5":
                        id = input("Ingrese el id del paquete a eliminar: ")
                        eliminar_paquete(id)
                elif op == "3":
                    print("Reservas:")
                    print("")
                    print("1. Ver reservas")
                    print("2. Agregar reserva")
                    print("3. Eliminar reserva")
                    print("s. Salir")
                    print("")
                    op = input()

                    if op == "1":
                        mostrar_reservas()
                    elif op == "2":
                        print("Ingrese el id del paquete:")
                        paquete_id = input()
                        print("Ingrese la fecha de la reserva:")
                        fecha_reserva = input()
                        agregar_reserva(usuario.id, paquete_id, fecha_reserva)
                    elif op == "3":
                        eliminar_reserva()

            else:
                print("Usuario o contraseña incorrectos")

        elif opcion == "2":
            print("Ingrese su nombre:")
            nombre = input()
            print("Ingrese su email:")
            email = input()
            print("Ingrese su contraseña:")
            contraseña = pwinput()
            registrar_usuario(nombre, email, contraseña)
            print("Usuario registrado exitosamente!")

        elif opcion.lower() == "s":
            print("""⠀⠀⠀⣖⠲⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠉⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠸⡆⠹⡀⣠⢤⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡏⠀⡧⢤⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⡧⢄⣹⣅⣜⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠁⠀⢹⠚⠃⠀⠀⠀⠀⠀
⠀⣀⠴⢒⣉⡹⣶⣤⣀⡉⠉⠒⠒⠒⠤⠤⣀⣀⣀⠇⠀⠀⢸⠠⣄⠀⠀⠀⠀⠀
⠀⠈⠉⠁⠀⠀⠀⠉⠒⠯⣟⣲⠦⣤⣀⡀⠀⠀⠈⠉⠉⠉⠛⠒⠻⢥⣀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⣲⡬⠭⠿⢷⣦⣤⢄⣀⠀⠀⠚⠛⠛⠓⢦⡀
⠀⠀⠀⠀⠀⠀⠀⢀⣀⠤⠴⠚⠉⠁⠀⠀⠀⠀⣀⣉⡽⣕⣯⡉⠉⠉⠑⢒⣒⡾
⠀⠀⣀⡠⠴⠒⠉⠉⠀⢀⣀⣀⠤⡤⢶⣶⣋⠉⠉⠀⠀⠀⠈⠉⠉⠉⠉⠉⠁⠀
⣖⣉⣁⣠⠤⠶⡶⡶⢍⡉⠀⠀⠀⠙⠒⠯⠜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠁⠀⠀⠀⠀⠑⢦⣯⠇""")
            exit = True
