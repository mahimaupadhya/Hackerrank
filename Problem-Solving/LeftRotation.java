import java.util.*;
import java.util.Scanner;

public class Solution{
    public static void main(String args[])
    {
    int n; int d;
    Scanner sc= new Scanner(System.in);
    n= sc.nextInt();
    d=sc.nextInt();
    int []a=new int[n];
    for(int i=0;i<n;i++)
    {
        a[i]=sc.nextInt();
    }
    reverse(a,0,d-1);
    reverse(a,d,n-1);
    reverse(a,0,n-1);
    for(int i=0;i<n;i++)
        {
            System.out.print(a[i]+" ");
        }
    }
    static void reverse(int []arr, int start,int end)
    {
        while(start<end)
        {
            int temp=arr[start];
            arr[start]=arr[end];
            arr[end]=temp;
            start++;
            end--;
        }
    }

    


}
