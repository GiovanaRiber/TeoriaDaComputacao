#include <stdio.h>
#include <string.h>

int verificaReverso(const char *w, const char *wr, size_t indice) {
    if (indice >= strlen(w)) return 1; 
    if (w[indice] != wr[strlen(w) - indice - 1]) return 0; 
    return verificaReverso(w, wr, indice + 1); 
}

int pertence(const char *entrada) {
    size_t pos = strchr(entrada, '#') - entrada; 
    if (pos == (size_t)(-1)) return 0; 

    char w[100], wr[100];
    strncpy(w, entrada, pos);
    w[pos] = '\0'; 
    strcpy(wr, entrada + pos + 1); 

    if (strlen(w) != strlen(wr)) return 0; 

    return verificaReverso(w, wr, 0); 
}

int main() {
    char entrada[] = "abc#cba";
    printf("%d\n", pertence(entrada));
    return 0;
}
