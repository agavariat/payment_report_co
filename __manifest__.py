
{
	'name': 'Reporte para Recibos de Pago  - Colombia',
	
	'version': '12.0',
       
	'summary': 'Recibos de Pago para Facturación',
	'description': """
Reporte para Remisiones:
======================
	* Este módulo realiza un reporte qweb.
	
	""",
	'depends': [
		
		'account',
	],
	'data': [
		
		'views/payment_report_co.xml',
		
	],
	'installable': True,
	'application': True,
	'auto_install': True,
}
