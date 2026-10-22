USE tienda_online;

SELECT
    clientes1.id_cliente AS 'ID',
    clientes1.nombre AS 'Nombre',
    clientes1.apellido AS 'Apellido',
    ROUND(SUM((detalles1.precio_unitario * detalles1.cantidad) * (1 - (detalles1.descuento_pct / 100))), 2) AS 'GastoTotal'

FROM
    detalle_pedidos AS detalles1

    JOIN pedidos AS pedidos1 ON
        pedidos1.id_pedido = detalles1.id_pedido AND
        pedidos1.estado != 'cancelado'

        JOIN clientes AS clientes1 ON
            clientes1.id_cliente = pedidos1.id_cliente

GROUP BY
    ID,
    Nombre, 
    Apellido

HAVING
    GastoTotal > (
        SELECT
            AVG((detalles2.precio_unitario * detalles2.cantidad) * (1 - (detalles2.descuento_pct / 100)))

        FROM
            detalle_pedidos AS detalles2

            JOIN pedidos AS pedidos2 ON
                pedidos2.id_pedido = detalles2.id_pedido AND
                pedidos2.estado != 'cancelado'
        )

ORDER BY
    ID;