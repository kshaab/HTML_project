from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    """
    Специальный класс, который отвечает за
    обработку входящих запросов от клиентов
    """

    def do_GET(self) -> None:
        """Метод для обработки входящих GET-запросов"""
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        with open("src/contacts.html", "r", encoding="utf-8") as file:
            html_content = file.read()

        self.wfile.write(bytes(html_content, "utf-8"))

    def do_POST(self):
        content_length = int(self.headers.get("Content-Length", 0))
        post_data = self.rfile.read(content_length)
        post_data_str = post_data.decode("utf-8")
        post_data_dict = urllib.parse.parse_qs(post_data_str)

        print("Получен POST-запрос:")
        print("Headers:", self.headers)
        print("Data:", post_data_dict)

        self.send_response(200)
        self.end_headers()
        self.wfile.write("Данные получены".encode("utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
