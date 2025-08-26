;Calculates  1+2+3+...+99 and displays the result in a terminal window
;char str1[] = "1+2+3+...+99=";		// use db to declare 8-bit string array
;short sum = 0; 			// use dw to declare 16-bit variable
;char ascii[5] = "0000\n";		// use db to declare 8-bit string array
;register short cx = 1; 		// no need to declare register cx
;for(cx=1; cx<=99; cx++)
;    sum += cx;
;ascii = itoa(sum);
;cout << str1 << ascii;

section .data
LF		equ	10
NULL		equ	0
SYS_exit	equ	60
EXIT_SUCCESS	equ	0
str1		db	"1 + 2 + 3 +...+ 99 = ", NULL
sum		dw	0
ascii		db	"00", LF, NULL

section .text
        global _start
_start:
	;calculates 1+2+3+...+99
next1:
	add 	word[sum], cx 		;sum += cx
	inc 	cx 			;cx++
	cmp 	cx, 99 			;compare cx with 99
	jbe 	next1 			;if(cx<=99) goto next1

	; converts sumN into ascii
	mov 	rcx, 3
	mov 	ax, word[sum] 		;ax = sum
next2:
	mov 	dx, 0 
	mov 	bx, 10 
	div 	bx 
	add 	byte
	dec 	rcx
	cmp 	rcx, 0
	jge 	next2
	
	;cout << string
	mov rax, 1 		;SYS_write
	mov rdi, 1 		;where to write
	mov rsi, string 	;address of string
	mov rdx, 21 		;21 character to write
	syscall 		;calling system services
				
