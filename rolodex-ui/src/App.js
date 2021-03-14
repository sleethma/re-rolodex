import React from "react"
import CallerDash from "./components/CallerDash"
import s from './styles/app.module.css';


function App() {
  return (
    <div className={s.container}>
      <CallerDash/>
    </div>
  );
}

export default App;
