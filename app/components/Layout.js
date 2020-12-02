import Head from 'next/head';
import Cookies from 'js-cookie';
import Header from './Partial/Header';
import { REPOSITORY_ENDPOINT } from '../utils/constants';

const Layout = ({ children }) => (
    <>
        <Head>
            <title key="title">Progressor</title>
        </Head>
        <Header/>
        <h1 className="text-center mt-5">
            Repository: {Cookies.get('repositoryEndpoint') ? Cookies.get('repositoryEndpoint') : REPOSITORY_ENDPOINT}
        </h1>
        {children}
    </>
);

export default Layout;