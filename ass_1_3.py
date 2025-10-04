import sys

def stack():
    input = sys.stdin.readline
    t = int(input().strip())
    out = []
    for _ in range(t):
        s = input().rstrip("\n")
        left, right = [], []
        for ch in s:
            if ch == '-':
                if left: left.pop()
            elif ch == '<':
                if left: right.append(left.pop())
            elif ch == '>':
                if right: left.append(right.pop())
            else:
                left.append(ch)
        out.append(''.join(left) + ''.join(reversed(right)))
    print('\n'.join(out))

if __name__ == "__main__":
    stack()

'''
- 더 생각해보기: 스택 개념을 사용하지 않고, 일반 리스트에서 중간 삽입/삭제 방식으
로 구현한다면 어떤 성능의 차이가 발생할까

1) 일반 리스트(list.insert(i, x), list.pop(i))로 구현할 경우
  - 리스트는 연속된 메모리 구조 → 중간에 삽입/삭제 시 뒤쪽 원소를 한 칸씩 밀거나 당겨야 함
  - 각 연산이 O(n), 전체는 O(L²)까지 증가 가능
  - 예: 커서가 항상 문자열 중간에 있을 때 가장 비효율적

2) 2-Stack 방식과의 성능 차이
  - 2-Stack: O(L) - 모든 연산이 배열 끝에서만 발생 (push/pop은 O(1))
  - Cursor: O(L²) - splice/insert로 중간 작업 시 매번 O(L) 소요
'''