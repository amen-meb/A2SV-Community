if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    unique_scores = set(arr)
    
    sorted_scores = sorted(unique_scores, reverse=True)
    
    runner_up_score = sorted_scores[1]
    
    print(runner_up_score)
