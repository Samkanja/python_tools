import itertools

def main() -> None:
    for i in itertools.count(10):
        print(i)
        if i == 15:
            break
        



if __name__ == '__main__':
    main()