;char msg1[] = "Input a number (1~9): ";
;char msg2[] = " is Multiple of 3.";
;char buffer[2];
;char num;
;char ascii[10];
;register int r10 = 0;
;do {
;	cout << msg1;
;	cin >> buffer;
;	ascii[r10] = buffer[0];
;	r10++;
;} while(r10 < 9);
;r10 = 0;
;do {
;	num = atoi(ascii[r10]);
;	if(num%3 == 0) {
;		cout << ascii[r10] << msg2;
;	}
;r10++;
;} while(r10 < 9);

section .bss
num		resb    1			
buffer		resb	2
ascii		resb	10			

section .data
LF		equ	10
NULL		equ	0
SYS_exit	equ	60
EXIT_SUCCESS	equ	0
mesg1		db	"Input a number (0~9): "
mesg2		db	" is a multiple of 3. ", LF

section .text
        global _start
_start:
	mov	r12, 0			;counter
do1:
	;cout << mesg1
        mov     rax, 1				
        mov     rdi, 1				
        mov     rsi, mesg1			
        mov     rdx, 22				
        syscall
       
	;cin >> num
	mov	rax, 0				
	mov	rdi, 0				
	mov	rsi, buffer		
	mov	rdx, 2				
	syscall	
					
	mov	al, byte[buffer]
	mov	byte[ascii+r12], al		
	and	al, 0fh				
	mov	byte[num], al			
        
        ;if num%3==0
	mov	ah,0
	mov	al,byte[num]
	mov	bl,3
	div	bl
	cmp	ah,0
        jne     not_mul3
mess2:        
        ;cout << ascii
	mov     rax, 1				
        mov     rdi, 1				
        mov     rsi, buffer			
        mov     rdx, 1				
        syscall	
          
        ;cout << meg2
        mov     rax, 1				
        mov     rdi, 1				
        mov     rsi, mesg2			
        mov     rdx, 22				
        syscall	
not_mul3:
	inc	r12
	cmp	r12, 9			
        jne	do1	

done: 
	mov     rax, SYS_exit			;terminate excuting process
        mov     rdi, EXIT_SUCCESS		;exit status
        syscall					;calling system services
	


















