import cv2
import pyzbar.pyzbar as pyzbar
import qrcode


def leer_codigo_qr(imagen_path: str) -> str:
    # Cargar la imagen
    """
    Lee un código QR desde una imagen y devuelve los datos del código QR.

    Parámetros:
    imagen_path (str): Ruta de la imagen que contiene el código QR.

    Retorna:
    str: Los datos del código QR.
    """
    imagen = cv2.imread(imagen_path)

    # Decodificar los códigos QR en la imagen
    codigos = pyzbar.decode(imagen)

    # Extraer y devolver los datos de los códigos QR
    datos_codigos = codigos[0].data.decode("utf-8")
    return datos_codigos


def decode_xor_hex(hex_str: str, key: str) -> str:
    """
    Decodifica un string en hexadecimal XOR con una clave dada.

    Parámetros:
    hex_str (str): String en hexadecimal que contiene los datos a decodificar.
    key (str): Clave para XOR.

    Retorna:
    str: Los datos decodificados.
    """
    data = bytes.fromhex(hex_str)
    key_bytes = key.encode("utf-8")
    decoded = bytes([b ^ key_bytes[i % len(key_bytes)] for i, b in enumerate(data)])
    return decoded.decode("utf-8", errors="replace")


def encode_xor_to_hex(plain_text: str, key: str) -> str:
    """
    Codifica un string plano en hexadecimal XOR con una clave dada.

    Parámetros:
    plain_text (str): String plano que contiene los datos a codificar.
    key (str): Clave para XOR.

    Retorna:
    str: Los datos codificados en hexadecimal.
    """
    plain_bytes = plain_text.encode("utf-8")
    key_bytes = key.encode("utf-8")
    encoded = bytes(
        [b ^ key_bytes[i % len(key_bytes)] for i, b in enumerate(plain_bytes)]
    )
    #Guarda plain_text y encoded en un archivo de texto para debugging
    try:
        with open("codes/plain_text.txt", "a") as f:
            f.write(f"Plain text: {plain_text}\n")
            f.write(f"Encoded bytes: {encoded.hex()}\n")
    except Exception as e:
        print(e)

    return encoded.hex()


def genera_qr(codigo_hex: str, entrada: str) -> None:
    """
    Genera un código QR con la información dada y lo guarda en un archivo
    en la carpeta 'qrs' con el nombre 'generado_<último carácter del código
    hexadecimal>_<fecha y hora de entrada>.png'.

    Parámetros:
    codigo_hex (str): String en hexadecimal que contiene los datos a codificar.
    entrada (str): String que contiene la fecha y hora de entrada.

    Retorna:
    None
    """
    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=20,
            border=8,
        )
        # Genera una imagen que muestra los datos de enterada y el QR generado

        qr.add_data(codigo_hex)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save(f"qrs/generado_{codigo_hex[-5:]}.png")
        print(f"Código QR generado y guardado como '{codigo_hex[-4:]}.png'.")
        # muestra el código QR generado en pantalla
        img.show()

    except ImportError:
        print(
            "La librería 'qrcode' no está instalada. No se puede generar el código QR."
        )


if __name__ == "__main__":
    key = "uade123"
    qr_scan = "255154544d00075a50544a030201404155540b030a"
    print(decode_xor_hex(qr_scan, key))
    print(encode_xor_to_hex("P001|31/10/2025 12:50", key))
    genera_qr(encode_xor_to_hex("P001|31/10/2025 12:50", key), "P001|31/10/2025 12:50")
