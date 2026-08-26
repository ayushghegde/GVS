:load v13r_diff_pair_sym
:box 130 1450 131 1451
:getcell nf_cross child 0 0 parent 130 1450
:box 135 1456 165 1486
:paint via1
:box 20 1456 165 1486
:paint metal2
:label NEIGHBOR center metal2
:box 225 1456 255 1486
:paint via1
:box 225 1456 535 1486
:paint metal2
:label CELL center metal2
:box 180 1555 210 1585
:paint via1
:box 180 1555 210 1670
:paint metal2
:label AP_GATE center metal2
:box 500 1450 501 1451
:getcell nf_cross child 0 0 parent 500 1450
:box 505 1456 535 1486
:paint via1
:box 595 1456 625 1486
:paint via1
:box 595 1456 740 1486
:paint metal2
:label ARTERY center metal2
:box 550 1555 580 1585
:paint via1
:box 550 1555 580 1670
:paint metal2
:label EXPIRE center metal2
:box 80 900 110 1300
:paint metal2
:label GC center metal2
:box 650 900 680 1300
:paint metal2
:label GR center metal2
:save v13r_diff_pair_sym.mag
:drc check
:drc count total
:extract all
:quit -noprompt
