Program lesson3_Program1;

Uses Crt; {We will make use of the crt library}

Var PD, Dname, Cmodel : String;
    CostPD, TCostPD, Distance : Real; 
    {real is a decimal (described later on)}

Begin
	textbackground(brown); {background colour}
	ClrScr; {Clear screen with a brown colour. Try run the program without this..}
	TextColor(lightgreen); {text colour}
	TCostPD := 0; 
	Writeln('This program prompts you to ' +
		 'input the cost per litre of');
	Writeln('the petrol/diesel you spend in and ' +
		'the average distance you travel');
	Writeln('with your car every week. Then, ' +
		 'the computer calculates the total cost');
	Writeln('you spend in fuel every week.');
	Readkey; {program move on as soon as a key is pressed}
	ClrScr; {short for clear screen}
	GotoXy(28,3); {move to a position on the screen: x (horizontal), y (vertical)}
	Write('Diesel or Petrol? Type p or d: ');
	PD := Readkey; {as soon as a key is pressed, it is stored in the variable 'PD'}
	GotoXy(30,4);
	Write('Name Of Driver: ');
	Readln(Dname);
	GotoXy(30,5);
	Write('Car Model: ');
	Readln(Cmodel);
	GotoXy(29,6);
	Write('Cost of Diesel/Petrol: (£) ');
	Readln(CostPD);
	GotoXy(8,7);
	Writeln('Average distance you travel with ' +
		 'your car every week: (kilometres) ');
	Readln(Distance);
	ClrScr;
	GotoXy(28,3);
	Writeln('Name of Driver:',Dname);
	GotoXy(31,4); 
	Delay(500);
	Writeln('Car Model:',Cmodel);
	GotoXy(32,5); 
	Delay(500);
	Writeln('Diesel/Petrol:',PD);
	GotoXy(8,6); 
	Delay(500);
	Writeln('Average distance covered '+
		 'every week: ',Distance:1:2,'Km');
	GotoXy(25,7); 
	Delay(500);
	Writeln('Cost of ',PD,' per litre: £',CostPD:1:2,'/litre');
	Writeln; 
	Delay(500);
	Writeln;
	TCostPD := Distance * CostPD;
	GotoXy(21,10);
	Writeln('Total cost of ',PD,' per week:£',TCostPD:1:2);
	TCostPD := 0;
	GotoXy(21,12);
	Writeln('Total cost of ',PD,' per week:' +
		 '£',(Distance * CostPD):1:2);
	GotoXy(18,14);
	Writeln('Total cost of ',PD,' per week:£',Distance * CostPD);
	Readln;
End.
