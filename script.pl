% ---------------------------------- Reglas ---------------------------------- 
% Un cliente(que es una persona) puede realizar un pedido
empresa(farmacia).
metodo_pago(efectivo).
metodo_pago(tarjeta).
persona(nombre('juan'), apellido('vivar'), cedula(4654561), direccion('a la vuelta nomas c/cerca'), ruc('4564564-4')).
persona(nombre('pepe'), apellido('villasanti'), cedula(4654562), direccion('a la vuelta nomas c/ mas cerca'), ruc('4564565-5')).
persona(nombre('andres'), apellido('armoa'), cedula(4654563), direccion('a la vuelta nomas c/ muy cerca'), ruc('4564566-6')).
persona(nombre('jose'), apellido('villa'), cedula(4654567), direccion('a la vuelta nomas c/ muy lejos'), ruc('4564568-8')).
persona(nombre('raul'), apellido('gimenez'), cedula(4654569), direccion('a la vuelta nomas c/ muy cerca'), ruc('4654569-6')).
persona(nombre('julio'), apellido('dominguez'), cedula(4654570), direccion('a la vuelta nomas c/ muy cerca'), ruc('4654570-6')).
persona(nombre('luis'), apellido('santacruz'), cedula(4654571), direccion('a la vuelta nomas c/ muy cerca'), ruc('4654571-6')).

% Se pueden incluir Elementos de higiene, belleza, medicamento al pedido
higiene('jabon', precio(5400), stock(140)).
higiene('pastadental', precio(10000), stock(45)).
medicamento('omeprazol', precio(12000), stock(200)).
medicamento('supradyn', precio(23500), stock(121)).
belleza('shampu', precio(35000), stock(50)).
belleza('colageno', precio(40000), stock(45)).

numero_pedido_con_articulo(1, 'jabon').
numero_pedido_con_articulo(1, 'pastadental').
numero_pedido_con_articulo(1, 'omeprazol').
numero_pedido_con_articulo(2, 'omeprazol').
estado(1,'pendiente').
estado(2,'pagado').

% ---------------------------------- Condiciones ---------------------------------- 
cliente(X) :- persona(_, _, cedula(X), _, _).
puede_pedir(cedula(X)) :- cliente(X).

articulo_medicamento(X) :- medicamento(X, _, _).
articulo_belleza(X) :- belleza(X, _, _).
articulo_higiene(X) :- higiene(X, _, _).
vendible(X) :- articulo_higiene(X); articulo_belleza(X); articulo_medicamento(X).
cobrable(Numero_pedido) :- numero_pedido_con_articulo(Numero_pedido, _), estado(Numero_pedido, 'pendiente').
pagado(Numero_pedido) :- estado(Numero_pedido, 'pagado').
pendiente(Numero_pedido) :- estado(Numero_pedido, 'pendiente').