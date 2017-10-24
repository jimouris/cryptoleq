#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <inttypes.h>

#define WORD_SIZE 16
#define KEY_WORDS 4
#define ROUNDS 32

#define WORD_MASK ((0x1ull << (WORD_SIZE&63)) - 1)
#define C ((0xffffffffffffffffull ^ 0x3ull) & WORD_MASK)

uint16_t z[5][62] = {
    {1,1,1,1,1,0,1,0,0,0,1,0,0,1,0,1,0,1,1,0,0,0,0,1,1,1,0,0,1,1,0,1,1,1,1,1,0,1,0,0,0,1,0,0,1,0,1,0,1,1,0,0,0,0,1,1,1,0,0,1,1,0},
    {1,0,0,0,1,1,1,0,1,1,1,1,1,0,0,1,0,0,1,1,0,0,0,0,1,0,1,1,0,1,0,1,0,0,0,1,1,1,0,1,1,1,1,1,0,0,1,0,0,1,1,0,0,0,0,1,0,1,1,0,1,0},
    {1,0,1,0,1,1,1,1,0,1,1,1,0,0,0,0,0,0,1,1,0,1,0,0,1,0,0,1,1,0,0,0,1,0,1,0,0,0,0,1,0,0,0,1,1,1,1,1,1,0,0,1,0,1,1,0,1,1,0,0,1,1},
    {1,1,0,1,1,0,1,1,1,0,1,0,1,1,0,0,0,1,1,0,0,1,0,1,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,1,0,1,0,0,1,1,1,0,0,1,1,0,1,0,0,0,0,1,1,1,1},
    {1,1,0,1,0,0,0,1,1,1,1,0,0,1,1,0,1,0,1,1,0,1,1,0,0,0,1,0,0,0,0,0,0,1,0,1,1,1,0,0,0,0,1,1,0,0,1,0,1,0,0,1,0,0,1,1,1,0,1,1,1,1}
};

#define ROR(x, r) ((x >> r) | (x << ((sizeof(uint16_t) * 8) - r)))
#define ROL(x, r) ((x << r) | (x >> ((sizeof(uint16_t) * 8) - r)))

void simon_encrypt(uint16_t const pt[static 2], uint16_t ct[static 2], uint16_t const K[static ROUNDS]) {
    ct[0] = pt[0];
    ct[1] = pt[1];
    uint16_t tmp;
    for (int i = 0; i < ROUNDS; ++i) {
        tmp = ct[0];
        ct[0] = ct[1] ^ (ROL(ct[0], 1) & ROL(ct[0], 8)) ^ ROL(ct[0], 2) ^ K[i];
        ct[1] = tmp;
    }
}

void simon_decrypt(uint16_t const ct[static 2], uint16_t pt[static 2], uint16_t const K[static ROUNDS]) {
    uint16_t tmp;
    pt[0] = ct[0];
    pt[1] = ct[1];
    for (int i = 0; i < ROUNDS; ++i) {
        tmp = pt[1];
        pt[1] = pt[0] ^ (ROL(pt[1], 1) & ROL(pt[1], 8)) ^ ROL(pt[1], 2) ^ K[ROUNDS-i-1];
        pt[0] = tmp;
    }
}

int main(void) {
    uint16_t plain_text[2] = { 0x6565, 0x6877 };
    const uint16_t cipher_text[2] = { 0xc69b, 0xe9bb };
    uint16_t buffer[2] = { 0 };

    uint16_t exp[ROUNDS] = { 256, 2312, 4368, 6424, 29123, 46665, 22228, 57456, 61786, 50485, 56724, 16400, 9482, 28518, 59755, 19416, 4069, 31815, 57583, 15905, 1627, 17292, 62058, 46528, 34313, 40846, 55487, 2476, 59410, 10000, 11434, 36116};

    printf("PTL: %" PRIu16 ", PTR: %" PRIu16 " \n", plain_text[0], plain_text[1]);
    simon_encrypt(plain_text, buffer, exp);
    printf("CTL: %" PRIu16 ", CTR: %" PRIu16 " \n", buffer[0], buffer[1]);

    if (buffer[0] != cipher_text[0] || buffer[1] != cipher_text[1]) {
        printf("Encryption failed!\n");
        return EXIT_FAILURE;
    }
    printf("Encryption ok!\n");

    return EXIT_SUCCESS;
}