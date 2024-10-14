import java.io.*;
public class DAG
{
	int i,j,k;
	int count=-1,flag=0;
	String str[]=new String[10];
	String table[][]=new String[10][10];
	public DAG()
	{
		try
		{
		 BufferedReader br=new BufferedReader(new InputStreamReader(System.in)); 
		System.out.println("Saail Chavan KFPMSCCS016\n");
		 System.out.println("Enter The Sequence of code:");
		 System.out.println("Enter q to Quit");
			for(i=0;i<str.length;i++)
			{
			  str[i]=br.readLine();
			 if(str[i].equals("q"))
			 break;
			 else
				 count++;
		
			}
			System.out.println("The Sequence of code are:");
			for(i=0;i<str.length;i++)
			{
		
			if(str[i].equals("q"))
			 break;
			 System.out.println(str[i]);
			}
		}
		catch(IOException e)
		{}
	}
	public void tablestruct()
	{
		for(i=0;i<str.length;i++)
		{
			for(j=0;j<str.length;j++)
			{
				table[i][j]="";
			}
		}
		try
		{
		for(i=0;i<=count;i++)
		{
			for(j=0;j<=count+1;j++)
			{
				if(str[i].length()==3)//D=A
				{
					if(j==0)
					table[i][j]=str[i].substring(0,1);
					if(j==1)
					table[i][j]=str[i].substring(1,2);
					if(j==2)
					table[i][j]=str[i].substring(2);
				}
				if(str[i].length()==5)//A=B+C
				{
					if(j==0)
					table[i][j]=str[i].substring(0,1);
					if(j==1)
					table[i][j]=str[i].substring(3,4);
					if(j==2)
					table[i][j]=str[i].substring(2,3);
					if(j==3)
					table[i][j]=str[i].substring(4);
				}
			}
		}
		}
		catch(NullPointerException e)
		{}
		
		for(i=0;i<=count;i++)
		{
			for(j=i+1;j<=count;j++)
			{
				if(str[i].length()==5 && str[j].length()==5)
				{
					if(str[i].substring(2,5).equals(str[j].substring(2,5)))
					{
					 table[i][0]= table[i][0].concat(","+str[j].substring(0,1)+str[j].substring(4));
					  for(k=0;k<=count;k++)
						 table[j][k]="";
					}
				}
			}
				if(str[i].length()==3)
				{

					if(i==count)
					{
						for(j=count-1;j>=0;j--)
						{
							if(str[i].substring(2,3).equals(str[j].substring(0,1)))
							{
							  table[j][0]= table[j][0].concat(","+str[i].substring(0,1));
							  for(k=0;k<=count;k++)
								table[i][k]="";
							}
						}
					}
					else
					{
						for(j=i+1;j<=count;j++)
						{
							if(str[i].substring(2,3).equals(str[j].substring(0,1)))
							{
							  table[i][0]= table[i][0].concat(","+str[j].substring(0,1));
							  for(k=0;k<=count;k++)
								table[j][k]="";
							}
						}
					}
				}
				
			}
		System.out.println();
		System.out.print("Label"+"      "+"Operator"+"  "+"Left"+"  "+"Right");
		System.out.println();
		for(i=0;i<=count;i++)
		{
			for(j=0;j<=count+1;j++)
			{
				System.out.print(table[i][j]+"\t      ");
			}
			System.out.println();
		}
	}
	public static void main(String arg[])
	{
		DAG d=new DAG();
		d.tablestruct();
	}
}
