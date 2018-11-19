import cherrypy


class Root(object):

    @cherrypy.expose
    def index(self):
        with open("html/index.html") as f:
            return f.read()
        return "Error"

    @cherrypy.expose
    def log_word(self, sbj_id, exp_type, duration, word, typeahead):
        with open("log_file", "a") as f:
            f.write(",".join(map(str, (sbj_id, exp_type, duration, word, typeahead))))


def main():
    cherrypy.config.update({"server.socket_port": 5555, "server.socket_host": "0.0.0.0"})
    cherrypy.quickstart(Root(), "/")


if __name__ == "__main__":
    main()