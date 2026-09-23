# src/python/main.py

import hashlib

# Banco de dados em memória para a entidade de Passageiros (domínio de viagens/turismo)
passageiros_db = []
_id_contador = 1


def cadastrar(registros, nome_completo, email, senha):
    """Cadastra um novo passageiro garantindo a unicidade do e-mail e hash da senha."""
    global _id_contador

    # Validação de regra de negócio: e-mail único
    for registro in registros:
        if registro["email"] == email:
            raise ValueError(f"Erro: O e-mail '{email}' já está cadastrado no sistema.")

    # Aplicação de hash na senha (atendendo à regra de segurança do modelo)
    senha_hash = hashlib.sha256(senha.encode("utf-8")).hexdigest()

    novo_passageiro = {
        "id": _id_contador,
        "nome_completo": nome_completo,
        "email": email,
        "senha": senha_hash,
    }

    registros.append(novo_passageiro)
    _id_contador += 1
    return novo_passageiro


def buscar_por_id(registros, id_procurado):
    """Busca um passageiro pelo seu identificador único."""
    for registro in registros:
        if registro["id"] == id_procurado:
            return registro
    return None


def listar(registros):
    """Retorna todos os passageiros cadastrados."""
    return registros


def atualizar(registros, id_procurado, novo_nome=None, novo_email=None):
    """Atualiza os dados de um passageiro existente."""
    passageiro = buscar_por_id(registros, id_procurado)
    if not passageiro:
        return None

    if novo_nome:
        passageiro["nome_completo"] = novo_nome

    if novo_email:
        for registro in registros:
            if registro["email"] == novo_email and registro["id"] != id_procurado:
                raise ValueError(
                    f"Erro: O e-mail '{novo_email}' já está em uso por outro passageiro."
                )
        passageiro["email"] = novo_email

    return passageiro


# Execução e testes do sistema em memória adaptado para o domínio de viagens
if __name__ == "__main__":
    print("=== CADASTRO DE PASSAGEIROS ===")
    try:
        cadastrar(
            passageiros_db, "Carla Mendes", "carla.mendes@viagens.com", "viagem2026"
        )
        cadastrar(
            passageiros_db,
            "Marcos Vinicius",
            "marcos.vinicius@viagens.com",
            "turismo456",
        )
        print("Passageiros cadastrados com sucesso.")
    except ValueError as e:
        print(e)

    print("\n=== LISTAGEM DE PASSAGEIROS ===")
    for passageiro in listar(passageiros_db):
        print(passageiro)

    print("\n=== BUSCA POR ID (ID: 2) ===")
    resultado_busca = buscar_por_id(passageiros_db, 2)
    print(resultado_busca if resultado_busca else "Não encontrado")

    print("\n=== ATUALIZAÇÃO (ID: 1) ===")
    passageiro_atualizado = atualizar(
        passageiros_db, 1, novo_nome="Carla Mendes de Souza"
    )
    print(passageiro_atualizado)

    print("\n=== TENTATIVA DE DUPLICAÇÃO DE E-MAIL (Erro esperado) ===")
    try:
        cadastrar(
            passageiros_db, "Outra Carla", "carla.mendes@viagens.com", "senhadiferente"
        )
    except ValueError as e:
        print(f"Exceção capturada corretamente: {e}")
