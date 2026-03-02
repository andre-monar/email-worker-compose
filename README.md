# 📧 Email Worker Compose

**Projeto educacional completo** de simulação de envio de emails, desenvolvido durante o curso **Docker: Ferramenta essencial para desenvolvedores**. Apesar de ter fins didáticos, o projeto conta com **arquitetura pronta para produção**, incluindo preocupações reais com segurança, escalabilidade e boas práticas de desenvolvimento.

## 🏗️ Arquitetura
```text
🌐 Frontend (Nginx) → 🐍 App (Python) → 🗄️ Banco (PostgreSQL)
                          ↓
                        📦 Redes
                          ↓
                        ⚙️ Worker
```

## 🚀 Tecnologias

- **Frontend**: Nginx + HTML + Proxy Reverso
- **API**: Python + Bottle
- **Banco de Dados**: PostgreSQL 9.6 para armazenamento de mensagens
- **Fila**: Redis 3.2, com workers que simulam envio de e-mail
- **Containerização**: Docker + Docker Compose


## 🔒 Segurança
- **Proxy reverso** com Nginx (abstrai a API e evita exposição direta)
- **Redes Docker isoladas** (`banco`, `web`, `fila`) - cada serviço tem acesso apenas ao necessário
- **Variáveis de ambiente** para credenciais (senhas não ficam hardcoded)
- Containeres rodando com usuários não-root (quando possível)

## 📈 Escalabilidade
- **Arquitetura baseada em filas** (Redis)
- **Workers escaláveis horizontalmente**

## 🐳 Serviços (Docker)

| Serviço | Imagem | Porta | Descrição |
|---------|--------|-------|-----------|
| **db** | postgres:9.6 | 5432 | Banco de dados PostgreSQL |
| **queue** | redis:3.2 | 6379 | Fila Redis para mensagens |
| **app** | python:3.6-slim | 8080 | API em Bottle que recebe requisições |
| **worker** | custom (build) | - | Consumidor da fila (simula envio) |
| **frontend** | nginx:1.13 | 80 | Proxy reverso + arquivos estáticos |

## 🌐 Redes (Docker)

O projeto utiliza 3 redes Docker isoladas:
- banco: PostgreSQL + App
- web: Nginx + App
- fila: Redis + App + Worker

# Execução

## 📋 Pré-requisitos

- [Docker](https://docs.docker.com/get-started/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## 🔧 Instalação e Execução

1. **Clone o repositório**
```bash
git clone https://github.com/seu-usuario/email-worker-compose.git
cd email-worker-compose
```

2. **Inicie os containers**
```bash
docker-compose up -d
```
Para escalar os workers (exemplo com 3), use:
```bash
docker-compose up -d --scale worker=3 
```

3. **Verifique o status**
```bash
docker-compose ps
```

4. **Acesse a aplicação e teste o envio**
- http://localhost
- Envie o formulário

5. **Verifique os logs dos workers**
```bash
docker-compose logs -f -t worker
```

6. **Verifique o banco de dados**
```bash
docker-compose exec db psql -U postgres -d email_sender -c 'select * from emails'
```

## 🛑 Comandos úteis (Docker)
| Comando | Descrição |
|---------|-----------|
| `docker-compose ps` | Lista status dos containers |
| `docker-compose logs -f [serviço]` | Acompanha logs de um serviço |
| `docker-compose restart [serviço]` | Reinicia um serviço |
| `docker-compose down` | Para e remove containers |
| `docker-compose down -v` | Remove containers e volumes (apaga dados) |
| `docker-compose up --build` | Reconstrói imagens antes de subir |

## 🔧 Variáveis de Ambiente (Personalização opcional)

| Serviço | Variável | Padrão | Descrição |
|---------|----------|--------|-----------|
| **app** | `DB_HOST` | `db` | Host do PostgreSQL |
| | `DB_USER` | `postgres` | Usuário do banco |
| | `DB_PASSWORD` | `postgres` | Senha do banco |
| | `DB_NAME` | `sender` | Nome do banco |
| | `REDIS_HOST` | `queue` | Host do Redis |
| **worker** | `REDIS_HOST` | `queue` | Host do Redis |

## 👨‍🏫 Créditos
Este projeto foi desenvolvido durante o curso:
[**Docker: Ferramenta essencial para desenvolvedores**](https://www.udemy.com/course/curso-docker/?srsltid=AfmBOopTgiVSa27rTnBCj1dM9PIxE9oHg2VBPCT4_iBWUlCEFxf0uUNq) ministrado por [Leonardo Moura Leitão](https://github.com/leonardomleitao) e Juracy Filho.

## 📄 Licença
Este projeto é para fins educacionais. Sinta-se à vontade para estudar, modificar e compartilhar.
