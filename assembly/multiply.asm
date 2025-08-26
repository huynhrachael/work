;unsigned int num1 = 300,000; 		// use dd to declare 32-bit variable
;unsigned int num2 = 400,000; 		// use dd to declare 32-bit variable
;unsigned long product = 0; 		// use dq to declare 64-bit variable
;product = long(num1 * num2);

section .data
SYS_exit	equ	60
EXIT_SUCCESS	equ	0
num1	dd	300000
num2	dd	400000	
product	dq	0

section .text
	global _start
_start:
	mov	eax,word[num1]
	mul	dword[num2]
	mov	dword[product],eax
	mov	dword[product+4],edx
_stop:
	mov	rax,SYS_exit		;terminating executing process
	mov	rdi,EXIT_SUCCESS	;exit status
	syscall

