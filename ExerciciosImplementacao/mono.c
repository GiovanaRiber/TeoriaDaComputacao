#include <stdio.h>
#include <string.h>

int main() {
    char entrada[] = "abbc#cba";
    char w[100], wr[100];
    size_t i;
    int valido;

    r1: valido = 1; 
    r2: i = strchr(entrada, '#') - entrada;  
    if (i == (size_t)(-1)) {
        valido = 0;  
        goto r7;  
    }
    r3: strncpy(w, entrada, i);  
    w[i] = '\0'; 
    r4: strcpy(wr, entrada + i + 1);  
    r5: 
    for (size_t j = 0; j < strlen(w); j++) {
        if (w[j] != wr[strlen(w) - j - 1]) {  
            valido = 0;  
            goto r7; 
        }
    }
    r7: 
    printf("%d\n", valido);  
    return valido;  
}
