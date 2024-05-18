# AC10 - beecrowd 1258
aux=False

while True:
    n=int(input())
    if n==0:break
    d=dict()
    
    for i in range(n):
        nome=input()
        x=input().split()
        x.append(nome)
        d[i]=x
    d=dict(sorted(d.items(),key=lambda x: x[1][2]))
    d=dict(sorted(d.items(),key=lambda x: x[1][1],reverse=True))
    d=dict(sorted(d.items(),key=lambda x: x[1][0]))
    if aux:print()
   
    for i,j in d.items():
        print(*j,sep=" ")
    aux=True

# AC10 - beecrowd 1260
def process_cases(test_cases):
    results = []
    
    for case in test_cases:
        tree_counts = {}
        total_trees = 0
        
        for tree in case:
            if tree in tree_counts:
                tree_counts[tree] += 1
            else:
                tree_counts[tree] = 1
            total_trees += 1
        
        sorted_species = sorted(tree_counts.keys())
        
        case_result = []
        for species in sorted_species:
            percentage = (tree_counts[species] / total_trees) * 100
            case_result.append(f"{species} {percentage:.4f}")
        
        results.append(case_result)
    
    return results


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split("\n")
    
    num_cases = int(data[0])
    cases = []
    
    current_case = []
    for line in data[2:]:
        if line.strip() == "":
            if current_case:
                cases.append(current_case)
                current_case = []
        else:
            current_case.append(line.strip())
    
    if current_case:
        cases.append(current_case)
    
    results = process_cases(cases)
    
    for i, result in enumerate(results):
        for line in result:
            print(line)
        if i < len(results) - 1:
            print("")


if __name__ == "__main__":
    main()

# AC10 - beecrowd 2518
import math
while True:
    try:
        deg = int(input())
        h, c, l = input().split()

        hip = math.sqrt((int(c)**2)+(int(h)**2))
        hip *= (int(l)/100*int(deg))/100
        print('%.4f'%hip)

    except EOFError:
        break
