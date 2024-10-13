import java.io.*;
import java.util.*;
class pconst
{
public static void pcon()
{
	String str;
	int flag=1;
	System.out.print("Enter the string :: ");
	Scanner s=new Scanner(System.in);
	str=s.nextLine();
	for (int i = 0; i < str.length(); i++) 
    	{
		if (!(str.charAt(i)>='0' && str.charAt(i)<='9'))
        	{
		flag=0;
		}
	}
	if(flag==1)
	System.out.println("Constant");
	else
	System.out.println("Not a Constant");
}
public static void main(String[] args)
{	
System.out.println("Saail Chavan KFPMSCCS016\n");
pcon();
}}

