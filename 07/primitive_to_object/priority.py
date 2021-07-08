from dataclasses import dataclass

@dataclass(frozen = True)
class Priority:
	_v: str;

	@property
	def value(self):
		return (self._v);

