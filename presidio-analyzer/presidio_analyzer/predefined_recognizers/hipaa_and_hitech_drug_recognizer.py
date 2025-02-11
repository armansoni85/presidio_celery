import json
import os
from presidio_analyzer import Pattern, PatternRecognizer
from typing import List

base_path = '/home/arman/Client/Eric/Presidio_web-main/presidio-analyzer/data'

def load_data_lazy(filename, loader_function):
    """Load data lazily, only when needed."""
    if not hasattr(load_data_lazy, "cache"):
        load_data_lazy.cache = {}
    if filename not in load_data_lazy.cache:
        load_data_lazy.cache[filename] = loader_function()
    return load_data_lazy.cache[filename]

# Data loader function for drugs
def load_drugs():
    with open(os.path.join(base_path, 'Drugs.json')) as f:
        return set(json.load(f))

# Lazy-load drug data
drugs = load_data_lazy('Drugs.json', load_drugs)

class DrugRecognizer(PatternRecognizer):
    """Recognize drug names using patterns."""

    def __init__(
        self,
        supported_language: str = "en",
        supported_entity: str = "HIPAA_HITECH_DRUG",
    ):
        patterns = [Pattern(f"Drug Name: {drug}", rf"\b{drug}\b", 0.9) for drug in drugs]
        context = [
            "drug", "medication", "prescription", "treatment"
        ]
        super().__init__(
            supported_entity=supported_entity,
            patterns=patterns,
            context=context,
            supported_language=supported_language,
        )
