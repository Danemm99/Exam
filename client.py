import socket
import numpy as np
import time


def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 12345))
    n, m, l = np.random.randint(1000, 2000, size=3)
    matrix_a = np.random.randint(1, 10, size=(n, m))
    matrix_b = np.random.randint(1, 10, size=(m, l))

    print(f"[CLIENT1] Generated matrices:")
    print("Matrix A:")
    print(matrix_a)
    print("Matrix B:")
    print(matrix_b)

    print("[CLIENT1] Sending matrix sizes to server")
    client_socket.send(f"{n},{m},{l}".encode())

    print("[CLIENT1] Sending matrices to server")
    client_socket.send(matrix_a.tobytes())
    client_socket.send(matrix_b.tobytes())

    result_data = b""
    while True:
        chunk = client_socket.recv(4096)
        if not chunk:
            time.sleep(0.1)
            break
        result_data += chunk

    if len(result_data) == 0:
        print("[CLIENT1] Server closed the connection prematurely.")
    else:
        result_matrix = np.frombuffer(result_data, dtype=int).reshape(n, l)

        print("[CLIENT1] Received result matrix:")
        print(result_matrix)

    client_socket.close()
    print("[CLIENT1] Connection closed")


if __name__ == "__main__":
    start_client()


