import { Component } from "react";
import './TotalBar.css';

class TotalBar extends Component {

  render() {

    let orders = this.props.orders;

    let total = 0
    if (orders.length !== 0){
      total = orders.map(item => item.cost_in_dollar).reduce((prev, next)=>prev + next, 0);
    }

    return (
      <table className="total_bar">
        <thead>
          <tr>
            <th>TOTAL</th>
          </tr>
          <tr>
            <td>{total}</td>
          </tr>
        </thead>
      </table>
    );
  }
}

export default TotalBar;
