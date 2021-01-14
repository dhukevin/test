    #include<stdio.h>
    #include<stdint.h>
    #include<assert.h>
    #include "fun.c"
    int main(int argc,char* argv[])
    {
        int a = -123;
        int b = a /10;
        printf("%d" , b);
        int i;

        for(i = 0 ; i <23 ; i++)
        {
            printf("%d" , i);
        }

        i = 2;
        #if 0
        printf("a" 
                "b%d%d%d" , 1,
                2,
                3);
        #endif
    }
