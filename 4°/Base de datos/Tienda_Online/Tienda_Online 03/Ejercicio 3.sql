USE tienda_online;

SELECT
    productos1.id_producto AS 'ID',
    productos1.nombre AS 'Nombre',
    SUM(detalles1.cantidad) AS 'TotalVendido'

FROM
    detalle_pedidos AS detalles1

    JOIN pedidos AS pedidos1 ON
        pedidos1.id_pedido = detalles1.id_pedido AND
        pedidos1.estado != 'cancelado'

    JOIN productos AS productos1 ON
        productos1.id_producto = detalles1.id_producto

GROUP BY
    ID,
    Nombre

ORDER BY
    TotalVendido DESC;