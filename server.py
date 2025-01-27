from http.server import HTTPServer, SimpleHTTPRequestHandler
import webbrowser
import os
import socket

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    try:
        server_address = ('', port)
        httpd = server_class(server_address, handler_class)
        print(f'Starting server on port {port}...')
        webbrowser.open(f'http://localhost:{port}')
        httpd.serve_forever()
    except PermissionError:
        print(f"Error: Permission denied for port {port}. Try running with administrator privileges or use a port number above 1024.")
    except socket.error as e:
        print(f"Error: Could not start server. Port {port} might be in use.")
        print(f"Error details: {e}")

if __name__ == '__main__':
    run()
