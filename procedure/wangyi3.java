import java.io.*;
import java.util.*;
public class Main
{
    public static void main(String args[])
    {
        Scanner cin = new Scanner(System.in);
        	String string = cin.nextLine();
        	for(int i=string.length();i>=0;i--){
        		String str = string.substring(0, i);
        		StringBuffer sb=new StringBuffer(str);
        		sb.reverse();
        		int n=0;
        		for(int j=0;j<str.length();j++){
        			if(str.charAt(j)==sb.charAt(j))
        				n++;
        		}
        		if(n==str.length()){
        			System.out.println(str.length());
        			break;
        		}
        	}
    }
}