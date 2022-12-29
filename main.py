hours = int(input())
minutes = int(input())
times = int(input())

wait_hours = (hours + ((times + minutes) // 60)) % 24
wait_minutes = minutes + (times % 60) % 60


print(f'{wait_hours:>02}:{wait_minutes:>02}')

# 8
# 0
# 65

# 09:05


# 10
# 15
# 2752

# 08:07
