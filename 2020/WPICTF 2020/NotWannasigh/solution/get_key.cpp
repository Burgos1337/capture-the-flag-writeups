#include <stdio.h>
#include <stdlib.h>
#include <time.h>

FILE *f;

int main() {
    int i, n;
   
    n = 374109;
   
    srand(1585599106); 

    f = fopen("key.txt", "w");
    for (i = 0 ; i < n ; i++) {
    	fprintf(f, "%d", rand() & 0xff);
    }
    fclose(f);
    return(0);
}
