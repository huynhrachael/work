;unsigned short array[7] = {12, 1003, 6543, 24680, 789, 30123, 32766}; // use dw for 16-bit array
;unsigned short even[7]; // use resw to declare 16-bit variable
;register long rsi = 0, rdi = 0; // no need to declare register rsi and rdi
;do {
;	if(array[rsi] % 2 == 0) {
;		even[rdi] = array[rsi];
;		rdi++;
;	}
;rsi++;
;} while(rsi < 7)

section	.data
SYS_exit	equ	60
EXIT_SUCCESS	equ	0
array		db	12, 1003, 6543, 24680, 789, 30123, 32766

section .bss
even	resw	7

section	.text
	global _start
_start:
	mov	rsi,0		;array
	mov	rdi,0		;even

doloop:
	mov	ax,word[array+(rsi*2)]
	mov	dx,0
	mov	bx,2
	div	bx
	cmp	dx,0
	jne	skip
	mul	bx
	mov	word[even+(rdi*2)],ax
	inc 	rdi
skip:
	inc	rsi
	cmp	rsi,7
	jb	doloop
endloop:
	mov	rax,SYS_exit		;terminating executing process
	mov	rdi,EXIT_SUCCESS	;exit status
	syscall		

