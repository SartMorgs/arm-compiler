
				variavel 	EQU 	0x200 			; Define uma valor para um label ou um endereço para este label.
				...
				...
		
	
				AREA main, CODE, READONLY
	
main			PROC								; Inicio do programa principal.
				...
				BL	func							; Aqui é feita uma chamada de função (func).
				...
				...
				B	main										
													; Fim da área de programa.		
		
func			PROC								; Código da função.
				...
				...
				ENDP								; Indica fim da função.
		
				...
				...
				...
		
		
		
INT0_Handler	PROC								; Formato das Interrupções. Sempre usar diretiva Handler.
				..
				..
				ENDP

				
				END
				
				
	