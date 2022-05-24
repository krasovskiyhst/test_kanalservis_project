import { Component } from "react";
import './Table.css';
import Order from "./Order";

class Table extends Component {

  render() {

    let orders = this.props.orders;
    let items = orders.map(order => {
      return <Order key={order.id} order={order} />;
    });

    return (
      <table>
        <thead>
          <tr>
            <th>№</th>
            <th>заказ №</th>
            <th>стоимость, $</th>
            <th>Срок поставки</th>
          </tr>
          { items }
        </thead>
      </table>
    );
  }
}

export default Table;

