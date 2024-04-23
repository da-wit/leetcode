def split_and_join(line):
    # write your code here
    val = line.split()
    result = "-".join(val)
    return result

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)