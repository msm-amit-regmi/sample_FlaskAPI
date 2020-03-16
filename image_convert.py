import base64


def encode(img_path: str) -> str:
    print(img_path)
    with open(img_path, 'rb') as f:
        enc = from_byte_to_str(f.read())
        return enc


def from_byte_to_str(b: bytes) -> str:
    return base64.b64encode(b).decode('utf-8')


def decode(img_str: str):
    dec = base64.b64decode(img_str.encode())
    return dec
