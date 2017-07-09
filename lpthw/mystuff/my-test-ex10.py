wsl = "World Surf League"
kelly_slater = "Kelly Slater"
jjf = "John John Florence"
gabriel_medina = "Gabriel Medina"
italo_ferreira = "Italo Ferreira"
board_size = 5.10
small = 1
medium = 1.17
big = 1.25

print "%s best surfers are:\n%s\n%s\n%s\n%s" % (wsl, 
	kelly_slater, jjf, gabriel_medina, italo_ferreira)

print "Their favourite surfboard's sizes are:\n%s:\t %.1f\"\n%s:\t %.1f\"\n%s:\t %.1f\"\n%s:\t %.1f\"" % (kelly_slater,
 board_size * small,
	jjf, board_size * medium, gabriel_medina, board_size * medium,
	italo_ferreira, board_size * big)