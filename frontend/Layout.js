import Head from 'next/head';
import Header from './Partial/Header';

const Layout = ({ children }) => (
    <>
        <Head>
            <title key="title">Progressor</title>
        </Head>
        <Header/>
        {children}
    </>
);

export default Layout;