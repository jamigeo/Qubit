namespace Quantum.hellbell {
  open Microsoft.Quantum.Canon;
  open Microsoft.Quantum.Intrinsic;
  open Microsoft.Quantum.Measurement;

  @EntryPoint()
  operation BellTest() : Result {
    use qubit = Qubit() {
      H(qubit);
      let result = M(qubit);
      Reset(qubit);
      return result;
    }
  }
}
