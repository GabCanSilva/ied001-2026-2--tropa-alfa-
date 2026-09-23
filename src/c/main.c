// src/c/main.c
#include <stdio.h>
#include <string.h>

// Definição da estrutura para a entidade Passageiro
struct Passageiro {
    int id;
    char nome_completo[50];
    char email[50];
    char senha[50];
};

// Função para buscar um passageiro pelo ID no banco em memória
struct Passageiro* buscar_por_id(struct Passageiro registros[], int tamanho, int id_procurado) {
    for (int i = 0; i < tamanho; i++) {
        if (registros[i].id == id_procurado) {
            return &registros[i];
        }
    }
    return NULL;
}

int main(void) {
    // Inicialização do "banco de dados" em memória com a entidade Passageiro
    struct Passageiro passageiros_db[3] = {
        {1, "Carla Mendes", "carla.mendes@viagens.com", "hash_senha1"},
        {2, "Marcos Vinicius", "marcos.vinicius@viagens.com", "hash_senha2"},
        {3, "Ana Silva", "ana.silva@viagens.com", "hash_senha3"}
    };
    int tamanho = 3;

    printf("=== LISTAGEM DE PASSAGEIROS ===\n");
    for (int i = 0; i < tamanho; i++) {
        printf("id=%d | nome=%s | email=%s\n", 
               passageiros_db[i].id, 
               passageiros_db[i].nome_completo, 
               passageiros_db[i].email);
    }

    printf("\n=== BUSCA POR ID (ID: 2) ===\n");
    struct Passageiro* resultado = buscar_por_id(passageiros_db, tamanho, 2);
    if (resultado != NULL) {
        printf("Encontrado -> id=%d | nome=%s | email=%s\n", 
               resultado->id, 
               resultado->nome_completo, 
               resultado->email);
    } else {
        printf("Não encontrado\n");
    }

    return 0;
}