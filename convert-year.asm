; A1W1A1: "year to month & day", in assembly x32
; Run on m86k processor or visit https://asm-editor.specy.app/

org $1000

DATA:

    buffer: dcb.b 32, 0
    void:   dcb.b 8, 0
    
    days:   dc.l ', Days: ', 1
    mths:   dc.l 'Months: ', 1
    size    equ #8

    input:  dc.w 0
    offst:  dc.w 0

CODE:
    
    ; input
    move.b  #4, d0
    trap    #15
    move.w  d1, input
    
    ; months
    lea     buffer, a0
    move.l  a0, a2

    move.l  #12, d0
    lea     mths, a1
    jsr     section

    ; days
    lea     buffer, a1
    jsr     _strlen
    move.l  d1, offst

    add.l   offst, a0
    move.l  a0, a2
    
    move.l  #356, d0
    lea     days, a1
    jsr     section

    ; output
    lea     buffer, a1
    jsr     _strlen
    move.l d1, offst

    move.l  #0, d0
    move.l  offst, d1
    trap    #15
   
    ; clean & exit
    lea     buffer, a1
    move.l  #$50, d1
    jsr     _clrseg
    jmp     EXIT

section:
    
    ; prefix
    jsr     _strcpy

    ; calculate
    move.l  d0, d1
    mulu    input, d1

    ; convert
    move.l  a0, a1
    lea     void, a2 
    add.l   size, a1
    jsr     _itoa
    
section_:
    
    ; exit
    rts

_strlen:

    ; prepare
    clr d1
    clr d2

strlen:

    ; count
    add.b #1, d1
    move.b (a1, d1), d2
    
    ; recurse
    cmp.b #0, d2
    bne strlen

strlen_:

    ; exit
    rts

_strcpy:
    
    ; prepare
    clr     d1
    clr     d2

strcpy:

    ; move
    move.b  (a1, d1), (a2, d1)
    move.b  (a1, d1), d2
    
    ; update
    add.b   #1, d1
    cmp.l   #0, d2
    
    ; recurse
    bne     strcpy
    
strcpy_:
    
    ; exit
    rts

_itoa: 

    ; prepare
    clr     d2
    clr     d3

itoa:

    ; extract LSD
    divu    #10, d1
    swap    d1
    
    ; insert
    move.b  d1, (a1, d2)
    add.b   #'0', (a1, d2)

    ; reset
    clr.b   d1
    swap    d1
    add.b   #1, d2

    ; interrupt
    tst.l   d1
    beq     itoa_revert

    ; recurse
    jmp     itoa

    itoa_revert:
    sub.b   #1, d2

    ; to random
    itoa_export:
    move.b  (a1, d2), (a2, d3)

    sub.b   #1, d2
    add.b   #1, d3

    cmp.b   #0, d2
    bge     itoa_export

    ; from random
    itoa_import:
    move.b  (a2, d2), (a1, d2)
    move.b  #0, (a2, d2)

    add.b   #1, d2
    cmp.b   d2, d3
    bgt     itoa_import

itoa_:
    
    ; exit
    rts

_clrseg:

    clr     d2

clrseg:

    clr     (a1, d2)
    add.b   #2, d2
    cmp.b   d1, d2
    blt     clrseg

clrseg_:

    rts

EXIT:
