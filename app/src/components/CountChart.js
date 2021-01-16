import { Helmet } from 'react-helmet'
import { CartesianGrid, Legend, Line, LineChart, Tooltip, XAxis, YAxis } from 'recharts'
import React from 'react'

const CountChart = ({ title, data, keyword }) => (
  <>
    <Helmet title={title} />
    <div className="kit__utils__heading">
      <h5>
        <span className="mr-3">{title}</span>
      </h5>
    </div>
    <div className="row">
      <div className="col-lg-12">
        {keyword === 'file_and_folder' ? (
          <LineChart
            width={1050}
            height={600}
            data={data}
            margin={{
              top: 5,
              right: 30,
              left: 20,
              bottom: 5,
            }}
          >
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="name" />
            <YAxis />
            <Tooltip />
            <Legend />
            <Line type="monotone" dataKey="file" stroke="#82ca9d" />
            <Line type="monotone" dataKey="folder" stroke="#3498db" />
          </LineChart>
        ) : (
          <LineChart
            width={1050}
            height={600}
            data={data}
            margin={{
              top: 5,
              right: 30,
              left: 20,
              bottom: 5,
            }}
          >
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="name" />
            <YAxis />
            <Tooltip />
            <Legend />
            <Line type="monotone" dataKey="total" stroke="#8884d8" activeDot={{ r: 8 }} />
            <Line type="monotone" dataKey="javascript" stroke="#82ca9d" />
            <Line type="monotone" dataKey="java" stroke="#3498db" />
            <Line type="monotone" dataKey="python" stroke="#9b59b6" />
            <Line type="monotone" dataKey="php" stroke="#f39c12" />
          </LineChart>
        )}
      </div>
    </div>
  </>
)

export default CountChart
