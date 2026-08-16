from pathlib import Path
cmd=[]
def c(s): cmd.append(':'+s)
def box(x1,y1,x2,y2,paint=None):
 c(f'box {x1} {y1} {x2} {y2}')
 if paint: c(f'paint {paint}')
def nmos(x,y,gate_label):
 box(x,y,x+90,y+42,'ndiffusion'); box(x+37,y-30,x+52,y+110,'polysilicon')
 for xx in [x+10,x+62]:
  box(xx,y+12,xx+17,y+29,'ndc'); c('paint mcon'); box(xx-5,y+7,xx+22,y+34,'metal1')
 box(x+37,y+80,x+54,y+97,'pc'); c('paint mcon'); box(x+32,y+75,x+59,y+102,'metal1')
 box(x+20,y+63,x+71,y+114,'metal2'); box(x+33,y+76,x+59,y+102,'via1'); box(x+20,y+63,x+71,y+114,'metal3'); box(x+32,y+75,x+60,y+103,'via2')
def pmos(x,y,gate_label):
 box(x-100,y-100,x+190,y+230,'nwell')
 box(x,y,x+90,y+84,'pdiffusion'); box(x+37,y-40,x+52,y+150,'polysilicon')
 for xx in [x+10,x+62]:
  box(xx,y+30,xx+17,y+47,'pdc'); c('paint mcon'); box(xx-5,y+25,xx+22,y+52,'metal1')
 box(x+37,y+120,x+54,y+137,'pc'); c('paint mcon'); box(x+32,y+115,x+59,y+142,'metal1')
 box(x+20,y+103,x+71,y+154,'metal2'); box(x+33,y+116,x+59,y+142,'via1'); box(x+20,y+103,x+71,y+154,'metal3'); box(x+32,y+115,x+60,y+143,'via2')
 box(x+125,y+30,x+142,y+47,'nsc'); c('paint mcon'); box(x+120,y+25,x+147,y+52,'metal1')

c('load cmr_nand4')
nmos(500,100,'ROW'); nmos(800,100,'COL')
pmos(500,500,'ROW'); pmos(800,500,'COL')
box(530,188,560,645,'metal3'); box(530,400,560,430); c('label ROW center metal3')
box(830,188,860,645,'metal3'); box(830,400,860,430); c('label COL center metal3')
box(450,335,950,365,'metal2'); box(900,335,950,365); c('label WAKEN center metal2')
box(450,700,950,730,'metal2'); box(900,700,950,730); c('label VDD center metal2')
box(450,20,950,50,'metal2'); box(900,20,950,50); c('label GND center metal2')
def via_to_m2(cx,cy):
 box(cx-20,cy-20,cx+20,cy+20,'metal1'); c('paint metal2'); box(cx-13,cy-13,cx+13,cy+13,'via1')
for x in [500,800]:
 via_to_m2(x+18,538); box(x+3,365,x+33,538,'metal2')
 via_to_m2(x+70,538); box(x+55,538,x+85,575,'metal2'); box(x+55,545,x+115,575,'metal2'); box(x+85,545,x+115,715,'metal2')
 via_to_m2(x+133,538); box(x+118,538,x+148,715,'metal2')
via_to_m2(518,120); box(503,120,533,150,'metal2'); box(470,120,533,150,'metal2'); box(470,120,500,350,'metal2')
via_to_m2(870,120); box(855,35,885,120,'metal2')
via_to_m2(570,120); via_to_m2(818,120); box(570,105,818,135,'metal2')
for x in [430,930]:
 box(x,100,x+17,117,'psc'); c('paint mcon'); box(x-5,95,x+22,122,'metal1'); via_to_m2(x+8,108); box(x-18,35,x+34,108,'metal2')
c('save'); c('drc check'); c('drc count total'); c('extract all'); c('quit -noprompt')
Path('cmr_cmd.txt').write_text('\n'.join(cmd)+'\n')
