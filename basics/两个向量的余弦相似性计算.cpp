#include<iostream>
#include<math.h>
using namespace std;
double mycosine(int* arrayA,int* arrayB,int length){
    if(!arrayA||!arrayB) return 0;
    double sumarrayA=0,sumarrayB=0;
    double cosine=0;
    for(int i=0;i<length;i++){
        sumarrayA+=arrayA[i]*arrayA[i];
        sumarrayB+=arrayB[i]*arrayB[i];
        cosine+=arrayA[i]*arrayB[i];
    }
    sumarrayA=sqrt(sumarrayA);
    sumarrayB=sqrt(sumarrayB);
    if((sumarrayA-0<0.0001)||(sumarrayB-0<0.0001)){
        return 0;
    }
    cosine/=(sumarrayA*sumarrayB);
    return cosine;
}

int main(){
    int length;
    cin>>length;
    int* arrayA=new int[length];
    int* arrayB=new int[length];
    char tag='y';
    while(tag == 'y'){
        for(int i=0;i<length;i++){
            cin>>arrayA[i];
        }
        for(int i=0;i<length;i++){
            cin>>arrayB[i];
        }
        cout<<mycosine(arrayA,arrayB,length)<<endl;
        cin>>tag;
    }
}