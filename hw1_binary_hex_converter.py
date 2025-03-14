def convert_numbers():
    try:
        # 輸入十進位數字
        decimal_number = int(input("請輸入一個十進位數字: "))
        
        # 轉換為二進位
        binary_number = bin(decimal_number)
        
        # 轉換為十六進位
        hexadecimal_number = hex(decimal_number)
        
        # 輸出結果
        print(f"十進位: {decimal_number}")
        print(f"二進位: {binary_number}")
        print(f"十六進位: {hexadecimal_number}")
    
    except ValueError:
        print("請輸入有效的十進位數字！")

# 執行函數
convert_numbers()