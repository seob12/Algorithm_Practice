from lcs import *
from exactMatching import *
from approxMatching import *
from HuffmanCodes import *

def testKMP():
    esm = ESM()
    esm.smKMP('no pain no gain', 'no')

def testHP():
    esm = ESM()
    esm.smHP('no pain no gain', 'no')

def testASM():
    asm = ApproximateMatching()
    print(asm.editDistanceDC('edasdcxzaeqwe', 'enonixcoaadkkncx'))

from heapq import heappop, heappush

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

def build_huffman_tree(text):
    # 문자 빈도수 계산
    freq_map = {}
    for char in text:
        freq_map[char] = freq_map.get(char, 0) + 1

    # 빈도수를 기준으로 최소 힙 구성
    min_heap = []
    for char, freq in freq_map.items():
        node = HuffmanNode(char, freq)
        heappush(min_heap, (freq, node))

    # Huffman 트리 구성
    while len(min_heap) > 1:
        freq1, node1 = heappop(min_heap)
        freq2, node2 = heappop(min_heap)
        merged_freq = freq1 + freq2
        merged_node = HuffmanNode(None, merged_freq)
        merged_node.left = node1
        merged_node.right = node2
        heappush(min_heap, (merged_freq, merged_node))

    # 최종 Huffman 트리 반환
    _, root = heappop(min_heap)
    return root

def build_huffman_codes(root):
    codes = {}

    def traverse(node, code):
        if node.char is not None:
            codes[node.char] = code
        else:
            traverse(node.left, code + '0')
            traverse(node.right, code + '1')

    traverse(root, '')
    return codes

def compress_text(text, codes):
    compressed_text = ''
    for char in text:
        compressed_text += codes[char]
    return compressed_text

def decompress_text(compressed_text, codes):
    decoded_text = ''
    code = ''
    for bit in compressed_text:
        code += bit
        if code in codes:
            char = codes[code]
            decoded_text += char
            code = ''
    return decoded_text

# 예제 실행
text = "Hello, World!"

# Huffman 트리 구성
root = build_huffman_tree(text)

# Huffman 코드 구성
codes = build_huffman_codes(root)

# 텍스트 압축
compressed_text = compress_text(text, codes)

# 압축된 텍스트 출력
print(f"압축된 텍스트: {compressed_text}")

# 압축 해제
decoded_text = decompress_text(compressed_text, codes)

# 압축 해제된 텍스트 출력
print(f"압축 해제된 텍스트: {decoded_text}")
  
'''if __name__ == '__main__':
    #testKMP()
    #testHP()
    #testASM()
    #testlcs()
    testhuffman()'''
        