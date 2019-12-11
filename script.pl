empresa(farmacia).
metodo_pago(efectivo).
metodo_pago(tarjeta).
persona(nombre(juan), apellido(vivar), cedula(4654561), direccion('a la vuelta nomas c/cerca'), ruc('4564564-4')).
persona(nombre(pepe), apellido(villasanti), cedula(4654562), direccion('a la vuelta nomas c/ mas cerca'), ruc('4564565-5')).
persona(nombre(andres), apellido(armoa), cedula(4654563), direccion('a la vuelta nomas c/ muy cerca'), ruc('4564566-6')).
persona(nombre(jose), apellido(villa), cedula(4654567), direccion('a la vuelta nomas c/ muy lejos'), ruc('4564568-8')).
persona(nombre(raul), apellido(gimenez), cedula(4654569), direccion('a la vuelta nomas c/ muy cerca'), ruc('4654569-6')).
persona(nombre(julio), apellido(dominguez), cedula(4654570), direccion('a la vuelta nomas c/ muy cerca'), ruc('4654570-6')).
persona(nombre(luis), apellido(santacruz), cedula(4654571), direccion('a la vuelta nomas c/ muy cerca'), ruc('4654571-6')).

% Se pueden incluir Elementos de higiene, belleza, medicamento al pedido
higiene(jabon, stock(140)).
higiene(aguaoxigenada, stock(50)).
higiene(pastadental, stock(45)).
medicamento(omeprazol, stock(200)).
medicamento(supradyn, stock(121)).
belleza(shampu, stock(50)).
belleza(colageno, stock(45)).


precio_articulo(jabon, 5400).
precio_articulo(aguaoxigenada, 1500).
precio_articulo(pastadental, 10000).
precio_articulo(omeprazol, 12000).
precio_articulo(supradyn, 23500).
precio_articulo(shampu, 35000).
precio_articulo(colageno, 40000).


numero_pedido_con_articulo(1, jabon).
numero_pedido_con_articulo(1, pastadental).
numero_pedido_con_articulo(1, omeprazol).
numero_pedido_con_articulo(1, aguaoxigenada).
numero_pedido_con_articulo(1, supradyn).
numero_pedido_con_articulo(2, omeprazol).
numero_pedido_con_articulo(3, supradyn).
numero_pedido_con_articulo(4, supradyn).
numero_pedido_con_articulo(3, pastadental).
numero_pedido_con_articulo(3, supradyn).

estado(1, pendiente).
estado(2, pagado).
estado(3, pendiente).
estado(4, pagado).

cliente(X) :-
    persona(_, _, cedula(X), _, _).
puede_pedir(cedula(X)) :-
    cliente(X).

articulo_medicamento(X) :-
    medicamento(X, _).
articulo_belleza(X) :-
    belleza(X, _).
articulo_higiene(X) :-
    higiene(X, _).
% ---------- Se verifica si un articulo es vendible ----------
vendible(X) :-
    (   articulo_higiene(X);
       articulo_belleza(X);
       articulo_medicamento(X)
    ).
% ---------- Se verifica si un pedido se puede cobrar ----------
cobrable(Numero_pedido) :-
    numero_pedido_con_articulo(Numero_pedido, _),
    estado(Numero_pedido, pendiente).
% ---------- Se verifica si un pedido se encuentra pagado ----------
pagado(Numero_pedido) :-
    estado(Numero_pedido, pagado).
% ---------- Se verifica si un pedido se encuentra pendiente ----------
pendiente(Numero_pedido) :-
    estado(Numero_pedido, pendiente).

vender_articulo(X,Y) :-
    vender(X,0.0,Y).

vender([],Y,Y).

vender([Head|Tail],Y0,Y) :-
    precio_articulo(Head,Cost),
    Y1 is Y0 + Cost,
    vender(Tail,Y1,Y).