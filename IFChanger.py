import subprocess, os, netifaces

INFO = "[i] Creado por __Rodion__. (github.com/RodionButEncapsulated)\n"

LOGO = '''M""M MM""""""""`M MM'""""'YMM dP                                                    
M  M MM  mmmmmmmM M' .mmm. `M 88                                                    
M  M M'      MMMM M  MMMMMooM 88d888b. .d8888b. 88d888b. .d8888b. .d8888b. 88d888b. 
M  M MM  MMMMMMMM M  MMMMMMMM 88'  `88 88'  `88 88'  `88 88'  `88 88ooood8 88'  `88 
M  M MM  MMMMMMMM M. `MMM' .M 88    88 88.  .88 88    88 88.  .88 88.  ... 88       
M  M MM  MMMMMMMM MM.     .dM dP    dP `88888P8 dP    dP `8888P88 `88888P' dP       
MMMM MMMMMMMMMMMM MMMMMMMMMMM                                 .88                   
                                                          d8888P                    '''

menu1 = """\tINDIQUE LA INTERFAZ A CAMBIAR\n"""
menu2 = """\tINDIQUE EL MODO A CAMBIAR\n"""


def clean_screen(): # Función para limpiar pantalla.
    os.system("clear")

def mode_monitor(interface): # Función para activar el modo monitor en una interfaz de red indicada.
    subprocess.call(f"sudo ifconfig {interface} down", shell=True) # Apagar la interfaz.
    subprocess.call("sudo airmon-ng check kill", shell=True) # Finalizar servicios que pueden generar conflicto.
    subprocess.call(f"sudo airmon-ng start {interface}", shell=True) # Encender el modo monitor.
    subprocess.call(f"sudo ifconfig {interface} up", shell=True) # Encender la interfaz.
    subprocess.call("sudo service NetworkManager start", shell=True)  # Reiniciar servicios cerrados.
    subprocess.call("sudo service wpa_supplicant start", shell=True)  # Reiniciar servicios cerrados.

def mode_managed(interface): # Función para activar el modo managed en una interfaz de red indicada.
    subprocess.call(f"sudo ifconfig {interface} down", shell=True) # Apagar la interfaz.
    subprocess.call("sudo airmon-ng check kill", shell=True) # Finalizar servicios que pueden generar conflicto. 
    subprocess.call(f"sudo airmon-ng stop {interface}", shell=True) # Apagar el modo monitor.
    subprocess.call(f"sudo ifconfig {interface} up", shell=True) # Encender la interfaz.
    subprocess.call("sudo service NetworkManager start", shell=True) # Reiniciar servicios cerrados.
    subprocess.call("sudo service wpa_supplicant start", shell=True) # Reiniciar servicios cerrados.

def check_interfaces(): # Revisa las interfaces de red disponibles en el equipo.
    interfaces = netifaces.interfaces()
    return interfaces

def select_interface(): # Muestra las interfaces de red en orden.
    interfaces = check_interfaces() # Obtener las interfaces disponibles.
    print(menu1)
    for interface in interfaces:
        print(f"[{interfaces.index(interface)}] {interface}") # Mostrar las interfaces disponibles.
    choice = int(input("\n[?] Elija una opción: "))
    
    return interfaces[choice] # Devuelve la interfaz de red selecionada.

def select_mode(interface): # Muestra los modos a los que se puede cambiar la interfaz de red ingresada como argumento.
    print(menu2)
    print("[0] Mode Monitor\n[1] Mode Managed")
    choice = input("\n[?] Elija una opción: ") 
    if choice == "0":
        mode_monitor(interface) # Sí la opción es 0 ejecuta el modo monitor sobre la interfaz seleccionada anteriormente.
    elif choice == "1":
        mode_managed(interface) # Sí la opción es 1 ejecuta el modo managed sobre la interfaz seleccionada anteriormente.
    else:
        print("[!] La opción indicada no es correcta.") 


def main(): # Función principal.
    clean_screen() # Limpiar pantalla.
    print(LOGO) # Imprime el ASCII art con el nombre del programa.
    print(INFO) # Imprime la información de GitHub.
    interface = select_interface() # Obtener la interfaz a cambiar.
    clean_screen() # Limpiar pantalla.
    select_mode(interface) # Ejecutar el cambio sobre la interfaz indicada.



if __name__ == "__main__": # Inicializador.
    main()
