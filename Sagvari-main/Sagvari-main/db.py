import math
t = list(map(lambda x: list(map(int, x.split("-"))),open("input.txt").read().split("\n")))

print("2. feladat")
ll = t[0][:]
ll.sort(key = lambda x: -x)
ll = ll[:10]
print(f'Az 1. sorban szereplő 10 legnagyobb szám átlaga: {sum(ll)/len(ll):0.2f}')

print("3. feladat")
t3 = t[1][:]
t3.sort(key = lambda x: x)
t3 = t3[:12]
print(f'A 2. sorban szereplő 12 legkisebb szám összege: {sum(t3)}')

print("4. feladat")
t4 = t[2][:]
for num in t4:
    if num < 7:
        t4.remove(num)
print(f'A 3. sorban szereplő 7-nél nagyobb számok maximuma: {max(t4)}')

from math import sqrt as gy
print("5. feladat")


print(f'A 4. sorban szereplő ')

print("6. feladat")
t6 = t[4][:]
t6 = filter(lambda num: num % 2 == 0,t6)
t6 = list(t6)
for i in range(len(t6)):
    t6[i] = t6[i] ** 2

print(f'Az ötödik sorban szereplő páros számok négyzeteinek összege: {sum(t6)}')


print ("7. feladat")
t7 = t
def flatten(l):
    return [item for sublist in l for item in sublist]
t7 = flatten(t7)
t7.sort(key = lambda x: -x)
t7 = t7[:17]

print(f'Az inputban szereplő összes szám közül a 17 legnagyobb szám maximuma: {min(t7)}')

'''input.txt:
53-38-81-3-75-81-33-90-74-4-99-41-2-82-5-19-10-55-68-59-93-80-85-21-77-9-95-35-92-78-11-21-40-46-4-51-68-96-48-83-32-16-32-34-20-82-46-96-68
47-64-87-57-69-99-61-85-29-91-58-13-40-98-83-53-89-47-57-27-74-82-85-6-12-33-12-9-1-47-58-32-11-50-76-13-65-60-50-87-15-35-16-86-99-88-72-71-92
82-58-4-21-4-75-9-64-27-43-5-21-49-72-59-42-55-72-8-78-78-47-24-97-14-40-23-19-82-94-97-82-68-3-27-51-63-66-46-43-65-71-11-15-69-3-6-3-39
17-38-77-7-49-90-69-98-63-83-98-61-17-85-27-13-47-33-58-86-81-63-31-11-85-4-67-87-73-29-6-87-10-60-78-72-54-21-10-93-87-33-91-41-24-8-87-7-86
20-8-81-73-99-32-51-97-76-17-61-7-39-55-13-37-52-69-71-92-34-41-43-39-26-73-9-82-17-95-11-98-59-16-88-99-69-59-57-68-78-6-31-59-39-50-39-16-17
'''