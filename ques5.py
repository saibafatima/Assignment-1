# Q5. Using a while loop, verify if the number A is purely divisible by number B and if so then how many
# times it can be divisible.

A = 36
B = 6
count = 0
while A % B == 0:
    A = A/B
    count +=1

print(f"A can be divided by count B {count} times")