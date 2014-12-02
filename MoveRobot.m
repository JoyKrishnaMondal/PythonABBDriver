function MoveRobot(value)
 %  Value should be in the form of "0,0,0"
system(horzcat('ipy DllAccess.py ',value));

fileID = fopen('arg.txt','w');
fprintf(fileID,value);
f.close(fileID);

end