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
%Y-axis (Making even vector size )
a=reshape(Feature_vector,6,6)
%rearranging the rows to make first three rows as Violin
Y=a([1 2 5 3 4 6],:);
%Plotting the feature vector with legend
scatter(X,Y(1,:),10,'s','MarkerFaceColor', 'red'); hold on;
scatter(X,Y(5,:),10,'c','MarkerFaceColor','blue'); hold on;
scatter(X,Y(2,:),10,'s','MarkerFaceColor', 'red');hold on;
scatter(X,Y(3,:),10,'s','MarkerFaceColor','red'); hold on;
scatter(X,Y(4,:),10,'c','MarkerFaceColor','blue');hold on;
scatter(X,Y(6,:),10,'c','MarkerFaceColor','blue');
xlabel('Visual Word index');
ylabel('Normalized Cross Corelation');
title("Feature Vector");
legend('Violin','Guitar', 'location','northeast');