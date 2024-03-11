# poetry_generator.py

from quantum_library import QuantumPoetryAlgorithm  # Annahme: Bibliothek für Quantenalgorithmen

def generate_poetry():
    quantum_poetry_algorithm = QuantumPoetryAlgorithm()
    poem = quantum_poetry_algorithm.generate_poem()
    return poem

if __name__ == "__main__":
    generated_poem = generate_poetry()
    print("Generated Quantum Poem:")
    print(generated_poem)
