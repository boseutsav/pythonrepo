person = input('Enter person name>>')
father_of={}
father_son_pair = input('Father son pair>>\n').split()
while father_son_pair:
    father_of[father_son_pair[0]]=father_son_pair[1]
    father_son_pair = input().split()

num_grandchild = 0
for son, father in father_of.items():
    if person == father:
        num_grandchild += list(father_of.values()).count(son)
for son,father in father_of.items():
    print(f"father: {father} and son: {son}")
print(f'Grandchilren of {person} are {num_grandchild}')