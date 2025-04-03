import socket
import ssl
import threading

server_address = ('localhost', 12345)

def receive_data(ssl_socket):
    try:
        while True:
            data = ssl_socket.recv(1024)
            if not data:
                break
            print("Nhận:", data.decode('utf-8'))
    except Exception as e:
        print("Lỗi khi nhận dữ liệu:", e)
    finally:
        ssl_socket.close()
        print("Ngắt kết nối từ máy chủ.")

# Create a client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Configure SSL context
context = ssl.SSLContext(ssl.PROTOCOL_TLS)
context.verify_mode = ssl.CERT_NONE  # Disable certificate verification (not recommended for production)
context.check_hostname = False

try:
    # Wrap the socket with SSL
    ssl_socket = context.wrap_socket(client_socket, server_hostname='localhost')
    ssl_socket.connect(server_address)

    # Start a thread to handle receiving data
    receive_thread = threading.Thread(target=receive_data, args=(ssl_socket,))
    receive_thread.daemon = True  # Ensure the thread exits when the main program exits
    receive_thread.start()

    # Main loop to send messages
    while True:
        try:
            message = input("Nhập tin nhắn: ")
            if message.strip().lower() == "exit":
                print("Đang ngắt kết nối...")
                break
            ssl_socket.send(message.encode('utf-8'))
        except Exception as e:
            print("Lỗi khi gửi tin nhắn:", e)
            break
except KeyboardInterrupt:
    print("\nNgười dùng đã ngắt kết nối.")
except Exception as e:
    print("Lỗi kết nối:", e)
finally:
    ssl_socket.close()
    print("Đã đóng kết nối.")