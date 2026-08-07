import http.server
import socketserver
import os

PORT = 8000
DIRECTORY = "site"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

if __name__ == "__main__":
    # Asegurar que estamos en el directorio correcto
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Crear y ejecutar el servidor web
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Servidor web iniciado en el puerto {PORT}")
        print(f"Puedes acceder al sitio en http://localhost:{PORT}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServidor detenido por el usuario.")
