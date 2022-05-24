import { Component } from "react";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer
} from "recharts";

class LineChartOrders extends Component {

  render() {

    let data = this.props.ordersChart;
      return (
        <ResponsiveContainer width={'99%'} height={500}>
          <LineChart data={data} margin={{ top: 20, right: 70, left: -10, bottom: 5 }}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="delivery_time" />
            <YAxis type="number"/>
            <Tooltip />

            <Line type="monotone" dataKey="cost_in_dollar_for_chart" stroke="#0095FF" />
          </LineChart>
        </ResponsiveContainer>
      )
  };
}

export default LineChartOrders;