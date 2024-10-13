import java.io.*;
import java.util.*;
class oper
{
public static void opr()
{
	String[] a={"+","-","/","*","<=",">=","<",">","==","!="};
	String str;
	int i,flag=0;
	System.out.println("Enter the opperator :: ");
	Scanner s=new Scanner(System.in);
	str=s.nextLine();
	for(i=0;i<a.length;i++)
	{
		boolean c=str.equals(a[i]);
		if(c){
		flag=1;
		break;
		}
		else	
		flag=0;	
	}
	if(flag==1)
	System.out.println("Operator");
	else
	System.out.println("Not an Operator");
}
public static void main(String[] args)
{
System.out.println("Saail Chavan KFPMSCCS016\n");
opr();
}
}

