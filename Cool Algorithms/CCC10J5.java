/*
  https://dmoj.ca/src/1695367
*/
import java.util.*;
public class J5_Chess {
    public static ArrayList<int[]> poss(int[] loc){
        ArrayList<int[]> locations = new ArrayList<>();
        int[] temp = new int[2];
        if (loc[0] - 2 > 0){
            temp[0] = loc[0] - 2;
            if (loc[1] - 1 > 0) {
                temp[1] = loc[1] - 1;
                locations.add(temp.clone());
            }
            if (loc[1] + 1 < 9) {
                temp[1] = loc[1] + 1;
                locations.add(temp.clone());
            }
        }
        if (loc[0] - 1 > 0){
            temp[0] = loc[0] - 1;
            if (loc[1] - 2 > 0) {
                temp[1] = loc[1] - 2;
                locations.add(temp.clone());
            }
            if (loc[1] + 2 < 9) {
                temp[1] = loc[1] + 2;
                locations.add(temp.clone());
            }
        }
        if (loc[0] + 2 > 0){
            temp[0] = loc[0] + 2;
            if (loc[1] - 1 > 0) {
                temp[1] = loc[1] - 1;
                locations.add(temp.clone());
            }
            if (loc[1] + 1 < 9) {
                temp[1] = loc[1] + 1;
                locations.add(temp.clone());
            }
        }
        if (loc[0] + 1 > 0){
            temp[0] = loc[0] + 1;
            if (loc[1] - 2 > 0) {
                temp[1] = loc[1] - 2;
                locations.add(temp.clone());
            }
            if (loc[1] + 2 < 9) {
                temp[1] = loc[1] + 2;
                locations.add(temp.clone());
            }
        }
        return locations;
    }

    public static void main(String[] args){
       Scanner scan = new Scanner(System.in);
       String[] temp = scan.nextLine().split(" ");
        int size = temp.length;
        int [] start = new int [size];
        for(int i=0; i<size; i++) {
            start[i] = Integer.parseInt(temp[i]);
        }
        temp = scan.nextLine().split(" ");
        size = temp.length;
        int [] end = new int [size];
        for(int i=0; i<size; i++) {
            end[i] = Integer.parseInt(temp[i]);
        }
        Queue<int[]> queue = new LinkedList<>();
        ArrayList<int[]> possibilities = poss(start);
        for (int i = 0; i < possibilities.size(); i++) {
            queue.add(possibilities.get(i));
        }
        int distance = 1;
        int counter = queue.size();
        boolean found = false;
        if (end[0] == start[0] && end[1] == start[1]) {
            System.out.println(0);
        } else {
            while (!found) {
                if (counter == 0) {
                    counter = queue.size();
                    distance++;
                }
                int[] loc = queue.remove();
                if (loc[0] == end[0] && loc[1] == end[1]) {
                    found = true;
                } else {
                    possibilities = poss(loc);
                    for (int i = 0; i < possibilities.size(); i++) {
                        queue.add(possibilities.get(i));
                    }
                }
                counter--;
            }
            System.out.println(distance);
        }
    }
}
