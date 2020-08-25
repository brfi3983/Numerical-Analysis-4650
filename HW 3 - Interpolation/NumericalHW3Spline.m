<<<<<<< HEAD
w = 0.1;
b = [-0.29;-0.56;-0.814;-0.56;0;0;0;0]
b_Clamped = [-0.29;-0.56;-0.814;-0.56;-2.8004996;-2.9734038;0;0]
Nodes = [1 0 0 0 0 0 0 0;
    0 0 0 0 1 0 0 0;
    0 0 0 0 1 w w^2 w^3;
    1 w w^2 w^3 0 0 0 0];
End = [0 0 2 0 0 0 0 0;
    0 0 0 0 0 0 2 6*w];
End_Clamped = [0 1 0 0 0 0 0 0;
    0 0 0 0 0 1 2*w 3*w^2];
Connect = [0 1 2*w 3*w^2 0 -1 0 0;
    0 0 2 6*w 0 0 -2 0];
A = [Nodes; End; Connect]
A_Clamped = [Nodes; End_Clamped; Connect]

x = inv(A)*b
=======
w = 0.1;
b = [-0.29;-0.56;-0.814;-0.56;0;0;0;0]
b_Clamped = [-0.29;-0.56;-0.814;-0.56;-2.8004996;-2.9734038;0;0]
Nodes = [1 0 0 0 0 0 0 0;
    0 0 0 0 1 0 0 0;
    0 0 0 0 1 w w^2 w^3;
    1 w w^2 w^3 0 0 0 0];
End = [0 0 2 0 0 0 0 0;
    0 0 0 0 0 0 2 6*w];
End_Clamped = [0 1 0 0 0 0 0 0;
    0 0 0 0 0 1 2*w 3*w^2];
Connect = [0 1 2*w 3*w^2 0 -1 0 0;
    0 0 2 6*w 0 0 -2 0];
A = [Nodes; End; Connect]
A_Clamped = [Nodes; End_Clamped; Connect]

x = inv(A)*b
>>>>>>> df807cb4c3d48e521e288700e6b4420d69ede4c5
x_Clamped = inv(A_Clamped)*b_Clamped