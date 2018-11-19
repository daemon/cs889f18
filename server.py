import cherrypy


class Root(object):

    @cherrypy.expose
    def index(self, **kwargs):
        with open("html/index.html") as f:
            content = f.read()
        if "word" in kwargs:
            sbj_id = kwargs["sbj_id"]
            exp_type = kwargs["exp_type"]
            duration = kwargs["duration"]
            word = kwargs["word"]
            typeahead = kwargs["typeahead"]
            with open("{}_{}_log.csv".format(exp_type, sbj_id), "a") as f:
                f.write(",".join(map(str, (sbj_id, exp_type, duration, word, typeahead))) + "\n")
        return content


def main():
    cherrypy.config.update({"server.socket_port": 5555, "server.socket_host": "0.0.0.0"})
    cherrypy.quickstart(Root(), "/")


if __name__ == "__main__":
    main()