


conj(0,_,0).
conj(0,0,_).
conj(1,1,_).
conj(6,5,4).
conj(2,5,9).
conj(0,5,3).


conj(A,B,C) :- A=B,B=C; conj(A,C,B).
