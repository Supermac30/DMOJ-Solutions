/*
	https://dmoj.ca/problem/ccc07s4
*/
import java.util.*;

class node {
	int total = 0;
	int checked= 0;
	ArrayList<Integer> connections = new ArrayList<Integer>();
	ArrayList<Integer> connectedTo = new ArrayList<Integer>();
	public node(int name){
		if (name == 1){
			total = 1;
		}
	}
	public node(){
	}

}
public class CCC07S4 {
	public static boolean check(ArrayList<node> nodes){
		for (node point: nodes){
			if (point.checked != point.connectedTo.size()){
				return true;
			}
		}
		return false;
	}
	public static void main(String[] args) {
		ArrayList<node> nodes= new ArrayList<node>();
		ArrayList<Integer> names= new ArrayList<Integer>();
		Scanner scan = new Scanner(System.in);
		int end = scan.nextInt();
		int a = Integer.parseInt(scan.next());
		int b = Integer.parseInt(scan.next());
		while (a!=0){
			if (!names.contains(a)){
				nodes.add(new node(a));
				names.add(a);
			}
			if (!names.contains(b)){
				nodes.add(new node(b));
				names.add(b);
			}
			nodes.get(names.indexOf(a)).connections.add(b);
			nodes.get(names.indexOf(b)).connectedTo.add(a);
			a = Integer.parseInt(scan.next());
			b = Integer.parseInt(scan.next());
		}
		node lookAt = null;
		if (nodes.size() != 0){
			lookAt = nodes.get(names.indexOf(1));	
		}
		while (check(nodes)){
			for (int connection: lookAt.connections){
				node point = nodes.get(names.indexOf(connection));
				point.total += lookAt.total;
				point.checked++;
			}
			for (int connection: lookAt.connections){
				node point = nodes.get(names.indexOf(connection));
				if (point.checked == point.connectedTo.size()){
					lookAt = point;
				}
			}
		}
		if (nodes.size() == 0)
			System.out.println(0);
		else
			System.out.println(nodes.get(names.indexOf(end)).total);
	}
}
