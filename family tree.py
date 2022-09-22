parent( pam, bob).
parent( tom, bob).
parent( tom, liz).
parent( bob, jim).
parent( pat, bob).
parent( ann, tom).
parent( ann, pam).
parent( pat, liz).
parent( pat, pam).

female( pam).
female( liz).
female( ann).
female( pat).
male( tom).
male( bob).
male( jim).

offspring( Y, X)  :-
   parent( X, Y).
mother( X, Y)  :-
   parent( X, Y),
   female( X).
father( X, Y)  :-
   parent( X, Y),
   male( X).

grandparent( X, Z)  :-
   parent( X, Y),
   parent( Y, Z).
   
grandfather( X, Z)  :-
   father( X, Y),
   parent( Y, Z).
   
sister( X, Y)  :-
   parent( Z, X),
   parent( Z, Y),
   female( X),
   X \= Y.

predecessor( X, Z)  :-   % Rule pr1
   parent( X, Z).

predecessor( X, Z)  :-   % Rule pr2
   parent( X, Y),
   predecessor( Y, Z).
