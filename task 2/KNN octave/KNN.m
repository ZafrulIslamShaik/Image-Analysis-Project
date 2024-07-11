close all;
clear all;
%feature vector extracted from task 1
Feature_vector=[0.9765759009496094
0.9434142192908879
0.9706744310100839
0.921644450356053
0.953700099793419
0.9598625686326585
0.972870957745455
0.9411536222502908
0.9748753435652696
0.9252713717314319
0.9447707643502927
0.9501041976937845
0.9702119342433213
0.9463605095024065
0.9785818010617313
0.921883392412825
0.9540926835733039
0.9574170293974006
0.9680525353056187
0.9411297770376515
0.9746518388727781
0.9326989190039723
0.9493836414108896
0.9654802136990205
0.9675863150764341
0.9405637151971145
0.9724716636262695
0.8980857864158507
0.9466190639423734
0.938526359258671
0.974962865815436
0.9406060873316718
0.9764689024435197
0.9324602858542445
0.9440927638261646
0.9639472593627063]
X=[ 1 2 3 4 5 6];
%reshaping the feature vector for size 6X6
a=reshape(Feature_vector,6,6);

%trained data
Y= a([1 2 3 4], :);

Violin = a([1 2],:);
Guitar =a([3 4],:);
%test data
Z1 =a([5],:); %violin feature vector for testing
Z2 =a([6],:); %Guitar feature vector for testing
s=input("enter the test data feature vector 1 or 2 ")

Ecludian_dis=[];
if s==1
  Ecludian_dis =[];
for i=1:size(Y,1) %all rows of training set
  for j=1:size(Y,2)%all column of training set
    for k= 1:size(Z1,2);%all column of test set

 value=sqrt((Z1(1,k)-Y(i,j))^2+ (k -j)^2) ; %ecludian distance
 Ecludian_dis= [Ecludian_dis; value]; %storing Ecludian distances for all points
end
end
end

else
for i=1:size(Y,1) %all rows of training set
  for j=1:size(Y,2)%all column of training set
    for k= 1:size(Z2,2);%all column of test set

 value=sqrt((Z2(1,k)-Y(i,j))^2+ (k -j)^2) ; %ecludian distance
 Ecludian_dis= [Ecludian_dis; value]; %storing Ecludian distances for all points
end
end
end
end
Ecludian_dis
size(Ecludian_dis)
[M,I]=min(Ecludian_dis); %index of min distance K=1
d1=I
Ecludian_dis(I,:)=[];
[M,I]=min(Ecludian_dis); %index of min distance K=2
d2=I
Ecludian_dis(I,:)=[];
[M,I]=min(Ecludian_dis);%index of min distance K=3
d3=I
if d1<=72
  d1=1;
else
  d1=4;
end
if d2<=72
  d2=1;
else
  d2=4;
end
if d3<=72
  d3=1;
else
  d3=4;
end

sum_d=d1+d2+d3;
if sum_d<=6
imshow('1.jpg'); title("Violin")
else
imshow('3.jpg');title("Guitar")
end

