# Juego - Damas Españolas

Se implementa el juego de Damas Españolas con una maquina que trabaja con el algoritmo Alfa Beta con el lenguaje Python. 
#
El juego de Damas Españolas, o Damas Clásicas, es considerado como la variante viva más antigua
del juego de damas. Se practica en toda la Península Ibérica, en el Norte de África y en muchos
países de Sudamérica y Centroamérica. Se juega sobre un damero de 8x8, en el que se utilizan
exclusivamente las casillas de color blanco, en donde cada uno de los dos bandos utiliza 12 piezas
de color blanco y negro respectivamente, denominadas peones. Inicialmente los peones se ubican
en las tres primeras filas de su lado correspondiente en el tablero. Comienza la partida el jugador
que maneja las piezas de color blanco.


Reglas del juego.

1) El Juego de Damas se desarrolla en un tablero de 64 casillas (8x8), coloreadas blancas y negras
alternadamente (tablero clásico) con el escaque inferior derecho de color blanco.
2) El tablero debe ser superficie plana y no brillante, dividido en ocho partes iguales en altura y
anchura (8x8) cuyas intersecciones dan lugar a las 64 casillas del tablero.
3) Las piezas, llamadas peones, podrán ser de madera, plástico, hueso o marfil, 12 por cada bando,
blancas y negras.

4) Se juega sobre las casillas blancas del tablero, quedando la gran diagonal o diagonal principal a
la derecha del jugador (esquina inferior derecha del tablero).
5) El tablero se numera de la siguiente forma: Esta numeración será la utilizada a fin de
representación de partidas, posiciones, estudios y en general todo lo relacionado con la
nomenclatura del juego.
6) Los 12 peones blancos se colocan sobre las casillas 1 a 12 del tablero y los 12 negros sobres las
casillas 21 a 32.
7) Cada color es conducido por un jugador. La primera jugada debe ser realizada siempre por el
jugador con las fichas blancas.
8) Los movimientos de los peones son en diagonal, una sola casilla y en sentido de avance, o sea,
hacia el campo oponente.
9) Los movimientos se realizan alternadamente, uno por jugador.
10) "Pieza tocada, pieza jugada". Si se toca una pieza, ésta debe jugarse si el movimiento es posible.
11) Si un peón llega a la línea base del contrario (1-4 blanco, 29-32 negro), se convierte en dama,
coronándolo con otro peón.
12) La dama mueve también en diagonal, pero hacia adelante y hacia atrás, pudiendo recorrer
cualquier número de casillas si están libres.
13) La dama no puede saltar dos peones juntos o un peón de su color. En caso de peón de otro color
ver captura de piezas.
14) Si un peón se encuentra en casilla diagonal contigua a otro del contrario estando la posterior
vacía y en turno de juego, puede saltar por encima de este hasta la casilla vacía, retirándole del
tablero.
15) Si después de realizado un salto, el peón llega a una casilla en las mismas condiciones de la
anterior, puede continuar saltando y así todas las veces en las que esto sea posible (captura
múltiple).
16) Si una dama se encuentra en turno y en la misma diagonal con una pieza contraria tras la cual
hay casillas vacías, puede saltar está hasta quedar en cualquiera de las casillas vacías.
17) Si después de realizado el salto anterior se vuelve a encontrar en otra diagonal con pieza
contraria en las mismas condiciones, podrá proseguir los saltos todas las veces que esto fuese
posible (capturas múltiples).
18) En capturas múltiples, no se puede saltar dos veces por encima de la misma pieza.
19) Un movimiento de captura no finaliza hasta que se terminan todos los saltos posibles. Solo
entonces pueden retirarse del tablero las piezas capturadas.
20) El capturar es absolutamente obligatorio. Si un jugador no se ha dado cuenta de una captura,
debe advertírsele.
21) En caso de competición, si una partida se demostrase que a partir de cierto movimiento se han
infringido las reglas, deberá ser repetido a partir del movimiento infractor o anulada, según acordase
el jurado nombrado al efecto.

22) Ley de la Cantidad: Es obligatorio capturar al mayor número posible de piezas.
23) Ley de la Calidad: A igual número de piezas a capturar, es obligatorio capturar a las de mayor
calidad, dama antes que peón.
24) Un juego se considera perdido cuando un jugador:
* Pierde todas sus piezas.
* Tiene piezas, pero tocándoleturno no tiene movimiento posible (ahogado).
* Abandone la partida.

#



