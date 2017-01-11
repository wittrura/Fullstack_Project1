#
import SimpleHTTPServer
import SocketServer

def start_server():
    PORT = 8080

    Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

    httpd = SocketServer.TCPServer(("", PORT), Handler)
    print "serving at port", PORT
    httpd.serve_forever()
    #webbrowser.open('localhost://', PORT)

start_server()
