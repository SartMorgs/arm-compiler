
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ADDRESSNAME AREA AREATYPE CODE COMMA END ENDP EQU FUNCTIONNAME INTHANDLER NUMBER OPCODE PROC REGISTERcode : labels codetypes main functions interruptions END\n\t\t\t\t| codetypes main functions interruptions END\n\t\t\t\t| labels codetypes main functions END\n\t\t\t\t| codetypes main functions END\n\t\t\t\t| labels codetypes main END\n\t\t\t\t| codetypes main ENDmain : FUNCTIONNAME PROC commandscommands : command commands\n\t\t\t\t\t| command\n\t\tlabels : label labels\n\t\t\t\t  | labelcodetypes : codetype codetypes\n\t\t\t\t\t | codetypefunctions : function functions\n\t\t\t\t  \t | functioninterruptions : interruption interruption\n\t\t\t\t  \t \t | interruptionlabel : ADDRESSNAME EQU NUMBERcodetype : AREA FUNCTIONNAME COMMA CODE COMMA AREATYPEfunction : FUNCTIONNAME PROC commands ENDPinterruption : INTHANDLER PROC commands ENDPcommand : OPCODE NUMBER\n\t\t\t\t   | OPCODE FUNCTIONNAME\n\t\t\t\t   | OPCODE body\n\t\t\t\t   | OPCODEbody : REGISTER COMMA REGISTER COMMA REGISTER\n\t\t\t\t| REGISTER COMMA REGISTER NUMBER\n\t\t\t\t| REGISTER COMMA NUMBER\n\t\t\t\t| REGISTER COMMA REGISTER\n\t\t\t\t| REGISTER COMMA ADDRESSNAME\n\t\t\t\t| REGISTER\n\t\t\t\t| FUNCTIONNAME'
    
_lr_action_items = {'ADDRESSNAME':([0,4,21,50,],[6,6,-18,55,]),'AREA':([0,2,4,5,11,21,51,],[7,7,-11,7,-10,-18,-19,]),'$end':([1,17,24,26,36,37,47,],[0,-6,-5,-4,-3,-2,-1,]),'FUNCTIONNAME':([3,5,7,8,9,12,15,18,31,32,33,41,42,43,44,45,49,51,53,54,55,57,58,],[10,-13,14,10,19,-12,19,19,-7,-9,43,-8,-22,-23,-24,-31,-20,-19,-29,-28,-30,-27,-26,]),'EQU':([6,],[13,]),'END':([9,15,16,18,23,25,27,29,31,32,33,35,38,41,42,43,44,45,49,52,53,54,55,57,58,],[17,24,26,-15,36,37,-17,-14,-7,-9,-25,47,-16,-8,-22,-23,-24,-31,-20,-21,-29,-28,-30,-27,-26,]),'PROC':([10,19,28,],[20,30,39,]),'NUMBER':([13,33,50,53,],[21,42,54,57,]),'COMMA':([14,34,45,53,],[22,46,50,56,]),'INTHANDLER':([16,18,23,27,29,49,52,],[28,-15,28,28,-14,-20,-21,]),'OPCODE':([20,30,32,33,39,42,43,44,45,53,54,55,57,58,],[33,33,33,-25,33,-22,-23,-24,-31,-29,-28,-30,-27,-26,]),'CODE':([22,],[34,]),'ENDP':([32,33,40,41,42,43,44,45,48,53,54,55,57,58,],[-9,-25,49,-8,-22,-23,-24,-31,52,-29,-28,-30,-27,-26,]),'REGISTER':([33,50,56,],[45,53,58,]),'AREATYPE':([46,],[51,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'code':([0,],[1,]),'labels':([0,4,],[2,11,]),'codetypes':([0,2,5,],[3,8,12,]),'label':([0,4,],[4,4,]),'codetype':([0,2,5,],[5,5,5,]),'main':([3,8,],[9,15,]),'functions':([9,15,18,],[16,23,29,]),'function':([9,15,18,],[18,18,18,]),'interruptions':([16,23,],[25,35,]),'interruption':([16,23,27,],[27,27,38,]),'commands':([20,30,32,39,],[31,40,41,48,]),'command':([20,30,32,39,],[32,32,32,32,]),'body':([33,],[44,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> code","S'",1,None,None,None),
  ('code -> labels codetypes main functions interruptions END','code',6,'p_code','ArmYacc.py',12),
  ('code -> codetypes main functions interruptions END','code',5,'p_code','ArmYacc.py',13),
  ('code -> labels codetypes main functions END','code',5,'p_code','ArmYacc.py',14),
  ('code -> codetypes main functions END','code',4,'p_code','ArmYacc.py',15),
  ('code -> labels codetypes main END','code',4,'p_code','ArmYacc.py',16),
  ('code -> codetypes main END','code',3,'p_code','ArmYacc.py',17),
  ('main -> FUNCTIONNAME PROC commands','main',3,'p_main','ArmYacc.py',28),
  ('commands -> command commands','commands',2,'p_commands','ArmYacc.py',32),
  ('commands -> command','commands',1,'p_commands','ArmYacc.py',33),
  ('labels -> label labels','labels',2,'p_labels','ArmYacc.py',41),
  ('labels -> label','labels',1,'p_labels','ArmYacc.py',42),
  ('codetypes -> codetype codetypes','codetypes',2,'p_codetypes','ArmYacc.py',49),
  ('codetypes -> codetype','codetypes',1,'p_codetypes','ArmYacc.py',50),
  ('functions -> function functions','functions',2,'p_functions','ArmYacc.py',57),
  ('functions -> function','functions',1,'p_functions','ArmYacc.py',58),
  ('interruptions -> interruption interruption','interruptions',2,'p_interruptions','ArmYacc.py',65),
  ('interruptions -> interruption','interruptions',1,'p_interruptions','ArmYacc.py',66),
  ('label -> ADDRESSNAME EQU NUMBER','label',3,'p_label','ArmYacc.py',74),
  ('codetype -> AREA FUNCTIONNAME COMMA CODE COMMA AREATYPE','codetype',6,'p_codetype','ArmYacc.py',78),
  ('function -> FUNCTIONNAME PROC commands ENDP','function',4,'p_function','ArmYacc.py',82),
  ('interruption -> INTHANDLER PROC commands ENDP','interruption',4,'p_interruption','ArmYacc.py',86),
  ('command -> OPCODE NUMBER','command',2,'p_command','ArmYacc.py',90),
  ('command -> OPCODE FUNCTIONNAME','command',2,'p_command','ArmYacc.py',91),
  ('command -> OPCODE body','command',2,'p_command','ArmYacc.py',92),
  ('command -> OPCODE','command',1,'p_command','ArmYacc.py',93),
  ('body -> REGISTER COMMA REGISTER COMMA REGISTER','body',5,'p_body','ArmYacc.py',100),
  ('body -> REGISTER COMMA REGISTER NUMBER','body',4,'p_body','ArmYacc.py',101),
  ('body -> REGISTER COMMA NUMBER','body',3,'p_body','ArmYacc.py',102),
  ('body -> REGISTER COMMA REGISTER','body',3,'p_body','ArmYacc.py',103),
  ('body -> REGISTER COMMA ADDRESSNAME','body',3,'p_body','ArmYacc.py',104),
  ('body -> REGISTER','body',1,'p_body','ArmYacc.py',105),
  ('body -> FUNCTIONNAME','body',1,'p_body','ArmYacc.py',106),
]
