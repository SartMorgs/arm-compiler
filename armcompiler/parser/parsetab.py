
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ADDRESSNAME AREA AREATYPE CODE COMMA END ENDP EQU FUNCTIONNAME INTHANDLER NUMBER OPCODE ORG PROC REGISTERcode : directives main functions interruptions END\n\t\t\t\t| directives main interruptions END\n\t\t\t\t| directives main functions END\n\t\t\t\t| directives main ENDdirectives : directivemain : FUNCTIONNAME PROC commandfunctions : functioninterruptions : interruptiondirective : AREA FUNCTIONNAME COMMA CODE AREATYPE\n\t\t\t\t\t | ADDRESSNAME EQU NUMBER\n\t\t\t\t\t | directive\n\t\t\t\t\t | function : FUNCTIONNAME PROC command ENDP\n\t\t\t\t\t| function\n\t\t\t\t\t| interruption : INTHANDLER PROC command ENDP\n\t\t\t\t\t\t| interruption\n\t\t\t\t\t\t| command : OPCODE NUMBER\n\t\t\t\t   | OPCODE FUNCTIONNAME\n\t\t\t\t   | OPCODE body\n\t\t\t\t   | OPCODE\n\t\t\t\t   | command\n\t\t\t\t   | body : REGISTER COMMA REGISTER COMMA REGISTER\n\t\t\t\t| REGISTER COMMA REGISTER NUMBER\n\t\t\t\t| REGISTER COMMA NUMBER\n\t\t\t\t| REGISTER COMMA REGISTER\n\t\t\t\t| REGISTER\n\t\t\t\t| '
    
_lr_action_items = {'AREA':([0,],[4,]),'ADDRESSNAME':([0,],[5,]),'FUNCTIONNAME':([0,2,3,4,6,17,19,25,26,31,32,33,34,35,39,40,42,43,],[-12,7,-5,8,15,-24,-10,-6,32,-19,-20,-21,-29,-9,-28,-27,-26,-25,]),'$end':([1,12,21,22,28,],[0,-4,-3,-2,-1,]),'EQU':([5,],[9,]),'END':([6,10,11,13,14,17,20,25,26,31,32,33,34,36,37,39,40,42,43,],[12,21,22,-7,-8,-24,28,-6,-22,-19,-20,-21,-29,-13,-16,-28,-27,-26,-25,]),'INTHANDLER':([6,10,13,17,25,26,31,32,33,34,36,39,40,42,43,],[16,16,-7,-24,-6,-22,-19,-20,-21,-29,-13,-28,-27,-26,-25,]),'PROC':([7,15,16,],[17,23,24,]),'COMMA':([8,34,39,],[18,38,41,]),'NUMBER':([9,26,38,39,],[19,31,40,42,]),'OPCODE':([17,23,24,],[26,26,26,]),'CODE':([18,],[27,]),'ENDP':([23,24,26,29,30,31,32,33,34,39,40,42,43,],[-24,-24,-22,36,37,-19,-20,-21,-29,-28,-27,-26,-25,]),'REGISTER':([26,38,41,],[34,39,43,]),'AREATYPE':([27,],[35,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'code':([0,],[1,]),'directives':([0,],[2,]),'directive':([0,],[3,]),'main':([2,],[6,]),'functions':([6,],[10,]),'interruptions':([6,10,],[11,20,]),'function':([6,],[13,]),'interruption':([6,10,],[14,14,]),'command':([17,23,24,],[25,29,30,]),'body':([26,],[33,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> code","S'",1,None,None,None),
  ('code -> directives main functions interruptions END','code',5,'p_code','ArmYacc.py',12),
  ('code -> directives main interruptions END','code',4,'p_code','ArmYacc.py',13),
  ('code -> directives main functions END','code',4,'p_code','ArmYacc.py',14),
  ('code -> directives main END','code',3,'p_code','ArmYacc.py',15),
  ('directives -> directive','directives',1,'p_directives','ArmYacc.py',24),
  ('main -> FUNCTIONNAME PROC command','main',3,'p_main','ArmYacc.py',28),
  ('functions -> function','functions',1,'p_functions','ArmYacc.py',32),
  ('interruptions -> interruption','interruptions',1,'p_interruptions','ArmYacc.py',36),
  ('directive -> AREA FUNCTIONNAME COMMA CODE AREATYPE','directive',5,'p_directive','ArmYacc.py',40),
  ('directive -> ADDRESSNAME EQU NUMBER','directive',3,'p_directive','ArmYacc.py',41),
  ('directive -> directive','directive',1,'p_directive','ArmYacc.py',42),
  ('directive -> <empty>','directive',0,'p_directive','ArmYacc.py',43),
  ('function -> FUNCTIONNAME PROC command ENDP','function',4,'p_function','ArmYacc.py',53),
  ('function -> function','function',1,'p_function','ArmYacc.py',54),
  ('function -> <empty>','function',0,'p_function','ArmYacc.py',55),
  ('interruption -> INTHANDLER PROC command ENDP','interruption',4,'p_interruption','ArmYacc.py',62),
  ('interruption -> interruption','interruption',1,'p_interruption','ArmYacc.py',63),
  ('interruption -> <empty>','interruption',0,'p_interruption','ArmYacc.py',64),
  ('command -> OPCODE NUMBER','command',2,'p_command','ArmYacc.py',71),
  ('command -> OPCODE FUNCTIONNAME','command',2,'p_command','ArmYacc.py',72),
  ('command -> OPCODE body','command',2,'p_command','ArmYacc.py',73),
  ('command -> OPCODE','command',1,'p_command','ArmYacc.py',74),
  ('command -> command','command',1,'p_command','ArmYacc.py',75),
  ('command -> <empty>','command',0,'p_command','ArmYacc.py',76),
  ('body -> REGISTER COMMA REGISTER COMMA REGISTER','body',5,'p_body','ArmYacc.py',85),
  ('body -> REGISTER COMMA REGISTER NUMBER','body',4,'p_body','ArmYacc.py',86),
  ('body -> REGISTER COMMA NUMBER','body',3,'p_body','ArmYacc.py',87),
  ('body -> REGISTER COMMA REGISTER','body',3,'p_body','ArmYacc.py',88),
  ('body -> REGISTER','body',1,'p_body','ArmYacc.py',89),
  ('body -> <empty>','body',0,'p_body','ArmYacc.py',90),
]
