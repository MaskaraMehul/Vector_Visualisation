clc, clearvars

fprintf("This is a simple 3d Vector Plotter and Calculator.\n\n")
i1 = input("Enter i component of vector 1: ");
j1 = input("Enter j component of vector 1: ");
k1 = input("Enter k component of vector 1: ");
i2 = input("Enter i component of vector 2: ");
j2 = input("Enter j component of vector 2: ");
k2 = input("Enter k component of vector 2: ");

origin = [0 0 0];
v1 = [i1 j1 k1];
v2 = [i2 j2 k2];

v1dotv2 = dot(v1,v2);
v1xv2 = cross(v1,v2);
v2xv1 = cross(v2,v1);
magv1 = norm(v1);
magv2 = norm(v2);
theta_rad = acos((v1dotv2)/(magv1*magv2));
theta_deg = rad2deg(theta_rad);

disp("-------------------------------")
%disp("v1 = " + v1(1) + "i + " + v1(2) + "j + " + v1(3) + "k");
%disp("v2 = " + v2(1) + "i + " + v2(2) + "j + " + v2(3) + "k\n");

fprintf("v1 = %.2fi + %.2fj + %.2fk\n", v1(1), v1(2), v1(3));
fprintf("v2 = %.2fi + %.2fj + %.2fk\n", v2(1), v2(2), v2(3));
fprintf("v1.v2 = %.2f\n", v1dotv2);
fprintf("v1 x v2 = %.2fi + %.2fj + %.2fk\n", v1xv2(1), v1xv2(2), v1xv2(3));
fprintf("v2 x v1 = %.2fi + %.2fj + %.2fk\n", v2xv1(1), v2xv1(2), v2xv1(3));
fprintf("Angle between the 2 vectors is: %.2f°\n", theta_deg)
disp("------------------------------")

quiver3(0,0,0,v1(1),v1(2),v1(3), 0);
hold on
quiver3(0, 0, 0, v2(1), v2(2), v2(3), 0);
hold on
quiver3(0, 0, 0, v1xv2(1), v1xv2(2), v1xv2(3), 0, '--');
legend("v1", "v2", "v1 x v2")
title("3-D Plot of Vector 1 and Vector 2")

xlim([-10 10])
ylim([-10 10])
zlim([-10 10])

grid on