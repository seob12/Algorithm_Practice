def generate_shift_table(pattern):
    pattern_length = len(pattern)
    shift_table = {}
    
    # 패턴의 마지막 문자를 제외한 나머지 문자에 대해 최대 이동 거리 계산
    for i in range(pattern_length - 1):
        c = pattern[i]
        shift_table[c] = pattern_length - 1 - i
    
    # 패턴에 존재하지 않는 문자에 대한 이동 거리는 패턴 길이로 설정
    shift_table.setdefault(None, pattern_length)
    
    return shift_table

def search_horspool(text, pattern):
    text_length = len(text)
    pattern_length = len(pattern)
    shift_table = generate_shift_table(pattern)
    
    i = pattern_length - 1  # 패턴의 마지막 문자 인덱스
    while i < text_length:
        j = 0
        
        # 패턴의 뒤에서부터 문자를 비교하며 일치 여부 확인
        while j < pattern_length and pattern[pattern_length - 1 - j] == text[i - j]:
            j += 1
        
        if j == pattern_length:
            return i - pattern_length + 1  # 패턴이 일치하는 위치의 시작 인덱스 반환
        else:
            c = text[i]
            i += shift_table.get(c, pattern_length)  # shift_table을 참조하여 이동 거리 결정
    
    return -1  # 패턴이 발견되지 않은 경우 -1 반환

text = "Hello, World!"
pattern = "World"

index = search_horspool(text, pattern)

if index != -1:
    print(f"패턴이 발견되었습니다. 인덱스: {index}")
else:
    print("패턴이 발견되지 않았습니다.")