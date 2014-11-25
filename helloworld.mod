MODULE MainModule
	VAR string text;
	VAR num Amount := 100;
	PERS robtarget p20;

	PROC main()

	p20 := CRobT();
	p20 := Offs(p20,Amount,Amount,Amount);
	MOVEL p20,v10,z100,tool0;

	ENDPROC
ENDMODULE

