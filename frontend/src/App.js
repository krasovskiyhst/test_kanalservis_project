import logo from './logo.png';
import { Component } from "react";
import './App.css';
import Tables from "./components/tables/Tables";
import Charts from "./components/charts/Charts";
import axios from "axios";


if (window.location.origin === "http://localhost:3000") {
  axios.defaults.baseURL = "http://127.0.0.1:8000";
} else {
  axios.defaults.baseURL = window.location.origin + ":8000";
}


class App extends Component {

  render() {
    return (
      <div>
        <header>
          <div className="logo">
            <a href="/">
              <img className="logo-img" src={logo} alt=""/>
            </a>
          </div>
        </header>
        <div className="main">
            <Charts/>
            <Tables/>
        </div>
      </div>
    );
  }
}

export default App;

