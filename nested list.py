records=[]
marks=set()
ln=[] # 2nd lowest marks name
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
for name,score in records:
    marks.add(score)
lm=sorted(marks)[1] #lowest marks
for name,score in records:
    if lm==score:
        ln.append(name)
for name in sorted(ln):
    print(name)
