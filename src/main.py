# importar librerías para leer código QR
import os
from datetime import datetime
from functions import leer_codigo_qr, decode_xor_hex, encode_xor_to_hex, genera_qr


def test_imagenes(ruta: str = "qrs", comienza: str = "generado") -> None:
    try:
        for imagen in os.listdir(ruta):
            if not imagen.lower().endswith(
                (".png", ".jpg", ".jpeg")
            ) or not imagen.lower().startswith((comienza.lower())):
                continue
            ruta_imagen = os.path.join(ruta, imagen)
            datos = leer_codigo_qr(ruta_imagen)

            print(f"Datos del código {imagen}: {datos}")

            if len(datos) > 10:
                print("Datos decodificados de la pantalla:")
                print(decode_xor_hex(datos, key))
            else:
                print("Es QR corto")
            print()

    except Exception as e:
        print(e)
        print("Error al leer los códigos QR.")


def main(key: str) -> None:
    """
    Genera un código QR con la información de entrada dada y lo guarda en un archivo
    en la carpeta 'qrs' con el nombre 'generado_<último carácter del código hexadecimal>_<fecha y hora de entrada>.png'.

    Parámetros:
    key (str): Clave para XOR.

    Retorna:
    None
    """
    while True:
        aula = input("Ingrese el número de aula (por ejemplo, P001): ").upper()
        if len(aula) == 4 and aula[0] == "P" and aula[1:].isdigit():
            break
    fecha_hoy = input("Ingrese la fecha (DDMMYYYY) (enter para la actual): ")
    if not fecha_hoy:
        fecha_hoy = datetime.now().strftime("%d/%m/%Y")
        print(f"Fecha actual: {fecha_hoy}")
    fecha = fecha_hoy.replace("/", "")
    hora = input("Ingrese la hora de entrada (HHMM): ")
    entrada = f"{aula}|{fecha[:2]}/{fecha[2:4]}/{fecha[4:]} {hora[:2]}:{hora[2:]}"
    print(f"Entrada: {entrada}")
    codigo_hex = encode_xor_to_hex(entrada, key)
    print(f"Código hexadecimal XOR: {codigo_hex}")
    genera_qr(codigo_hex, entrada)


if __name__ == "__main__":
    key = "uade123"
    # main(key)
    test_imagenes(ruta="scans", comienza="Entrada")
