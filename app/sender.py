from bottle import route, run, request
import sys
import time

print("🚀 Iniciando aplicação Bottle...", file=sys.stderr)

@route('/', method='POST')
def send():
    assunto = request.forms.get('assunto')
    mensagem = request.forms.get('mensagem')
    print(f"📧 Recebido: assunto={assunto}, mensagem={mensagem}", file=sys.stderr)
    return 'Mensagem enfileirada! Assunto: {}; Mensagem: {}'.format(
        assunto, mensagem
    )

if __name__ == '__main__':
    print("🔥 Servidor deveria rodar em http://0.0.0.0:8080", file=sys.stderr)
    # TESTE: Forçar um loop infinito se o run não estiver funcionando
    try:
        run(host='0.0.0.0', port=8080, debug=True)
    except Exception as e:
        print(f"💥 ERRO: {e}", file=sys.stderr)
        # Mantém o container vivo pra debug
        while True:
            time.sleep(10)
            print("⏱️ Container ainda vivo...", file=sys.stderr)