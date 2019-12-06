% ---------------------------------- Reglas ---------------------------------- 
% Un cliente(que es una persona) puede realizar un pedido
empresa(farmacia).
metodo_pago(efectivo).
metodo_pago(tarjeta).
persona(juan).
numero_cedula(564564, juan).

% Se pueden incluir Elementos de higiene, belleza, medicamento al pedido
higiene(jabon).
higiene(pastadental).
medicamento(omeprazol).
medicamento(supradyn).
belleza(shampu).
belleza(colageno).


numero_pedido_con_articulo(1, jabon).
numero_pedido_con_articulo(1, pastadental).
numero_pedido_con_articulo(1, omeprazol).
numero_pedido_con_articulo(2, omeprazol).
estado_del_pedido(1, pendiente).
estado_del_pedido(2,pagado).

% ---------------------------------- Condiciones ---------------------------------- 
cliente(X) :- persona(X), numero_cedula(_, X).
puede_pedir(X) :- cliente(X).

articulo_medicamento(X) :- medicamento(X).
articulo_belleza(X) :- belleza(X).
articulo_higiene(X) :-higiene(X).

se_vende(X) :- articulo_higiene(X); articulo_belleza(X); articulo_medicamento(X).

cobrable(Numero_pedido) :- numero_pedido_con_articulo(Numero_pedido, _), estado_del_pedido(Numero_pedido, pendiente).
pagado(Numero_pedido) :- estado_del_pedido(Numero_pedido, pagado).
% ---------------------------------- Pruebas ----------------------------------
