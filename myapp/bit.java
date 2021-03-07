public class bit
{
   static int get(int arr[])
    {
        int ones=0;
        int twos=0;
        int comman;
        for(int i=0;i<4;i++)
        {
            twos=twos | (ones & arr[i]);
            ones=ones ^ arr[i];
            comman=~(ones & twos);
            ones &= comman;
            twos &= comman;
            return ones;

        }
    }
    public static void main(String[] args) {
        int arr[]={3,1,3,3};
        System.out.println(get(arr));
    }
}