marksheet=[]
scorelist=[]
if __name__ == '__main__':
        for _ in range(int(input())):
                name = input()
                score = float(input())
                marksheet+=[[name,score]]
                scorelist+=[score]
        b=sorted(list(set(scorelist)))[1] #sort karege scoresheet ko and phir usko set me dalege isse kya hoga ki numbers repeat nhi hoga. and [1] jo hai wo second lowest score dega.

        for a,c in sorted(marksheet):
             if c==b:
                    print(a)

#ye idar nhi site pe chaelga
                     
