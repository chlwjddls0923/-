# experiment.py
import time
import random
from memory_profiler import profile
from ds import ArrayList, LinkedList  # 1번에서 구현한 자료구조 불러오기

def test_insert(structure, x, rng):
    start = time.perf_counter()
    for _ in range(x):
        pos = rng.randint(0, structure.size())
        structure.insert(pos, -1)  # 임의의 위치에 -1 삽입
    end = time.perf_counter()
    return end - start

@profile
def run_experiment():
    SEED = 42
    rng = random.Random(SEED)

    # 삽입 횟수(x) 변화
    x_values = [100, 1000, 5000]

    for x in x_values:
        # 초기 리스트 크기 10,000 준비
        arr = ArrayList()
        llist = LinkedList()
        for i in range(10000):
            arr.append(i)
            llist.append(i)

        # 삽입 성능 측정
        t_arr = test_insert(arr, x, rng)
        t_ll  = test_insert(llist, x, rng)

        print(f"x={x}: ArrayList={t_arr:.6f}s, LinkedList={t_ll:.6f}s")

if __name__ == "__main__":
    run_experiment()
