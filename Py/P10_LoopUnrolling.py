import time

def main():
    array1 = [0] * 5

    t1 = time.time() * 1000
    # Version 1: Assign elements in a loop.
    for _ in range(10000000):
        for x in range(len(array1)):
            array1[x] = x
    t2 = time.time() * 1000

    # Version 2: Unroll the loop.
    for _ in range(10000000):
        array1[0], array1[1], array1[2], array1[3], array1[4] = 0, 1, 2, 3, 4
    t3 = time.time() * 1000

    print("Saail Chavan KFPMSCCS016")
    print("Time before loop unrolling: -->", int(t2 - t1), "ms")
    print("Time after loop unrolling: -->", int(t3 - t2), "ms")

if __name__ == "__main__":
    main()
