import java.util.*;
class token
{
static boolean isValid(String str, int n)
{

	// If first character is invalid
	if (!((str.charAt(0) >= 'a' && str.charAt(0) <= 'z')
		|| (str.charAt(0)>= 'A' && str.charAt(0) <= 'Z')))
		return false;

	// Traverse the string for the rest of the characters
	for (int i = 1; i < str.length(); i++)
	{
		if (!((str.charAt(i) >= 'a' && str.charAt(i) <= 'z')
			|| (str.charAt(i) >= 'A' && str.charAt(i) <= 'Z')
			|| (str.charAt(i) >= '0' && str.charAt(i) <= '9')
			|| str.charAt(i) == '_'))
			return false;
	}

	// String is a valid identifier
	return true;
}

public static boolean opr(String str)
{
	String[] a={"+","-","/","*","<=",">=","<",">","==","!="};
	int i;
	boolean flag=false;
	for(i=0;i<a.length;i++)
	{
		boolean c=str.equals(a[i]);
		if(c)
		{
		flag=true;
		break;
		}
		else	
		flag=false;	
	}
return flag;
}


public static boolean punc(String str)
{
	String[] a={".",",",";","(",")","{","}","[","]"};
	int i;
	boolean flag=false;
	for(i=0;i<a.length;i++)
	{
		boolean c=str.equals(a[i]);
		if(c)
		{
			flag=true;
			break;
		}
		else	
		flag=false;	
	}
return flag;
}

public static boolean res(String str)
{
	String[] a={"printf","scanf","if","else","break"};
	int i;
	boolean flag=false;
	for(i=0;i<a.length;i++)
	{
		boolean c=str.equals(a[i]);
		if(c)
		{
		flag=true;
		break;
		}
		else	
		flag=false;	
	}
return flag;
}

public static boolean pcon(String str)
{
	boolean flag=true;
	for (int i = 0; i < str.length(); i++) 
    	{
		if (!(str.charAt(i)>='0' && str.charAt(i)<='9'))
        	{
		flag=false;
		}
	
	}
return flag;
}

public static void main(String args[])
{
	System.out.println("Enter a string");
	Scanner c=new Scanner(System.in);
	String str = c.nextLine();
	int n = str.length();

	if (isValid(str, n)||res(str)||punc(str)||opr(str)||pcon(str))
		System.out.println(str+" Is a Token");
	else
		System.out.println(str+" is Not a Token");
}
}