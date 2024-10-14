import time

def main():
    array1, array2, array3 = [10, 20, 30], [20, 10, 30], [40, 40, 10]

    t1 = time.time() * 1000
    for _ in range(10000000):
        sum_val = sum(array1) + sum(array2) + sum(array3)
        if sum_val != 210: print(False)
    t2 = time.time() * 1000

    for _ in range(10000000):
        sum_val = sum(array1[i] + array2[i] + array3[i] for i in range(len(array1)))
        if sum_val != 210: print(False)
    t3 = time.time() * 1000

    print("Saail Chavan KFPMSCCS016")
    print("Before loop jamming ---->", int(t2 - t1), "ms")
    print("After loop jamming ---->", int(t3 - t2), "ms")

if __name__ == "__main__":
    main()
