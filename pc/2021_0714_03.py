# -*- coding: utf-8 -*-


    #%%

xxx=str(input("請輸入你學習的課程:  \t "));
yyy={"python":"201","java":"301","javascript":"401"};


 
if xxx    in yyy:
    print("教室是 %s " % yyy[xxx]);

    
else:
    print("來喔，再確認一下");
    print("是否有這三個課程\t python \t java\t  javascript \t");

    xxx1=str(input("請輸入你學習的課程:  \t "));

    if xxx1    in yyy:
        print("教室是 %s " % yyy[xxx1]);
    else:
    
        print("確認後，今天真的沒有課歐");
    #%%
    