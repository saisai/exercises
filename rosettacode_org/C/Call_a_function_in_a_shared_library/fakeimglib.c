#include <stdio.h>

int openimage(const char *s) {
    static int handle = 100;
    fprintf(stderr, "opening %s\n", s);
    return handle++;
}

/* gcc -shared -fPIC -nostartfiles fakeimglib.c -o fakeimglib.so */
