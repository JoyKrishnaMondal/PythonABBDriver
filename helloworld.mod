MODULE MainModule
	VAR string text;
	PERS robtarget p20;

	PROC main()

	p20 := CRobT();
	p20 := Offs(p20,0,0,100);
	MOVEL p20,v10,z100,tool0;

	ENDPROC
ENDMODULE