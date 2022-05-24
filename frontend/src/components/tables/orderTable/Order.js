import { Component } from "react";
import './Order.css';

class Order extends Component {
  render() {
    const { order } = this.props;
    return (
      <tr key={order.id}>
        <td>{order.id}</td>
        <td>{order.order_number}</td>
        <td>{order.cost_in_dollar}</td>
        <td>{order.delivery_time}</td>
      </tr>
    );
  }
}

export default Order;

