# coding=utf-8

import octoprint.printer

class temperature_probe(octoprint.printer.PrinterCallback):

	def on_printer_add_temperature(self, data):
		# Prints {'tool0': {'actual': 22.5, 'target': 0.0}, 'bed': {'actual': 22.9, 'target': 0.0}, 'time': 1496353649}
		print data

