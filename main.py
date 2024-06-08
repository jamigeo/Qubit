import qsharp
from Quantum.hellbell import BellTest
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

class BellTest:
    @staticmethod
    def simulate():
        # Beispielhafte Implementierung
        import random
        return 'One' if random.random() > 0.5 else 'Zero'

def run_bell_test(repeats):
    results = []

    for i in range(repeats):
        result = BellTest.simulate()
        print(f"Run {i+1}: Simulation result -> {result}")  # Debug-Ausgabe des Simulationsergebnisses
        binary_result = 1 if result == 'One' else 0
        print(f"Run {i+1}: Binary result -> {binary_result}")  # Debug-Ausgabe des binären Ergebnisses
        results.append(binary_result)

    print("Alle Ergebnisse:", results)  # Ausgabe aller Ergebnisse zur Überprüfung
    return results  # Rückgabe der Ergebnisse

def analyze_results(results):
    # Konvertiere die Liste in einen Tensor
    results_tensor = tf.convert_to_tensor(results, dtype=tf.int32)
    
    ones_count = tf.reduce_sum(results_tensor)
    zeros_count = tf.size(results_tensor) - ones_count

    print(f"Results analysis:\n"
           f"Total runs: {len(results)}\n"
           f"Number of Ones: {ones_count.numpy()}\n"
           f"Number of Zeros: {zeros_count.numpy()}")

    # Simple bar chart visualization using TensorFlow
    counts = tf.stack([zeros_count, ones_count])
    categories = ['Zero', 'One']

    return counts, categories

if __name__ == "__main__":
    repeats = 1000  # Number of times to repeat the Bell test
    results = run_bell_test(repeats)
    counts, categories = analyze_results(results)

    # Plot the results using TensorFlow
    plt.bar(categories, counts.numpy(), color=['blue', 'orange'])
    plt.xlabel('Result')
    plt.ylabel('Count')
    plt.title(f'Bell Test Results over {repeats} runs')
    plt.show()