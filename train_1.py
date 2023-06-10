def GC_content():
    """
    1. 서열 세 개를 입력받고 변수에 저장한다.
       seq a = input()
       seq b = input()
       seq c = input() 
    2. 그 서열들의 GC 함량을 계산한다.  
       GC 함량 = (G 개수 + C 개수)/ length(seq)
    """
    seq_a = str(input("seq a:"))
    seq_b = str(input("seq b:"))  
    seq_c = str(input("seq c:"))

    # .count() 
    print(f"seq a 함량 : {((seq_a.count('C') + seq_a.count('G')) / len(seq_a)) * 100}%")
    print(f"seq b 함량 : {(seq_b.count('C') + seq_b.count ('G')) / len(seq_b)}")
    print(f"seq c 함량 : {(seq_c.count('C') + seq_c.count('G')) / len(seq_c)}")
    return 0 


def main():
    GC_content()
    return 0

main()
