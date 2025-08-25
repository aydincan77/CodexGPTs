function App() {
  return (
    <div>
      <h1>Merhaba React!</h1>
      <button onClick={() => alert('Butona tıkladınız!')}>Bana Tıkla</button>
    </div>
  );
}

ReactDOM.render(<App />, document.getElementById('root'));
