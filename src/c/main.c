#include <stdio.h>
#include <string.h>

// Definição da estrutura para a entidade Cliente (Usuário da plataforma de tickets eletrônicos)
struct Cliente
{
    int id;
    char nome[50];
    char email[50];
    char senha[50];
};

// Função para buscar um cliente pelo ID na base de dados em memória
struct Cliente *buscar_por_id(struct Cliente registros[], int tamanho, int id_procurado)
{
    for (int i = 0; i < tamanho; i++)
    {
        if (registros[i].id == id_procurado)
        {
            return &registros[i];
        }
    }
    return NULL;
}

int main(void)
{
    // Inicialização do "banco de dados" em memória com clientes do sistema de tickets
    struct Cliente clientes_db[3] = {
        {1, "Lucas Almeida", "lucas.almeida@ticketfy.com", "hash_senha1"},
        {2, "Mariana Souza", "mariana.souza@ticketfy.com", "hash_senha2"},
        {3, "Carlos Eduardo", "carlos.eduardo@ticketfy.com", "hash_senha3"}};
    int tamanho = 3;

    printf("=== SISTEMA DE TICKETS ELETRÔNICOS - LISTAGEM DE CLIENTES ===\n");
    for (int i = 0; i < tamanho; i++)
    {
        printf("id=%d | nome=%s | email=%s\n",
               clientes_db[i].id,
               clientes_db[i].nome,
               clientes_db[i].email);
    }

    printf("\n=== BUSCA POR ID (ID: 2) ===\n");
    struct Cliente *resultado = buscar_por_id(clientes_db, tamanho, 2);
    if (resultado != NULL)
    {
        printf("Encontrado -> id=%d | nome=%s | email=%s\n",
               resultado->id,
               resultado->nome,
               resultado->email);
    }
    else
    {
        printf("Não encontrado\n");
    }

    return 0;
}