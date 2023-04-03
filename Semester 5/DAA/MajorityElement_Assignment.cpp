#include<bits/stdc++.h>
#include<ctime>
#include<cstdlib>
using namespace std;

int cntFrequency(int l, int r, vector<int> arr, vector<int> &cnt){
    if(l==r){
        cnt[arr[l]]++;
        return max(cnt[0], max(cnt[1], cnt[2]));
    }
    else if(l==r-1){
        cnt[arr[l]]++;
        cnt[arr[l+1]]++;
        return max(cnt[0], max(cnt[1], cnt[2]));
    }

    int m=(l+r)/2;
    cnt[arr[m]]++;
    int lft=cntFrequency(l, m-1, arr, cnt);
    int rgt=cntFrequency(m+1, r, arr, cnt);
    return max(lft, rgt);
}

int main(){
    int size=10000;
    vector<int> arr(size);

    for(int i=0; i<size; i++){
        arr[i]=rand()%3;
    }

    vector<int> cnt={0, 0, 0}; 
    cout<<(cnt[0]==cntFrequency(0, size-1, arr, cnt)?'X':(cnt[1]==cntFrequency(0, size-1, arr, cnt)?'Y':'Z'))<<endl;
}
