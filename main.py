
chestsAmount = 80
N = chestsAmount

n = 1

while n <= chestsAmount:
    unopenedChests = chestsAmount - n
    if unopenedChests <= n:
        totalStudents = n
    else:
        totalStudents = n + (unopenedChests - n)
    if totalStudents < N:
        N = totalStudents
    n = n + 1

print(N)