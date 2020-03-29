# find percentage

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    list = (student_marks[query_name])
    avg = float(sum(list) / len(list))
    print(format(avg, '.2f'))
    #sum1 = sum(d[query_name] for d in int(student_marks.values()))
    #print(sum1)
