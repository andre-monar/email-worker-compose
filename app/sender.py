import psycopg2
from bottle import Bottle, request
import redis
import json

class Sender(Bottle):
    def __init__(self):
        super().__init__()
        self.route('/', method='POST', callback=self.send)
        self.fila = redis.StrictRedis(host='queue', port=6379, db=0)
        DSN = 'dbname=email_sender user=postgres password=postgres host=db'
        self.conn = psycopg2.connect(DSN)

    def register_message(self, assunto, mensagem):
        c = self.conn.cursor()
        SQL = 'INSERT INTO emails (assunto, mensagem) VALUES (%s, %s)'
        c.execute(SQL, (assunto, mensagem))
        self.conn.commit()
        c.close()

        msg = {'assunto': assunto, 'mensagem': mensagem}
        self.fila.rpush('sender', json.dumps(msg))
        print('Mensagem registrada no BD.')

    def send(self):
        assunto = request.forms.get('assunto')
        mensagem = request.forms.get('mensagem')

        self.register_message(assunto, mensagem)

        return 'Mensagem enfileirada! Assunto: {}; Mensagem: {}'.format(
            assunto, mensagem
        )

if __name__ == '__main__':
    sender = Sender()
    sender.run(host='0.0.0.0', port=8080, debug=True)