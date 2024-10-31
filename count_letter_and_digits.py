from collections import Counter

def count_letters_and_digits(text):
    # 過濾出字母和數字
    filtered_text = ''.join(filter(str.isalnum, text.lower()))  # 將所有字母轉換為小寫
    
    # 使用 Counter 計算每個字母和數字的出現次數
    count = Counter(filtered_text)
    
    # 將結果按字母和數字的順序排列
    sorted_counts = sorted(count.items(), key=lambda x: (x[0].isdigit(), x[0]))
    
    # 輸出每個字母或數字及其出現次數
    for char, freq in sorted_counts:
        print(f"{char.upper()} {freq}")

# 測試文字
text = "Hello welcome to Cathay 60th year anniversary"
count_letters_and_digits(text)
