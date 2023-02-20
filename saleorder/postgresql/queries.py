def query_get_picking_quantity_by_customer(name_customer):
    """Suma todas las referencias que tengo despachadas de un cliente"""
    sql = f"""
        SELECT 
            CASE 
				WHEN SUM(T3.quantity) is null 
				THEN 0
				ELSE SUM(T3.quantity)
			END
        FROM
            saleorder_saleorder T0
            INNER JOIN picking_picking T1 ON T0.id = T1.sale_order_id
            INNER JOIN box_box T2 ON T1.id = T2.picking_id
            INNER JOIN box_item_boxitem T3 ON T2.id = T3.box_id
        WHERE
            T0.customer_name = '{name_customer}'
    """
    return sql

def query_get_request_quantity_by_customer(name_customer):
    """Suma todas las referencias que tengo solicitadas por un cliente"""
    sql = f"""
        SELECT
            CASE 
				WHEN SUM(T1.quantity) is null 
				THEN 0
				ELSE SUM(T1.quantity)
			END
        FROM
            saleorder_saleorder T0
            INNER JOIN saleorder_item_saleorderitem T1 ON T0.id = T1.sale_order_id
        WHERE
            T0.customer_name = '{name_customer}'
    """
    return sql

def query_get_picking_quantity_by_saleorder(sale_order):
    """Suma todas las referencias que tengo despachadas de una orden de venta"""
    sql = f"""
        SELECT
            CASE 
				WHEN SUM(T3.quantity) is null 
				THEN 0
				ELSE SUM(T3.quantity)
			END
        FROM
            saleorder_saleorder T0
            INNER JOIN picking_picking T1 ON T0.id = T1.sale_order_id
            INNER JOIN box_box T2 ON T1.id = T2.picking_id
            INNER JOIN box_item_boxitem T3 ON T2.id = T3.box_id
        WHERE
            T0.no_sale_order = '{sale_order}'
    """
    return sql

def query_get_request_quantity_by_saleorder(sale_order):
    """Suma todas las referencias que tengo solicitadas de una orden de venta"""
    sql = f"""
        SELECT
            CASE 
				WHEN SUM(T1.quantity) is null 
				THEN 0
				ELSE SUM(T1.quantity)
			END
        FROM
            saleorder_saleorder T0
            INNER JOIN saleorder_item_saleorderitem T1 ON T0.id = T1.sale_order_id
        WHERE
            T0.no_sale_order = '{sale_order}'
    """
    return sql