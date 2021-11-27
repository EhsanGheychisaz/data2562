#includ<iostream>
using namespace std;

int main()
{
    int time,t;
    cin>>t;
    int x[t];
    int y[t];

    for(int i=0;i<t;i++)
    {
        cin>>x[i]>>y[i];
    }

    for (int i=0;i<t;i++)
    {
        if(x[i]==y[i])
        {
            if(x[i]%2==0) time=2*x[i];

            else time=2*x[i]-1;

            cout<<time<<endl;
        }

        else if(y[i]==x[i]-2)
        {
            if(x[i]%2==0) time=x[i]+y[i];

            else time=2*x[i]-3;

            cout<<time<<endl;
        }

        else
            cout<<"-1"<<endl;
    }


    return 0;
}
