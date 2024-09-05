

---

# Flix_API

**Flix_API** é uma API desenvolvida em Django que fornece funcionalidades para gerenciar filmes, autenticação de usuários e estatísticas relacionadas a filmes. O projeto utiliza Django REST Framework para construir endpoints RESTful e Django Simple JWT para autenticação baseada em JSON Web Tokens (JWT).

## Funcionalidades

- **Gerenciamento de Filmes**: Adicione, atualize, visualize e exclua informações sobre filmes.
- **Autenticação**: Use JWT para autenticação segura.
- **Estatísticas**: Obtenha estatísticas sobre filmes e avaliações.

## Requisitos

- Python 3.8 ou superior
- Django 3.2 ou superior
- Django REST Framework 3.12 ou superior
- Django Simple JWT 5.0 ou superior

## Instalação

1. **Clone o Repositório**

   ```bash
   git clone https://github.com/gusttavuc1/flix_api.git
   cd flix_api
   ```

2. **Crie e Ative um Ambiente Virtual**

   ```bash
   python -m venv env
   source env/bin/activate  # No Windows use: env\Scripts\activate
   ```

3. **Instale as Dependências**

   ```bash
   pip install -r requirements.txt
   ```

4. **Aplique as Migrações**

   ```bash
   python manage.py migrate
   ```

5. **Crie um Superusuário (Opcional, para acesso ao Django Admin)**

   ```bash
   python manage.py createsuperuser
   ```

6. **Inicie o Servidor de Desenvolvimento**

   ```bash
   python manage.py runserver
   ```

## Configuração

Certifique-se de que o arquivo `settings.py` esteja configurado corretamente para suas necessidades. Aqui está um exemplo de configuração para arquivos estáticos:

```python
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```

## Endpoints da API

### Autenticação

- **POST** `/api/v1/authentication/token/`

  - Obtém o token JWT de autenticação.

- **POST** `/api/v1/authentication/token/refresh/`
  - Atualiza o token JWT.

### Filmes

- **GET** `/api/v1/movies/`

  - Lista todos os filmes.

- **POST** `/api/v1/movies/`

  - Adiciona um novo filme.

- **GET** `/api/v1/movies/{id}/`

  - Obtém detalhes de um filme específico.

- **PUT** `/api/v1/movies/{id}/`

  - Atualiza um filme específico.

- **DELETE** `/api/v1/movies/{id}/`
  - Exclui um filme específico.

### Estatísticas

- **GET** `/api/v1/movies/stats/`
  - Obtém estatísticas sobre filmes e avaliações.

## Contribuição

Contribuições são bem-vindas! Se você tiver sugestões ou encontrar problemas, abra um [issue](https://github.com/gusttavuc1/flix_api/issues) ou envie um [pull request](https://github.com/gusttavuc1/flix_api/pulls).

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Contato

[gusttavuc1@hotmail.com](mailto:gusttavuc1@hotmail.com)
GitHub: [gusttavuc1](https://github.com/gusttavuc1)
