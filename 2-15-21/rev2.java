import java.util.stream.IntStream;
import java.util.stream.Collector;
import java.util.stream.Collectors;


public class rev2{

    //One line soultion, cheaty cause reverse function
    public static String solve1(String in, int a, int b){
        return in.substring(0, a) + new StringBuffer(in.substring(a, Math.min(b+1, in.length()))).reverse().toString() + in.substring(Math.min(b+1, in.length()), in.length());
    }

    //One line soultion using helish stream mapping to reverse
    public static String solve2(String in, int a, int b){
        return in.substring(0, a) + IntStream.range(0, Math.min(b,in.length()-1)-a+1).mapToObj(i -> in.substring(a, Math.min(b+1, in.length())).charAt(Math.min(b,in.length()-1)-a-i)).collect(Collector.of(StringBuilder::new, StringBuilder::append, StringBuilder::append, StringBuilder::toString)) + in.substring(Math.min(b+1, in.length()), in.length());
    }

    public static String solve(String in, int a, int b){
        int il=in.length();
        b=b>=il?il-1:b;
        return in.substring(0, a) + new StringBuffer(in.substring(a,b+1)).reverse().toString() + in.substring(b+1, il);
    }

    public static void main(String[] args){
        System.out.println(solve("codewars", 1, 5).equals("cawedors"));
        System.out.println(solve("codingIsFun", 2, 100).equals("conuFsIgnid"));
        System.out.println(solve("FunctionalProgramming", 2, 15).equals("FuargorPlanoitcnmming"));
        System.out.println(solve("abcdefghijklmnopqrstuvwxyz", 0, 20).equals("utsrqponmlkjihgfedcbavwxyz"));
        System.out.println(solve("abcdefghijklmnopqrstuvwxyz", 5, 20).equals("abcdeutsrqponmlkjihgfvwxyz"));
    }
}