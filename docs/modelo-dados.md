# Modelo de Dados - Entidade Principal

## Entidade
Usuario

## Finalidade
Representa a entidade de cadastro de usuários no sistema, centralizando as informações de autenticação, identificação e contato de cada pessoa com acesso à plataforma.

## Atributos
- id: Identificador único e imutável do usuário (chave primária, gerada automaticamente).
- nome: Nome completo do usuário.
- email: Endereço de correio eletrônico único utilizado como identificador de login e canal de comunicação.
- senha: Hash criptográfico da senha de acesso do usuário (nunca armazenada em texto plano).

## Operações
- cadastrar(nome, email, senha)
- buscar_por_id(id)
- listar()
- atualizar(id, dados_atualizados)

## Regras / invariantes
1. O atributo **email** deve ser estritamente único no sistema e seguir um formato de e-mail válido.
2. O atributo **senha** deve obrigatoriamente ser persistido utilizando um algoritmo de hash seguro e salt (ex: bcrypt ou Argon2), sendo proibido o armazenamento da senha em texto puro.

## Operação provavelmente frequente
autenticar_por_email_e_senha - justificativa: Operação executada a cada tentativa de login na plataforma, sendo o ponto de entrada crítico para a sessão do usuário.