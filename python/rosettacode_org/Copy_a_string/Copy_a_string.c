#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    char src[] = "Hello";
    char dst[80];

    /* Use strlcpy() from <string.h>. */
    if (strncpy(dst, src, sizeof dst) >= sizeof dst) {
        fputs("The buffer is too smaill!\n", stderr);
        exit(1);
    }

    memset(src, '-', 5);
    printf("src: %s\n", src); /* src: ----- */
    printf("dst: %s\n", dst); /* dst: Hello */

    return 0;
}
