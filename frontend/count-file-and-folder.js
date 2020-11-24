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

const CountFileAndFolder = ({ data }) => {
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
                        <Line type="monotone" dataKey="file" stroke="#8884d8" activeDot={{r: 8}}/>
                        <Line type="monotone" dataKey="folder" stroke="#82ca9d"/>
                    </LineChart>
                </Col>
            </Row>
        </Container>
    )
}

CountFileAndFolder.getInitialProps = async () => {
    const { data } = await client.get('/count_file_and_folder');
    const results = data.map(item => (
        {
            name: item.date,
            file: item.file,
            folder: item.folder,
        }
    ));
    return { data: results }
}

export default CountFileAndFolder;