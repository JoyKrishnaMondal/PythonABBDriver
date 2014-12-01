MODULE MainModule
	PERS robtarget p20;
	PROC main()

		p20 := CRobT();
		p20 := Offs(0,0,0);
		MOVEL p20,v10,z100,tool0;

	ENDPROC
ENDMODULE