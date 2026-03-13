"""
A residential area ABC is holding an election for the neighborhood leader.
There are M candidates and N voters.
The residents are tired of candidates campaigning and canvassing for votes as in previous elections, so they introduce new rules:

- Candidates are numbered from 1 to M.
- Each voter writes exactly one candidate number on their ballot.
- The winner is the candidate with the SECOND HIGHEST number of votes.
- If no candidate has the second highest vote count, the election is cancelled.
- If multiple candidates have the same second highest number of votes, the candidate with the smallest index is chosen.

Write a program to determine the winner.

Input:
- The first line contains two integers N and M (1 < M < 10, 5 < N < 500).
- The second line contains N integers representing the ballots.
- Each value is valid (from 1 to M).

Output:
- Print the index of the winning candidate.
- If no one wins, print: NONE

For example:
- Input:
    (1)
    10 4
    2 3 1 2 3 4 1 2 3 2
    (2)
    8 4
    1 2 3 4 4 3 2 1
- Output:
    (1)
    3
    (2)
    NONE
"""

n, m = map(int, input().split())
a = list(map(int, input().split()))
d = {}

for i in a:
    if d.get(i) is None:
        d[i] = 1
    else:
        d[i] += 1

new = sorted(d, key=lambda x: (-d.get(x), x)) # sort based on (-value, key)
maxx = d[new[0]]
while len(new) > 0 and maxx == d[new[0]]:
    new.pop(0)

print(new[0] if len(new) > 0 else "NONE")