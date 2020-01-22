from cleo import Command

class SkeletonCommand(Command) :
	"""
	Implemention d'une commande très basique
	skeleton
	"""

	def handle(self) :
		self.line("Gretting")
