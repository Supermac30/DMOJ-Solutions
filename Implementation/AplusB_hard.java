/*
	https://dmoj.ca/problem/aplusb2
*/
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
public class AplusB_hard {
	public static String add(String inp0, String inp1) {
		while (inp0.length()<inp1.length())
			inp0 = "0" + inp0;
		while (inp0.length()>inp1.length())
			inp1 = "0" + inp1;
		String a[]  = inp0.split("");
		String b[] = inp1.split("");
		int carry = 0;
		String answer[] = new String[inp0.length()+1]; 
		for (int i = inp0.length()-1; i >=0;i--) {
			int add = Integer.parseInt(a[i])+Integer.parseInt(b[i])+carry;
			answer[i+1] = Integer.toString(add%10);
			carry = add/10;
		}
		if (carry != 0) {
			answer[0] = Integer.toString(carry);
			return String.join("", answer);
		}
		String answer0[] = Arrays.copyOfRange(answer,1,answer.length); 
		return String.join("", answer0);
		
	}
	public static String sub(String inp0, String inp1) {
		boolean isNegative = false;
		if (inp0.compareTo(inp1)==0)
			return "0";
		if (inp0.length() < inp1.length() || inp0.length() == inp1.length() && inp0.compareTo(inp1) <0) {
			isNegative = true;
			String temp = inp0;
			inp0 = inp1;
			inp1 = temp;
		}
		while (inp0.length()<inp1.length())
			inp0 = "0" + inp0;
		while (inp0.length()>inp1.length())
			inp1 = "0" + inp1;
		String a[]  = inp0.split("");
		String b[] = inp1.split("");
		int carry = 0;
		String answer[] = new String[inp0.length()];
		for (int i = inp0.length()-1; i >=0;i--) {
			int add = Integer.parseInt(a[i])-Integer.parseInt(b[i])+carry;
			if (add<0) {
				if (add == -10) {
					answer[i] = "0";
					carry= -1;
				}
				else {
					answer[i] = Integer.toString(10+(add%10));
					carry = -1;
				}
			}
			else {
				answer[i] = Integer.toString(add%10);
				carry = 0;
			}
		}
		int counter = 0;
		for (String num:answer) {
			if (num.equals("0"))
				++counter; 
			else
				break;
		}
		String fixed[] = Arrays.copyOfRange(answer,counter,answer.length);
		if (isNegative)
			return "-"+String.join("", fixed);
		return String.join("", fixed);
	}
	public static void main(String[] args) throws IOException {
		BufferedReader bi = new BufferedReader(new InputStreamReader(System.in));
		int length = Integer.parseInt(bi.readLine());
		for (int i = 0; i<length;i++) {
			String inp[] = bi.readLine().split(" ");
			if (inp[0].charAt(0) =='-' && inp[1].charAt(0) == '-') 
				System.out.println("-"+add(inp[0].substring(1),inp[1].substring(1)));
			else if (inp[0].charAt(0) !='-' && inp[1].charAt(0) != '-') 
				System.out.println(add(inp[0],inp[1]));
			else if (inp[0].charAt(0) =='-' && inp[1].charAt(0) != '-') 
				System.out.println(sub(inp[1],inp[0].substring(1)));
			else
				System.out.println(sub(inp[0],inp[1].substring(1)));
			
		}
	}
}
