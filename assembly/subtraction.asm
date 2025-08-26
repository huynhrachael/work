;signed short num1 = 0x1234; 		// use dw to declare 16-bit variable
;signed short num2 = 0xFEDC; 		// use dw to declare 16-bit variable
;signed int dif = 0; 			// use dd to declare 32-bit variable
;dif = int(num1 - num2);

section .data
SYS_exit	equ	60
EXIT_SUCCESS	equ	0
num1	dw	0x1234
num2	dw	0xFEDC	
dif	dd	0

section .text
	global _start
_start:
	mov	ax,word[num1]
	sub	ax,word[num2]
	sbb	dx,0
	
	mov	word[dif+0],ax
	mov	word[dif+2],dx
_stop:	
	mov	rax,SYS_exit		;temrinate executing process
	mov	rdi,EXIT_SUCCESS	;exit status
	syscall				;calling system services
