    �
	        � \��9    M ���� �7z�C (�E p�A ��	�C  V�E H�A ���C     � \�9    M ���� ����C (R�E p+�zA �f&�C  R�E H+�rA �  �C    ����FLAG   SRC �  {$CLEO .cs}

//-------------MAIN---------------
0000: NOP
wait 0

0AB4: 0@ = var 777
0@ = 0

:BUYPRO1_1226
wait 0
if and
875C: not marker $1719 enabled
0@ == 0
jf @BUYPRO1_1227
$SAVE_PICKUPS_X[2] = 416.9548 
$SAVE_PICKUPS_Y[2] = 2538.813 
$SAVE_PICKUPS_Z[2] = 9.5077 
$SAVE_POINTS_X[2] = 418.0759 
$SAVE_POINTS_Y[2] = 2536.771 
$SAVE_POINTS_Z[2] = 9.0077 
$SAVE_POINTS_ANGLE[2] = 269.2893
0@ = 1

:BUYPRO1_1227
wait 0
if and
075C: marker $1719 enabled
0@ == 0
jf @BUYPRO1_1226
$SAVE_PICKUPS_X[2] = 415.0912
$SAVE_PICKUPS_Y[2] = 2536.52
$SAVE_PICKUPS_Z[2] = 15.658
$SAVE_POINTS_X[2] = 418.3
$SAVE_POINTS_Y[2] = 2536.52
$SAVE_POINTS_Z[2] = 15.158
$SAVE_POINTS_ANGLE[2] = 270.0
0@ = 2
jump @BUYPRO1_1226�   __SBFTR 