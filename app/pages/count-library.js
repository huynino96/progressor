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
import cookies from "next-cookies";
import {REPOSITORY_ENDPOINT} from "../utils/constants";

const CountLibrary = ({ data }) => {
    return (
        <Container>
            <Row className="mt-5">
                <Col>
                    <LineChart
                        width={1050}
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
                        <Line type="monotone" dataKey="library" stroke="#8884d8" activeDot={{r: 8}}/>
                    </LineChart>
                </Col>
            </Row>
        </Container>
    )
}

CountLibrary.getInitialProps = async (context) => {
    const { repositoryEndpoint } = cookies(context);
    const finalRepositoryEndpoint = repositoryEndpoint ? repositoryEndpoint : REPOSITORY_ENDPOINT;
    const { data } = await client.get(`/count_library/${finalRepositoryEndpoint}`);
    const results = data.map(item => (
        {
            name: item.date,
            library: item.library,
        }
    ));
    return { data: results }
}

export default CountLibrary;