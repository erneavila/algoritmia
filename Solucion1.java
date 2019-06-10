/* THEME: PROBLEMA 1
 * AUTHOR: EAH
 * DATE: JUN-09-2019
 */

import java.util.Scanner;

public class Solucion1 {
	
	private static int num1;
	private static int num2;
	
	public static int SecuenciaDeNumeros() {
		
		if(num1 < num2) { 
			System.out.print("Secuencia ascendente iniciada: ");
			for( int i = num1; i <= num2;i++ ) { System.out.print( i + " " ); }
		}else { 
			System.out.print("Secuencia descendente iniciada: ");
			for( int i = num1; i >= num2;i-- ) { System.out.print( i + " " ); }
		}
		
		return  0;
	}
	
	public static void main(String[] args) {
		
		Scanner scanner = new Scanner(System.in);
		System.out.print("Primer numero: ");
		num1 = scanner.nextInt();
		System.out.print("Segundo numero: ");
		num2 = scanner.nextInt();

		SecuenciaDeNumeros();

	}	
}
