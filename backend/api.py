from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
import json

# port number for test server
PORT = 80


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path == "/":
                self.wfile.write(b"hello world")
        except:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(b"500 internal server error")

    def do_POST(self):
        try:
            if self.path == "/":
                self.wfile.write(b"hello world")
            #     length = int(self.headers.get("content-length"))
            #     request = json.loads(self.rfile.read(length))

            #     if request["text"] == "error":
            #         self.send_response(400)
            #         self.end_headers()
            #         self.wfile.write(b"400 bad request")

            #     elif request["text"] == "blank":
            #         self.send_response(200)
            #         self.send_header("Content-type", "application/json")
            #         self.end_headers()
            #         self.wfile.write(
            #             json.dumps(
            #                 {"predictions": [{"predictions": [], "sentiment": 0}]}
            #             ).encode("utf-8")
            #         )

            #     elif request["text"] == "mock":
            #         with open("mock-response.json", "r") as dummy:
            #             response = json.loads(dummy.read())
            #             self.send_response(200)
            #             self.send_header("Content-type", "application/json")
            #             self.end_headers()
            #             self.wfile.write(json.dumps(response).encode("utf-8"))

            #     else:
            #         with open("wayfair-response.json", "r") as dummy:
            #             response = json.loads(dummy.read())
            #             self.send_response(200)
            #             self.send_header("Content-type", "application/json")
            #             self.send_header("Access-Control-Allow-Origin", "*")
            #             self.send_header("Vary", "Accept-Encoding, Origin")
            #             self.end_headers()
            #             self.wfile.write(json.dumps(response).encode("utf-8"))

            # else:
            #     self.send_response(404)
            #     self.end_headers()
            #     self.wfile.write(b"404 not found")

        except:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(b"500 internal server error")

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "X-PINGOTHER, Content-Type")
        self.send_header("Access-Control-Max-Age", "86400")
        self.send_header("Vary", "Accept-Encoding, Origin")
        self.end_headers()


if __name__ == "__main__":
    print("Initializing server")
    httpd = HTTPServer(("0.0.0.0", PORT), RequestHandler)
    print("Wrapping SSL")
    # httpd.socket = ssl.wrap_socket(
    #     httpd.socket, keyfile=SSL_KEY, certfile=SSL_CERT, server_side=True
    # )
    print("Serving on port %d" % PORT)
    httpd.serve_forever()
