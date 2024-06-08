import qsharp
from Quantum.hellbell import BellTest
from qsharp import Result
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

def run_bell_test(repeats):
    results = []

    for i in range(repeats):
        result = BellTest.simulate()  # Q#-Operation aufrufen
        print(f"Run {i+1}: Simulation result -> {result}")
        binary_result = 1 if result == Result.One else 0  # Result sollte `Result`-Typ sein
        print(f"Run {i+1}: Binary result -> {binary_result}")
        results.append(binary_result)

    print("Alle Ergebnisse:", results)
    return results

def analyze_results(results):
    results_tensor = tf.convert_to_tensor(results, dtype=tf.int32)
    
    ones_count = tf.reduce_sum(results_tensor)
    zeros_count = tf.size(results_tensor) - ones_count

    print(f"Results analysis:\n"
          f"Total runs: {len(results)}\n"
          f"Number of Ones: {ones_count.numpy()}\n"
          f"Number of Zeros: {zeros_count.numpy()}")

    counts = tf.stack([zeros_count, ones_count])
    categories = ['Zero', 'One']

    return counts, categories

if __name__ == "__main__":
    repeats = 1000
    results = run_bell_test(repeats)
    counts, categories = analyze_results(results)

    plt.bar(categories, counts.numpy(), color=['blue', 'orange'])
    plt.xlabel('Result')
    plt.ylabel('Count')
    plt.title(f'Bell Test Results over {repeats} runs')
    plt.show()
