import _sqlite3
kioscoDB = _sqlite3.connect("Kiosco.db")
cursor = kioscoDB.cursor()

# cursor.execute("CREATE TABLE producto(id_producto INTEGER PRYMARY KEY, nombre, tipo, precio INTEGER NUMBER, cantidad INTEGER NUMBER, cantVentas INTEGER NUMBER)")
# cursor.execute("CREATE TABLE proveedores(id_proveedor INTEGER PRIMARY KEY, empresa, tipodeProductoVende)")
# cursor.execute("CREATE TABLE ventas(id_venta INTEGER PRIMARY KEY, id_producto, id_proveedor, fecha, FOREIGN KEY (id_producto) REFERENCES producto(id_producto),FOREIGN KEY (id_proveedor)REFERENCES proveedores(id_proveedor) )")

cursor.commit()
