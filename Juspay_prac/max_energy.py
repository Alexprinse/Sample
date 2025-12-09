from functools import lru_cache
def maximum_energy(s:str) -> int:
    s_list = list(s)
    n = len(s_list)

    def dfs(state:tuple) -> int:
        state_list = list(state)
        if 'B' not in state_list:
            return 0
        max_energy = 0
        for i , c in enumerate(state_list):
            if c != 'B':
                continue

            left = 0
            j = i - 1
            while j >= 0 and state_list[j] == 'A':
                left += 1
                j -= 1
            
            right = 0
            j = i+1

            while j < n and state_list[j] == 'A':
                right += 1
                j += 1

            if left > 0:
                new_state = state_list[:]
                new_state[i-left:i+1] = ['-']+['C'] * left
                energy = left + dfs(tuple(new_state))
                max_energy = max(max_energy,energy)

            if right > 0:
                new_state = state_list[:]
                new_state[i:i+right+1] = ['C'] * right + ['-']
                energy = right + dfs(tuple(new_state))
                max_energy = max(max_energy,energy)


            new_state = state_list[:]
            new_state[i] = '-'
            energy = dfs(tuple(new_state))
            max_energy = max(max_energy,energy)

            break

        return max_energy
    
    return (dfs(tuple(s_list)))

s1 = "AAABAAAABAA"

print(maximum_energy(s1))


            

