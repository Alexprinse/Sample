from functools import lru_cache

def get_max_energy_optimized(s: str) -> int:
    s_list = list(s)
    n = len(s_list)

    @lru_cache(maxsize=None)
    def dfs(state: tuple) -> int:

        state_list = list(state)
        if 'B' not in state_list:
            return 0  # No more B's to process

        max_energy = 0
        for i, c in enumerate(state_list):
            if c != 'B':
                continue

            left_count = 0
            j = i - 1
            while j >= 0 and state_list[j] == 'A':
                left_count += 1
                j -= 1

            right_count = 0
            j = i + 1
            while j < n and state_list[j] == 'A':
                right_count += 1
                j += 1

            if left_count > 0:
                new_state = state_list[:]
                new_state[i - left_count:i + 1] = ['-'] + ['C'] * left_count
                energy = left_count + dfs(tuple(new_state))
                max_energy = max(max_energy, energy)

            if right_count > 0:
                new_state = state_list[:]
                new_state[i:i + right_count + 1] = ['C'] * right_count + ['-']
                energy = right_count + dfs(tuple(new_state))
                max_energy = max(max_energy, energy)

            new_state = state_list[:]
            new_state[i] = '-'
            energy = dfs(tuple(new_state))
            max_energy = max(max_energy, energy)

            break 

        return max_energy

    return dfs(tuple(s_list))

s1 = "AAAABAAAAABAAAA"


print(get_max_energy_optimized(s1))