namespace Quantum.hellbell {
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Canon;

    @EntryPoint()
    operation BellTest() : Result {
        use q = Qubit();
        H(q);  // Hadamard-Gatter erzeugt Superposition
        let result = M(q);  // Messung des Qubits
        Reset(q);  // Zurücksetzen des Qubits
        return result;
    }
}

