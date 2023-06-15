from FlairNER import NER as FlairNER
from SpacyNER import NER as SpacyNER

abc = "Philosophers often understand emergence as a claim about the etiology of a system's properties. An emergent property of a system, in this context, is one that is not a property of any component of that system, but is still a feature of the system as a whole. Nicolai Hartmann (1882–1950), one of the first modern philosophers to write on emergence, termed this a categorial novum (new category)."

print(FlairNER(abc))
print(SpacyNER(abc))