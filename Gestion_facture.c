#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_PRODUCTS 50
#define MAX_FILENAME 50

typedef struct {
    char name[50];
    int quantity;
    float price;
} Product;

typedef struct {
    char clientName[50];
    Product products[MAX_PRODUCTS];
    int productCount;
} Invoice;

void addProduct(Invoice *invoice) {
    if (invoice->productCount < MAX_PRODUCTS) {
        Product newProduct;
        printf("Entrez le nom du produit: ");
        scanf("%s", newProduct.name);
        printf("Entrez la quantité: ");
        scanf("%d", &newProduct.quantity);
        printf("Entrez le prix unitaire: ");
        scanf("%f", &newProduct.price);
        
        invoice->products[invoice->productCount++] = newProduct;
    } else {
        printf("Limite de produits atteinte.\n");
    }
}

void saveInvoice(const Invoice *invoice, const char *filename) {
    FILE *file = fopen(filename, "w");
    if (file == NULL) {
        perror("Erreur d'ouverture du fichier");
        return;
    }
    
    fprintf(file, "Facture pour: %s\n", invoice->clientName);
    fprintf(file, "Produits:\n");
    
    for (int i = 0; i < invoice->productCount; i++) {
        fprintf(file, "%s | Quantité: %d | Prix unitaire: %.2f\n",
                invoice->products[i].name,
                invoice->products[i].quantity,
                invoice->products[i].price);
    }
    
    fclose(file);
    printf("Facture enregistrée dans %s\n", filename);
}

void displayInvoice(const Invoice *invoice) {
    printf("Facture pour: %s\n", invoice->clientName);
    printf("Produits:\n");
    
    for (int i = 0; i < invoice->productCount; i++) {
        printf("%s | Quantité: %d | Prix unitaire: %.2f\n",
               invoice->products[i].name,
               invoice->products[i].quantity,
               invoice->products[i].price);
    }
}

int main() {
    Invoice invoice;
    invoice.productCount = 0;
    
    printf("Entrez le nom du client: ");
    scanf("%s", invoice.clientName);
    
    char choice;
    
    do {
        addProduct(&invoice);
        printf("Voulez-vous ajouter un autre produit? (o/n): ");
        scanf(" %c", &choice);
    } while (choice == 'o' || choice == 'O');
    
    displayInvoice(&invoice);
    
    char filename[MAX_FILENAME];
    printf("Entrez le nom du fichier pour enregistrer la facture: ");
    scanf("%s", filename);
    
    saveInvoice(&invoice, filename);
    
    return 0;
}