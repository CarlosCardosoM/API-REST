# Monografias API

API RESTful para cadastro, consulta e gerenciamento de monografias acadêmicas. O projeto utiliza Django REST Framework, autenticação por token e fornece documentação automática via Swagger e ReDoc.

---

## Sumário

- [Como rodar o projeto](#como-rodar-o-projeto)
- [Endpoints da API](#endpoints-da-api)
- [Autenticação](#autenticação)
- [Modelo de Dados](#modelo-de-dados)
- [Documentação Interativa](#documentação-interativa)
- [Exemplo de uso com curl](#exemplo-de-uso-com-curl)

---

## Como rodar o projeto

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/CarlosCardosoM/API-REST.git
   cd API-REST
   ```

2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Realize as migrações:**
   ```bash
   python manage.py migrate
   ```

4. **Crie um superusuário (opcional, para acesso ao admin):**
   ```bash
   python manage.py createsuperuser
   ```

5. **Rode o servidor:**
   ```bash
   python manage.py runserver
   ```

---

## Endpoints da API

| Método | Endpoint                      | Descrição                                         | Autenticação |
|--------|-------------------------------|---------------------------------------------------|--------------|
| POST   | `/api/api-token-auth/`        | Gera token de autenticação                        | Não          |
| GET    | `/api/monografias/`           | Lista todas as monografias                        | Não          |
| POST   | `/api/monografias/`           | Cria uma nova monografia                          | Sim          |
| GET    | `/api/monografias/<id>/`      | Detalha uma monografia específica                 | Sim          |
| PUT    | `/api/monografias/<id>/`      | Atualiza todos os campos de uma monografia        | Sim          |
| PATCH  | `/api/monografias/<id>/`      | Atualiza campos específicos de uma monografia     | Sim          |
| DELETE | `/api/monografias/<id>/`      | Remove uma monografia                             | Sim          |

---

## Autenticação

- A autenticação é feita via Token (TokenAuthentication).
- Para obter o token, envie usuário e senha via POST para `/api/api-token-auth/`.  
  Exemplo:
  ```bash
  curl -X POST -d "username=SEU_USUARIO&password=SUA_SENHA" http://localhost:8000/api/api-token-auth/
  ```
  O retorno será:
  ```json
  {"token": "seutokenxxx"}
  ```
- Para acessar endpoints protegidos, inclua o header:
  ```
  Authorization: Token SEU_TOKEN_AQUI
  ```

---

## Modelo de Dados

O modelo principal é `Monografia`, com os seguintes campos:

- `titulo`: Título da monografia
- `autor`: Nome do autor
- `orientador`: Nome do orientador
- `coorientador`: Nome do coorientador (opcional)
- `resumo`: Resumo em português
- `abstract`: Resumo em inglês
- `palavras_chave`: Palavras-chave separadas por vírgula
- `data_defesa`: Data da defesa
- `arquivo`: Upload do arquivo da monografia (PDF, opcional)

---

## Documentação Interativa

Acesse a documentação automática da API:

- **Swagger UI:** [http://localhost:8000/swagger/](http://localhost:8000/swagger/)
- **ReDoc:** [http://localhost:8000/redoc/](http://localhost:8000/redoc/)

Nessas páginas você pode testar endpoints, visualizar parâmetros, exemplos de requisições, e conferir as respostas.

---

## Exemplo de uso com curl

**Listar monografias (GET público):**
```bash
curl http://localhost:8000/api/monografias/
```

**Cadastrar nova monografia (POST autenticado):**
```bash
curl -X POST -H "Authorization: Token SEU_TOKEN_AQUI" \
     -F "titulo=Minha Monografia" \
     -F "autor=João" \
     -F "orientador=Prof. Silva" \
     -F "resumo=Texto do resumo" \
     -F "abstract=Abstract text" \
     -F "palavras_chave=palavra1, palavra2" \
     -F "data_defesa=2024-12-10" \
     http://localhost:8000/api/monografias/
```

---

## Observações

- Para acesso ao admin, utilize `/admin/`.
- O projeto permite upload de arquivos PDF de até 5MB para cada monografia.
- Permissões padrão: somente usuários autenticados podem criar, editar e excluir monografias.

---

**Dúvidas ou sugestões?**  
Abra uma issue ou entre em contato!
