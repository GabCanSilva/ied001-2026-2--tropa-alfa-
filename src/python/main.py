# src/python/main.py

import hashlib

# Banco de dados em memória para a entidade de Clientes/Usuários
# de um Sistema de Venda de Tickets Eletrônicos
clientes_db = []
_id_contador = 1


def cadastrar(registros, nome, email, senha):
	"""Cadastra um cliente, garantindo e-mail único e senha protegida."""
	global _id_contador

	# Garante que não existam dois clientes com o mesmo e-mail.
	for registro in registros:
		if registro["email"] == email:
			raise ValueError(
				f"Erro: O e-mail '{email}' já está cadastrado no sistema de tickets."
			)

	# Armazena apenas o hash da senha, nunca a senha original.
	senha_hash = hashlib.sha256(senha.encode("utf-8")).hexdigest()

	novo_cliente = {
		"id": _id_contador,
		"nome": nome,
		"email": email,
		"senha": senha_hash,
	}

	registros.append(novo_cliente)
	_id_contador += 1
	return novo_cliente


def buscar_por_id(registros, id_procurado):
	"""Busca um cliente pelo identificador na base de dados."""
	for registro in registros:
		if registro["id"] == id_procurado:
			return registro
	return None


def listar(registros):
	"""Retorna todos os clientes cadastrados na plataforma."""
	return registros


def atualizar(registros, id_procurado, novo_nome=None, novo_email=None):
	"""Atualiza os dados cadastrais de um cliente existente."""
	cliente = buscar_por_id(registros, id_procurado)
	if not cliente:
		return None

	if novo_nome:
		cliente["nome"] = novo_nome

	if novo_email:
		for registro in registros:
			if registro["email"] == novo_email and registro["id"] != id_procurado:
				raise ValueError(
					f"Erro: O e-mail '{novo_email}' já está em uso por outro cliente."
				)
		cliente["email"] = novo_email

	return cliente

if __name__ == "__main__":
	print("=== CADASTRO DE CLIENTES - TICKETS ELETRÔNICOS ===")
	try:
		cadastrar(
			clientes_db,
			"Lucas Almeida",
			"lucas.almeida@ticketfy.com",
			"senhaIngresso123",
		)
		cadastrar(
			clientes_db,
			"Mariana Souza",
			"mariana.souza@ticketfy.com",
			"securePass456",
		)
		print("Clientes cadastrados com sucesso.")
	except ValueError as erro:
		print(erro)

	print("\n=== LISTAGEM DE CLIENTES ===")
	for cliente in listar(clientes_db):
		print(cliente)

	print("\n=== BUSCA POR ID (ID: 2) ===")
	resultado_busca = buscar_por_id(clientes_db, 2)
	print(resultado_busca if resultado_busca else "Não encontrado")

	print("\n=== ATUALIZAÇÃO (ID: 1) ===")
	cliente_atualizado = atualizar(clientes_db, 1, novo_nome="Lucas Almeida Silva")
	print(cliente_atualizado)
