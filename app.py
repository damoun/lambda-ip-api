from chalice import Chalice


app = Chalice(app_name='Chalice-IP-API')


@app.route('/')
def retrieve_ip():
    return dict(ip=app.current_request.context['source-ip'])
