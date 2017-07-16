[Question Link](https://www.careercup.com/questionthread?id=51726)

Given an instruction DBNZ, usage: DBNZ R L, means decrements R an d if R is non-zero branches to L.

Question: implement CLEAR R (sets R to 0)

Answer: 

    L: DBNZ X L

Question: implement GOTO L (jumps to L) using preview work

Answer: 

    CLEAR X
    DBNZ X L

Question: implement NEGATE X Y (make Y = -X)

Answer:

    CLEAR Y
    L1: DBNZ Y L2
    L2: DBNZ X L1
