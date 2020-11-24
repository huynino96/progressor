import {
    LineChart,
    Line,
    XAxis,
    YAxis,
    CartesianGrid,
    Tooltip,
    Legend,
} from 'recharts';
import { Container, Row, Col } from 'reactstrap';

import client from '../client';

const Home = ({ data }) => {
    return (
        <Container>
            <Row className="mt-5">
                <Col>
                    <LineChart
                        width={800}
                        height={600}
                        data={data}
                        margin={{
                            top: 5, right: 30, left: 20, bottom: 5,
                        }}
                    >
                        <CartesianGrid strokeDasharray="3 3"/>
                        <XAxis dataKey="name"/>
                        <YAxis/>
                        <Tooltip/>
                        <Legend/>
                        <Line type="monotone" dataKey="total" stroke="#8884d8" activeDot={{r: 8}}/>
                        <Line type="monotone" dataKey="javascript" stroke="#82ca9d"/>
                        <Line type="monotone" dataKey="java" stroke="#3498db" />
                        <Line type="monotone" dataKey="python" stroke="#9b59b6" />
                        <Line type="monotone" dataKey="php" stroke="#f39c12" />
                    </LineChart>
                </Col>
            </Row>
        </Container>
    )
}

Home.getInitialProps = async () => {
    const { data } = await client.get('/count_class');
    const results = data.map(item => (
        {
            name: item.date,
            total: item.total,
            javascript: item.javascript,
            java: item.java,
            python: item.python,
            php: item.php,
        }
    ));
    return { data: results }
}

export default Home;