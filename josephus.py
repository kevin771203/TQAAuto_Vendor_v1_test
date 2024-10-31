def josephus(n):
    # 初始化人員列表
    people = list(range(1, n + 1))
    index = 0  # 記錄當前報數的位置

    # 當列表中還有多於一個人時，持續進行
    while len(people) > 1:
        index = (index + 2) % len(people)  # 報數到3，因為數字從0開始，所以加2
        people.pop(index)  # 移除報到3的人

    return people[0]  # 返回最後剩下的人的順位


while True:
    try:
        n = int(input("請輸入人數 n (1-100): "))
        if 1 <= n <= 100:
            last_person = josephus(n)
            print(f"最後留下的同事是第 {last_person} 順位")
            break  # 如果輸入有效，則退出循環
        else:
            print("請輸入有效的人數 (1-100)")
    except ValueError:
        print("請輸入有效的整數！")  # 處理非整數輸入
