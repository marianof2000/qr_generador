# test con pytest para las funcionesd e functions.py
import pytest
from src.functions import leer_codigo_qr, decode_xor_hex, encode_xor_to_hex, genera_qr


def test_decode_xor_hex():
    # Caso de prueba 1
    hex_str = "255154544d00075a50544a030201404155540b030a"
    key = "uade123"
    expected_output = "P001|24/10/2025 11:19"
    assert decode_xor_hex(hex_str, key) == expected_output

    # Caso de prueba 2: Cadena vacía
    hex_str = ""
    expected_output = ""
    assert decode_xor_hex(hex_str, key) == expected_output

    # Caso de prueba 3: Clave más larga que los datos
    hex_str = "255154544d020b5a515c4a030201404155570b070b"
    key = "uade123"
    expected_output = "P001|08/08/2025 12:58"
    assert decode_xor_hex(hex_str, key) == expected_output

    # Caso de prueba 4: Clave corta
    """ hex_str = "48656c6c6f"
    key = "short"
    expected_output = "Hello"
    assert decode_xor_hex(hex_str, key) == expected_output """


def test_leer_codigo_qr():
    # Caso de prueba 1
    imagen_path = "scans/Entrada00.jpeg"
    expected_output = "2904F08F0"
    assert leer_codigo_qr(imagen_path) == expected_output

    # Caso de prueba 2
    imagen_path = "scans/Pantalla02.jpeg"
    expected_output = "255154544d020b5a515c4a030201404155570b070b"
    assert leer_codigo_qr(imagen_path) == expected_output

def test_encode_xor_to_hex():
    # Caso de prueba 1
    plain_text = "P001|24/10/2025 11:19"
    key = "uade123"
    expected_output = "255154544d00075a50544a030201404155540b030a"
    assert encode_xor_to_hex(plain_text, key) == expected_output

def test_genera_qr():
    # Caso de prueba 1
    codigo_hex = "255154544d00075a50544a030201404155540b030a"
    entrada = "P001|24/10/2025 11:19"
    try:
        genera_qr(codigo_hex, entrada)
    except Exception as e:
        pytest.fail(f"genera_qr raised an exception: {e}")

if __name__ == "__main__":
    pytest.main()
