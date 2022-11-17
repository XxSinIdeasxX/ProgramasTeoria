#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<time.h>

int menu();
void sigma(int, FILE*);
void binario(int,int, FILE*);

int main(){
    srand(time(NULL));
    FILE *doc;
    doc=fopen("Universo.txt","w"); //inicia con un archivo en blanco
  //doc=fopen("Universo.txt","a"); 
    int op;
    int n;
    while(1){
        op=menu();
        switch(op){
        case 1:
            printf("\nIngrese el valor de n: ");
            scanf("%d",&n);
            printf("Generando el universo de n = %d...\n\n",n);
            fprintf(doc,"\tUniverso de n = %d\n\nU = {e",n);
            sigma(n,doc);
            fputs("}\n\n",doc);
            printf("Se genero correctamente el universo de n = %d\n\n",n);
            break;
        case 2:
            n=rand()%1001;
            printf("Generando el universo de n = %d...\n\n",n);
            fprintf(doc,"\tUniverso de n = %d\n\nU = {e",n);
            sigma(n,doc);
            fputs("}\n\n",doc);
            printf("Se genero correctamente el universo de n = %d\n\n",n);
            break;
        case 3:
            printf("\nHasta luego :D");
            exit(0);
            break;
        default:
            break;
        }
    }
    return 0;
}

void binario(int n, int elem, FILE *doc){
    if(n==0){
        while(elem>0){
            fputc('0',doc);
            elem--;
        }
        return;
    }
    binario(n/2,elem-1,doc);
    fprintf(doc,"%d",n%2);
}

void sigma(int n, FILE *doc){
    if(n==0){
        return;
    }
    sigma(n-1,doc);
    //lo que genera sigma de n
    int i;
    for(i=0;i<pow(2,n);i++){
        fputs(", ",doc);
        binario(i, n, doc);
    }
}

int menu(){
    int respuesta = 0;
	printf("\n\t\t    Menu\n============================================\n");
	printf("1. Generar uinverso n\n");
	printf("2. Generar univerrso con n aleatorio\n");
	printf("3. Salir\n\nSeleccione una opcion: ");
	scanf("%d",&respuesta);
	while(respuesta>3 || respuesta<1){
        fflush(stdin);
		printf("\n\t> Error <\n\nSeleccione una opcion valida: ");
		scanf("%d",&respuesta);
	}return respuesta;
}