;#begin define print(addr, n)
;	rax = 1;
;	rdi = 1;
;	rsi = addr of string;
;	rdx = n;
;	syscall;
;#end
;#begin define scan(addr, n)
;	rax = 1;
;	rdi = 1;
;	rsi = addr of buffer;
;	rdx = n;
;	syscall;
;#end
;void main() {
;	char buffer[4];
;	int n;
;	int sumN;
;	char ascii[10];
;	char msg1[26] = "Input a number (004~999): ";
;	char msg2[16] = "1 + 2 + 3 +...+ ";
;	char msg3[4] = " = ";
;
;	print(msg1, 26);
;	scan(buffer, 4);
;	call toInteger(n, buffer);
;	call calculate(n, sumN);
;	call toString(n, ascii);
;	print(msg2, 16);
;	print(buffer, 3);
;	print(msg3, 3);
;	print(ascii, 6);
;}
;void toInteger(n, buffer) {
;	n = atoi(buffer);
;}
;void calculate(n, sumN) {
;	for(ecx=0; ecx<=n; ecx++) {
;		sumN += ecx;
;	}
;}
;void toString(sumN, ascii) {
;	ascii = itoa(sumN);
;}

;Code starts here
%macro	print 	2
        mov     rax, 1					;SYS_write
        mov     rdi, 1					;standard output device
        mov     rsi, %1					;output string address
        mov     rdx, %2					;number of character
        syscall						;calling system services
%endmacro

%macro	scan 	2
        mov     rax, 0					;SYS_read
        mov     rdi, 0					;standard input device
        mov     rsi, %1					;input buffer address
        mov     rdx, %2					;number of character
        syscall						;calling system services
%endmacro

section .bss
buffer	resb	4
n	resd	1
sumN	resd    1
ascii	resb    10

section	.data
LF		equ	10
NULL		equ	0
SYS_exit	equ	60
EXIT_SUCCESS	equ	0
msg1	db	"Input a number (004~999): ", NULL
msg2	db      "1 + 2 + 3 +...+ ", NULL
msg3	db	" = ", LF

section .text
        global _start
_start:
printmsg1:
	print	msg1, 26				;cout << msg1
	scan	buffer, 4				;cin >> buffer
	
	; converts buffer into n
	mov	rdi, buffer				;rdi = address of buffer
	mov	rsi, n					;rsi = address of n
	call	toInteger
	
	; calculates 1+2+3+...+N
	mov	rcx, 0					;rcx = 0
	mov	rdi, n					;rdi = addr. of n
	mov	rsi, sumN				;rsi = addr. of sumN
	call 	calculate				;call calculate
	
	; converts sum100 into ascii
	mov	rdi, sumN				;rdi = addr. of sumN
	mov	rsi, ascii				;rsi = addr. of ascii
	call	tostring
	
	; display message and result
	print	msg2, 16				;cout << msg2
	print	buffer, 3				
	print	msg3, 3 				;cout << str1
	print	ascii, 7				;cout << ascii

        mov     rax, SYS_exit				;terminate excuting process
        mov     rdi, EXIT_SUCCESS			;exit status
        syscall						;calling system services

;ascii to number
toInteger:
	mov	rax, 0					;clear ax
	mov	rbx, 10					;bx = 10
	mov	rsi, 0					;counter = 0
inputloop:
	mov	ecx,dword[buffer+rsi]			;convert ascii to number
	and	ecx,0fh
	add	eax,ecx
	
	adc	edx,0
	cmp	rsi, 2					;compare rcx with 2
	je	skipMul					;if rcx=2 goto skipMul
	mul	ebx					;dx:ax = ax * bx
skipMul:
	inc	rsi					;rcx++
	cmp	rsi, 3					;compare rcx with 3
	jl	inputloop				;if rcx<3 goto inputLoop
	mov	dword[n], eax				;n = ax

	; calculates 1+2+3+...+n
	mov	ecx, 0					;cx = 0
	ret

;calculate sum into ascii
calculate:
	add	dword[sumN], ecx			;sumN += cx
	inc	ecx					;cx++
	cmp	ecx, dword[n]				;compare cx with N
	jbe	calculate					;if(cx<=100) goto sumLoop
	ret

;converts sumN into ascii
tostring:
	;Part A - Successive division
	mov 	eax, dword[sumN] 			;get integer
	mov 	rcx, 0 					;digitCount = 0
	mov 	rbx, 10 				;set for dividing by 10
divideLoop:
	mov 	edx, 0
	div 	ebx 					;divide number by 10
	push 	rdx 					;push remainder
	inc 	rcx 					;increment digitCount
	cmp 	eax, 0 					;if (result > 0)
	jne 	divideLoop 				;goto divideLoop

	;Part B - Convert remainders and store
	mov 	rbx, ascii 				;get addr of ascii
	mov 	rdi, 0 					;rdi = 0
popLoop:
	pop 	rax 					;pop intDigit
	add 	eax, "0" 				;al = al + 0x30
	mov 	byte [rbx+rdi], al 			;string[rdi] = al
	inc 	rdi 					;increment rdi
	loop 	popLoop 				;if (digitCount > 0) goto popLoop
	ret

















