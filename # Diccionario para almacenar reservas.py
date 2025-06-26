reservas = {}

def reservar_zapatillas():
    print("\n-- Reservar Zapatillas --")
    if len(reservas) >= 20:
        print("No hay más stock disponible para reservas.")
        return
    nombre = input("Nombre del comprador: ")
    if nombre in reservas:
        print("Este comprador ya tiene una reserva registrada.")
        return
    clave = input("Digite la palabra secreta para confirmar la reserva: ")
    if clave != "EstoyEnListaDeReserva":
        print("Palabra secreta incorrecta. No se pudo realizar la reserva.")
        return
    reservas[nombre] = 1
    print(f"Reserva realizada exitosamente para {nombre}.")

def buscar_reservas():
    print("\n-- Buscar Zapatillas Reservadas --")
    nombre = input("Nombre del comprador a buscar: ")
    if nombre in reservas:
        pares = reservas[nombre]
        tipo = "VIP" if pares == 2 else "estándar"
        print(f"Reserva encontrada: {nombre} - {pares} par(es) ({tipo}).")
        opcion = input("¿Desea pagar adicional para VIP y reservar 2 pares? (s/n): ").lower()
        if opcion == "s":
            reservas[nombre] = 2
            print(f"Reserva actualizada a VIP. Ahora {nombre} tiene 2 pares reservados.")
        else:
            print("Manteniendo reserva actual.")
    else:
        print("No se encontró ninguna reserva con ese nombre.")

def cancelar_reserva():
    print("\n-- Cancelar Reserva --")
    nombre = input("Nombre del comprador cuya reserva desea cancelar: ")
    if nombre in reservas:
        del reservas[nombre]
        print(f"La reserva de {nombre} ha sido cancelada.")
    else:
        print("No se encontró ninguna reserva con ese nombre.")

def main():
    while True:
        print("""
TOTEM AUTOATENCIÓN RESERVA STRIKE

1.- Reservar zapatillas
2.- Buscar zapatillas reservadas
3.- Cancelar reserva de zapatillas
4.- Salir
""")
        opcion = input("Seleccione una opción (1-4): ")
        if opcion == "1":
            reservar_zapatillas()
        elif opcion == "2":
            buscar_reservas()
        elif opcion == "3":
            cancelar_reserva()
        elif opcion == "4":
            print("Programa terminado...")
            break
        else:
            print("Debe ingresar una opción válida!!")

main()
