# Django TesteFull Frontend

Frontend em Django com as mesmas funcionalidades do Angular.

## Funcionalidades

- ✅ Listagem de pessoas (CQRS - Query via MongoDB)
- ✅ Criação de pessoas (CQRS - Command via MySQL)
- ✅ Edição de pessoas
- ✅ Exclusão de pessoas
- ✅ Layout responsivo similar ao Angular (Material Design)
- ✅ Sidebar com navegação
- ✅ Mensagens de feedback (success/error)
- ✅ Modal de confirmação de exclusão

## Arquitetura

```
front/django/first/
├── config/                  # Configurações Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── persons/                 # App de pessoas
│   ├── forms.py            # Formulários
│   ├── services.py         # Service layer (API calls)
│   ├── urls.py             # Rotas
│   └── views.py            # Views
├── static/css/             # Estilos CSS
├── templates/              # Templates HTML
│   ├── base.html           # Layout base
│   └── persons/
│       ├── list.html       # Lista de pessoas
│       └── form.html       # Formulário
├── Dockerfile
├── manage.py
└── requirements.txt
```

## Variáveis de Ambiente

| Variável | Descrição | Default |
|----------|-----------|---------|
| `API_COMMAND_URL` | URL da API de comandos (MySQL) | `http://localhost:3000` |
| `API_QUERY_URL` | URL da API de queries (MongoDB) | `http://localhost:3001` |
| `DJANGO_SECRET_KEY` | Chave secreta do Django | dev key |
| `DJANGO_DEBUG` | Modo debug | `True` |
| `DJANGO_ALLOWED_HOSTS` | Hosts permitidos | `localhost,127.0.0.1,0.0.0.0` |

## Executar Local

```bash
cd front/django/first
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py runserver 0.0.0.0:8000
```

## Docker

```bash
docker-compose up -d django
```

Acesse: http://localhost:8082
