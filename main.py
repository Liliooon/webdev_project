from flask import Flask

from jsonrpc.backend.flask import api

app = Flask(__name__)
app.add_url_rule('/', 'api', api.as_view(), methods=['POST'])

@api.dispatcher.add_method
def words_counter(text):
    return len(text.split())

if __name__ == '__main__':
	app.run(debug=True)