# l10n-honduras
Localization for ODO10 - Honduras

## Documentos Fiscales:
### Comprobantes de venta
* Factura, boleta de venta, ticket, recibo de alquiler y recibo por honorarios.
### Documentos complementarios
* Nota de crédito, Nota de débito, Guía de remisión y comprobante de retención
### Otros comprobantes de Venta
* Recibo de servicio publico
* Documentos de bancos y seguros
* Documentación de la DEI para importación
* Boletos aéreos de pasajeros
* Documentos de instituciones del estado

| Documento| ISV | Régimen simplificado|PN no sujetos al ISV | Crédito fiscal ISV | Costo o gasto ISR|
|:--------:|:----:|:---:|:---:|:---:|:---:|
|Factura|SI|x|x|SI|SI|
|Boleta de venta|x|SI|SI|x|SI| 
|Ticket|SI|SI|SI|x|x|

# Requisitos mínimos de los Documentos Fiscales
* RTN
* Nombre/Razón Social
* Nombre Comercial
* Domicilio CM/Su
* Teléfono
* Correo electrónico
* Denominación
* CAI
* Fecha límite de emisión
* Núm. Correlativo
* Desato: ORIG/COP
* Rango de documentos

## Factura
* Nombre/Razón comprador
* RTN Comprador
* Fecha de emisión
* Descripción del bien o servicio
* Cantidades de unidades
* Valuar unitario del bien o servicio
* Subtotales discriminados por tarifa
* Discriminación del impuesto
* Signo de la moneda Lempira
* Importe total literal y numeral
* CAEE (Emisión electrónica)
* QR (opcional)

## Numero de documento fiscal:
```
001 - 001 - 01 - 00000001
  |     |    |    d) Numero correlativo del doc.
  |     |    c) Tipo de documento: 
  |     |        01 Factura
  |     |        02 Boleta de venta
  |     |        03 Recibo de alquiler
  |     |        04 Recibo por honorarios
  |     b) Establecimiento
  a) Punto de emisión
 ```
 Los Auto impresores deberán cumplir los requisitos 
 siguientes, según sea el caso:
 

## Sistema Computarizado
* Integrado a un sistema contable
* Software con mecanismos de seguridad y controles de auditoría.
* Software con persistencia y disponibilidad inmediata de la información.
* Que informe las características del software que utiliza 
* Matriz de Código de Barra
* Generación de archivos tipo texto.

## Sistemas de Autorización de Emisión Electrónica
* Sistema que cumpla con todos los requisitos de una Sistema computarizado.
* Que el sistema interactúe simultáneamente con los sistemas informáticos de la DEI y/ de los GDFE autorizados por la misma a fin de obtener el CAEE.

## Registros fiscales
* Registros de ventas
* Registros de compras
* Registro de retenciones

> Las Personas Naturales o Jurídicas, están obligadas a Suscribirse al Régimen de Facturación a través del aplicativo “DET Leve”, Módulo de Facturación, y autenticarse con su Usuario y Contraseña Tributaria, adquirida bajo el Portal Tributario “DEI en Línea”, posteriormente deben acceder al **Formulario DEI-926** de Suscripción al Régimen de Facturación.

# Autorización de impresión
Es el acto por el cual la DEI autorizará a los contribuyentes la impresión de sus Documentos Fiscales, otorgando la clave de autorización de impresión (CAI) y la fecha límite de emisión.
**Clave de Autorización de Impresión (CAI):** Es un código que emerge de la Autorización de Impresión.

Los contribuyentes realizarán las Solicitudes de Autorizaciones de Impresión a través del aplicativo DET LIVE, para lo cual deberán de acceder con credenciales de DEI en Línea.

### AUTOMIMPRESOR PROCEDIMIENTO GENERAL:
* Suscripción a Facturación DEI-926
* Autorización de impresión Auto impresor DEI-927


# Por hacer en próximas versiones
* Cambiar número de factura al formato XXX-XXX-XX-XXXXXXXX
  agregar los rangos de facturas
* Cambiar de provincia a departamento
* Cambiar NIF a RTN
* Crear lista de bancos de Honduras
* Agregar campo RTN a Clientes (individual y empresas)
* Elaborar el Estado de Resultados de su
negocio.
* Elaborar el Balance General de su negocio

