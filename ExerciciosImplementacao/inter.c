#include <stdio.h>
#include <string.h>

int pertence(const char *entrada) {
    size_t pos = strchr(entrada, '#') - entrada; 
    if (pos == (size_t)(-1)) return 0; 

    char w[100], wr[100];
    strncpy(w, entrada, pos);
    w[pos] = '\0'; 
    strcpy(wr, entrada + pos + 1); 

    if (strlen(w) != strlen(wr)) return 0; 

    size_t i = 0;
    while (i < strlen(w)) { 
        if (w[i] != wr[strlen(wr) - i - 1]) {
            return 0; 
        }
        i++;
    }
    return 1; 
}

int main() {
    char entrada[] = "abbc#cba";
    printf("%d\n", pertence(entrada));
    return 0;
}
