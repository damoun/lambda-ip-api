from bottle import Bottle, request


APP = Bottle()


@APP.route('/', ['GET'])
def retrieve_ip():
    return dict(ip=request.remote_addr)


if __name__ == '__main__':
    APP.run(port=3000, debug=True)
