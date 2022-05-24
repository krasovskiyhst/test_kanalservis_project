import { Component } from "react";
import axios from "axios";
import LineChartOrders from "./LineChartOrders";

class Charts extends Component {
  constructor(props) {
    super(props);
    this.state = { orders: [] };
  }

  componentDidMount() {
    axios.get(`/api/v1/orders/chart/`).then(response => {
        const orders = response.data;
        this.setState({ orders: orders })
    });
  }

  render() {

    let ordersChart = this.state.orders;

    return (
        <LineChartOrders ordersChart={ordersChart} />
    );
  }
}

export default Charts;