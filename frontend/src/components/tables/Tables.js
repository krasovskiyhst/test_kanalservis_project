import { Component } from "react";
import Table from "./orderTable/Table";
import TotalBar from "./totalBar/TotalBar";
import axios from "axios";
import './Tables.css';

class Tables extends Component {
  constructor(props) {
    super(props);
    this.state = { orders: [] };
  }

  componentDidMount() {
    axios.get(`/api/v1/orders/`).then(response => {
        const orders = response.data;
        this.setState({ orders: orders })
    });
  }

  render() {
    return (
      <div className="tables">
        <TotalBar orders={this.state.orders}/>
        <Table orders={this.state.orders}/>
      </div>
    );
  }
}

export default Tables;

