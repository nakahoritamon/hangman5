def hungman(letter):
    print("Let's start hungman!!")
    stage=[
           "  _____",
           " |     |",
           " |     o",
           " |    /|>",
           " |    /|",
           " |",
           ""]
    bar=list("_"*len(letter))
    value=list(letter)
    miss=0
    win=False
    
    while miss<len(stage):
        print(bar)
        i=input("アルファベットを一文字入力してください。")
        if i in value:
            k=letter.index(i)
            bar[k]=i
            value[k]="?"
            print('正解です！！')

        else:
            miss+=1
            print("\n".join(stage[0:miss]))

        if not "_" in bar:
            win=True
            break

    if win==True:
        print('正解！！')

    else:
        print('GAME OVER!!')
    x=input('continue:y/n')
    if x=="y":
        hungman(letter)
      

hungman("cat")
