def bunbetu(money):
    kingaku=int(money)
    if kingaku>=500:
        print('500円玉',kingaku//500,'枚')
        kingaku=kingaku-kingaku//500*500   #kingakuから1行上の分引く
    if kingaku>=100:
        print('100円玉',kingaku//100,'枚')
        kingaku=kingaku-kingaku//100*100
    if kingaku>=50:
        print('50円玉',kingaku//50,'枚')
        kingaku=kingaku-kingaku//50*50
    if kingaku>=10:
        print('10円玉',kingaku//10,'枚')
        kingaku=kingaku-kingaku//10*10
    if kingaku>=5:
        print('5円玉',kingaku//5,'枚')
        kingaku=kingaku-kingaku//5*5
    if kingaku>=1:
        print('1円玉',kingaku//1,'枚') 

okane=input('お金を入れてください コーラ200円　コーヒー150円　水100円')
if okane.isdigit():
    kingaku=int(okane)
    if   kingaku>= 200:
        sinamono=input('なにをかう? 1…コーラ　2…コーヒー　3…水　4…キャンセル')
        if sinamono.isdigit:
            syouhin=int(sinamono)
        if syouhin==1:
            print('コーラ','お釣り', kingaku-200,'円')
            bunbetu(kingaku-200)
        elif syouhin==2:
            print('コーヒー','お釣り', kingaku-150,'円')
            bunbetu(kingaku-150)
        elif syouhin==3:
            print('水','お釣り', kingaku-100,'円')
            bunbetu(kingaku-100)
        elif syouhin==4:
            print('キャンセル','お釣り',kingaku ,'円')
            bunbetu(kingaku)
        else:
            print('商品を入力してください','お釣り',kingaku ,'円')
            bunbetu(kingaku)
    elif   kingaku>= 150:
        sinamono2=input('なにをかう? 1…コーヒー　2…水　3…キャンセル')
        syouhin2=int(sinamono2)
        if syouhin2==1:
            print('コーヒー','お釣り', kingaku-150,'円')
            bunbetu(kingaku-150)
        elif syouhin2==2:
            print('水','お釣り', kingaku-100,'円')
            bunbetu(kingaku-100)
        elif syouhin2==3:
            print('キャンセル','お釣り',kingaku ,'円')
            bunbetu(kingaku)
        else:
            print('商品を入力してください','お釣り',kingaku ,'円')
            bunbetu(kingaku)
    elif   kingaku>= 100:
        sinamono3=input('なにをかう? 1…水　2…キャンセル')
        syouhin3=int(sinamono3)
        if syouhin3==1:
            print('水','お釣り', kingaku-100,'円')
            bunbetu(kingaku-100)
        elif syouhin3==2:
            print('キャンセル','お釣り',kingaku ,'円')
            bunbetu(kingaku)
        else:
            print('商品を入力してください','お釣り',kingaku ,'円')
            bunbetu(kingaku)
    else:
        print('お金が足りません','お釣り',kingaku ,'円')
        bunbetu(kingaku)
else:
    print('数値を入力してください')