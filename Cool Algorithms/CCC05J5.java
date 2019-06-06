import java.io.BufferedReader; 
import java.io.IOException; 
import java.io.InputStreamReader; 
import java.util.*;
public class CCC05J5 {
	public static boolean monkeyCheck(String word) {
		if (word.charAt(0) == 'A') {
			word = word.substring(1);
			if (word.equals("")) 
				return true;
			if (word.charAt(0) == 'N') {
				word = word.substring(1);
				return monkeyCheck(word);
			}
			return false;
		}
		if (word.charAt(0)=='B' && word.contains("S")) {
			Deque<String> stack = new ArrayDeque<String>();
			stack.push("B");
			int counter = 0;
			while (stack.size() != 0) {
				counter += 1;
				if (word.charAt(counter)=='B')
					stack.push("B");
				else if (word.charAt(counter) == 'S')
					stack.pop();
			}
			if (counter == word.length()-1) {
				if (counter == 1)
					return false;
				return monkeyCheck(word.substring(1,counter));
			}
			if (word.charAt(counter+1)!='N')
				return false;
			return monkeyCheck(word.substring(1,counter)) && monkeyCheck(word.substring(counter+2));
			
		}
		return false;
	}
	public static void main(String[] args) throws IOException {
		BufferedReader bi = new BufferedReader(new InputStreamReader(System.in));
		String word = bi.readLine();
		while (!word.equals("X")) {
			System.out.println(monkeyCheck(word) ? "YES":"NO");
			word = bi.readLine();
		}
	}
}
