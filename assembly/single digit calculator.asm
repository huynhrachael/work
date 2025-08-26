%macro  print   2
    mov     rax, 1
    mov     rdi, 1
    mov     rsi, %1
    mov     rdx, %2
    syscall
%endmacro

%macro  scan    2
    mov     rax, 0
    mov     rdi, 0
    mov     rsi, %1
    mov     rdx, %2
    syscall
%endmacro

section .bss
no1		resb	1
no2		resb	1
no3		resb	1
no4		resb	1
no5		resb	1
opp1		resb	1
opp2		resb	1
opp3		resb	1
opp4		resb	1
result		resb	1
buffer      	resb	10

section	.data
LF		          equ	    10
NULL		        equ	    0
SYS_exit	      equ	    60
EXIT_SUCCESS	  equ	    0
msg		          db	    "Enter operation strings: ", NULL
equal 	        db      " = " , LF
ascii           db      "00", 10

section .text
        global _start
_start:
	    print   msg, 24
    	scan    buffer, 10		
	
	;read number input
	    mov 	al, byte[buffer+0]		;no1
    	and 	al, 0fh
    	mov 	byte[no1], al
	
    	mov 	al, byte[buffer+2]		;no2
    	and 	al, 0fh
    	mov 	byte[no2], al
	
	    mov 	al, byte[buffer+4]		;no3
    	and 	al, 0fh
    	mov 	byte[no3], al
	
	    mov 	al, byte[buffer+6]		;no4
    	and 	al, 0fh
    	mov 	byte[no4], al
	
	    mov 	al, byte[buffer+8]		;no5
    	and 	al, 0fh
    	mov 	byte[no5], al
    	
	;read operation sign input
	    mov 	al, byte[buffer+1]		;opp1
    	mov 	byte[opp1], al			

    	mov 	al, byte[buffer+3]		;opp2
    	mov 	byte[opp2], al			
   
    	mov 	al, byte[buffer+5]		;opp3
    	mov 	byte[opp3], al			

    	mov 	al, byte[buffer+7]		;opp4
    	mov 	byte[opp4], al			
    	
first:
    	mov	  al, byte[no1]					
	    mov	  byte[result], al	  ;move no1 into result
	    cmp	  byte[opp1], '+'		  ;compare op1 to '+'		
	    jne	  skip11			        ;if op1 =! '+' jump to skip11
	    mov	  dil, byte[result]	  ;moves result into dil
	    mov	  sil, byte[no2]		  ;move no2 into sil
	    call	addition		        ;call adition function
	    jmp	  second			        ;when done jump to second
skip11:
	    cmp	  byte[opp1], '-'		;compare op1 to '-'
	    jne	  skip12			      ;if op1 =! '-' jump to skip12
	    mov	  dil, byte[result]	;moves result into dil
	    mov	  sil, byte[no2]		;move no2 into sil
	    call	subtraction		    ;call subtraction function
	    jmp	second			        ;when done jump to second
skip12:
	    cmp	   byte[opp1], '*'		  ;compare op1 to '*'		
	    jne    skip13		           	;if op1 =! '*' jump to skip13
	    mov	   dil, byte[result]	  ;move result into dil
	    mov    sil, byte[no2]		    ;move no2 into sil
	    call	 multiplication		    ;when done jump to second
	    jmp	second			
skip13:
    	cmp	  byte[opp1], '/'		;compare op1 to '/'				
    	mov   dil, byte[result]	;move total into dil
    	mov  	sil, byte[no2]		;move no2 into sil
    	call	division		      ;call division function
    	jmp	  second			      ;when done jump to second
second:	
    	mov	  byte[result], al	
    	cmp	  byte[opp2], '+'		;compare op2 to '+'		
    	jne	  skip21			      ;if op2 =! '+' jump to skip21
    	mov	  dil, byte[result]	;move result into dil
    	mov	  sil, byte[no3]		;move no3 into sil
    	call	addition		      ;call addition function
    	jmp	  third			        ;when done jump to third
skip21:
    	cmp	   byte[opp2], '-'		  ;compare op2 to '-'	
    	jne	   skip22			          ;if op2 =! '-' jump to skip22
    	mov	   dil, byte[result]	  ;move result into dil
    	mov  	 sil, byte[no3]		    ;move no3 into sil
    	call	subtraction		        ;call subtraction function
    	jmp	third			              ;when done jump to third
skip22:
  	cmp	  byte[opp2], '*'		      ;compare op2 to '*'			
  	jne	  skip23			            ;if op2 =! '*' jump to skip23
  	mov	  dil, byte[result]	      ;move result into dil	
  	mov	  sil, byte[no3]		      ;move no3 into sil
  	call	multiplication		      ;call multiplication function
  	jmp	third			                ;when done jump to third  
skip23:
  	cmp	  byte[opp2], '/'		      ;compare op2 to '/'				
  	mov	  dil, byte[result]	      ;move result into dil
  	mov	  sil, byte[no3]		      ;move no3 into sil
  	call	division		            ;call division function
  	jmp 	third			              ;when done jumpt to third

third: 		
  	mov	  byte[result], al	
  	cmp	  byte[opp3], '+'		      ;compare op3 to '+'		
  	jne	  skip31			            ;if op3 =! '+' jump to skip31
  	mov	  dil, byte[result]	      ;move result into dil
  	mov	  sil, byte[no4]		      ;move no4 into sil
  	call	addition		            ;call addition function
  	jmp	  fourth			            ;when done jump to fourth
skip31:
  	cmp	  byte[opp3], '-'		      ;compare op3 to '-'	
  	jne	  skip32			            ;if op3 =! '-' jump to skip32
  	mov	  dil, byte[result]	      ;move result into dil
  	mov	  sil, byte[no4]		      ;move no4 into sil
  	call	subtraction		          ;call subtraction function
  	jmp	  fourth			            ;when done jump to fourth
skip32:
  	cmp	  byte[opp3], '*'		      ;compare op3 to '*'		
  	jne	  skip33			            ;if op3 =! '*' jump to skip33
  	mov	  dil, byte[result]	      ;move result into dil
  	mov	  sil, byte[no4]		      ;move no4 into sil
  	call	multiplication		      ;call multiplication function
  	jmp	  fourth			            ;when done jump to fourth
skip33:
  	cmp	  byte[opp3], '/'		      ;compare op3 to '/'			
  	mov	  dil, byte[result]	      ;move result into dil
  	mov	  sil, byte[no4]		      ;move no4 into sil
  	call	division		            ;call division function
  	jmp	  fourth			            ;when done jump to fourth
	
fourth:		
  	mov	byte[result], al	
  	cmp	byte[opp4], '+'		        ;compare op4 to '+'		
  	jne	skip41			              ;if op4 =! '+' jump to skip41
  	mov	dil, byte[result]	        ;move result into sil
  	mov	sil, byte[no5]		        ;move no5 into dil
  	call	addition		            ;call addition function
	
skip41:
  	cmp	  byte[opp4], '-'		;compare op4 to '-'
  	jne	  skip42		      	;if op4 =! '-' jump to skip42
  	mov	  dil, byte[result]	;move result into dil
  	mov	  sil, byte[no5]		;move result into sil
  	call	subtraction	    	;call subtraction functon
  	
skip42:
	cmp	  byte[opp4], '*'		;compare op4 to '*'		
	jne	  skip43		       	;if op4 =! '*' jump to skip43
	mov	  dil, byte[result]	;move result into dil
	mov	  sil, byte[no5]		;move no5 into sil
	call	multiplication		;call multiplication fuction
			
skip43:
	cmp	  byte[opp4], '/'		;compare op4 to '/'		
	mov	  dil, byte[result]	;move result into dil
	mov	  sil, byte[no5]		;move no5 into sil
	call	division		      ;call division function


printResult:
  	mov	  rdi, result				;rdi = address of result
  	mov	  rsi, ascii				;rsi = address of ascii
  	call	tostring
  	
  	print	buffer, 9				;cout << buffer
  	print	equal, 3 				;cout << equal
  	print	ascii, 10				;cout << ascii
done:
    mov     rax, SYS_exit				  ;terminate excuting process
    mov     rdi, EXIT_SUCCESS			;exit status
    syscall			            			;calling system services

addition:						; Lines 223-224: Performs addition
  	mov	  al, dil 			
  	add	  al, sil				
  	mov	  byte[result], al	; Updates value of total
  	ret				              ; Returns back to line prior to calling
	
subtraction:				; Lines 214-218: Performs subtraction
  	mov	  al, dil 			
  	sub	  al, sil				
  	mov	  byte[result], al	; Updates value of total
  	ret				              ; Returns back to line prior to calling

multiplication:				; Lines 220-224: Performs multiplication
  	mov	  al, dil 			
  	mul	  sil				
  	mov	  byte[result], al	; Updates value of total
  	ret		              		; Returns back to line prior to calling
	
division:				; Lines 226-230: Performs division
  	mov	  al, dil 			
  	div	  sil				
  	mov	  byte[result], al	; Updates value of total
  	ret				              ; Returns back to place prior to calling

;converts result into ascii
tostring:
	;Part A - Successive division
	movzx   ax, byte[rdi] 			
	mov 	  rcx, 0 					
	mov 	  bx, 10 		;set for dividing by 10			
divideLoop:
	mov 	  dx, 0
	div 	  bx 		  ;divide number by 10				
	push 	  rdx 		;push remainder		
	inc 	  rcx 					
	cmp 	  ax, 0 					
	jne 	  divideLoop 				

	;Part B - Convert remainders and store
	mov 	  rbx, rsi	;get address of rsi			
	mov	    rdi, 0 		;rdi = 0			
popLoop:
	pop 	  rax 					
	add	    al,"0"				
	mov 	   byte [rbx+rdi], al 			
	inc 	  rdi 					
	loop 	  popLoop 
	mov	    byte[rbx+rdi], 10				
	ret
	
