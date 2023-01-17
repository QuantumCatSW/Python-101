import socket
import random

HOST = ''
PORT = 50007

# 첫 번째 매개변수 socket.AF_INET은 IPv4 인터넷 프로토콜을, 
# 두 번째 매개변수 socket.SOCK_STREAM은 소켓 유형이 문자열 등을 주고받는 스트림 방식임을 의미
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print('서버가 시작되었습니다.')
    conn, addr = s.accept()
    with conn:
        answer = random.randint(1, 9)
        print(f'클라이언트가 접속했습니다:{addr}, 정답은 {answer} 입니다.')
        while True:
            data = conn.recv(1024).decode('utf-8')
            print(f'데이터:{data}')

            try:
                n = int(data)
            except ValueError:
                conn.sendall(f'입력값이 올바르지 않습니다:{data}'.encode('utf-8'))
                continue

            if n == 0:
                conn.sendall(f"종료".encode('utf-8'))
                break
            if n > answer:
                conn.sendall("너무 높아요".encode('utf-8'))
            elif n < answer:
                conn.sendall("너무 낮아요".encode('utf-8'))
            else:
                conn.sendall("정답".encode('utf-8'))
                break
