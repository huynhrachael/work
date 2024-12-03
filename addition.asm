;unsigned short num1 = 0xFEDC; 		// use dw to declare 16-bit variable
;uunsigned short num2 = 0x1234; 	// use dw to declare 16-bit variable
;unsigned int sum = 0; 			// use dd to declare 32-bit variable
;sum = int(num1 + num2);

section .data
SYS_exit	equ	60
EXIT_SUCCESS	equ	0
num1	dw	0xFEDC
num2	dw	0x1234	
sum	dd	0

section .text
	global _start
_start:
	mov	dx,0
	mov	ax,word[num1]
	mov	ax,word[num2]
	adc	dx,0
	mov	word[sum+0],ax
	mov	word[sum+2],dx
	
	mov	rax, SYS_exit		;terminate executing process
	mov	rsi,EXIT_SUCCESS	;exit status
	syscall				;calling system services
