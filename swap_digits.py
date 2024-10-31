def swap_digits(input_scores):
    # 對每個分數進行十位數和個位數的對調
    swapped_scores = []
    
    for score in input_scores:
        # 將分數轉換為字符串，進行反轉
        swapped_score = int(str(score)[::-1])  # 反轉字符串並轉回整數
        swapped_scores.append(swapped_score)
        
    return swapped_scores

# 測試函數
input_scores = [35, 46, 57, 91, 29]
output_scores = swap_digits(input_scores)
print(output_scores)