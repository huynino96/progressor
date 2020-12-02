import {useState} from 'react';
import Link from 'next/link';
import {
    Collapse,
    Navbar,
    NavbarToggler,
    NavbarBrand,
    Nav,
    NavItem,
    NavLink,
    UncontrolledDropdown,
    DropdownToggle,
    DropdownMenu,
    DropdownItem,
} from 'reactstrap';

const Header = () => {
    const [isOpen, setIsOpen] = useState(false);

    const toggle = () => setIsOpen(!isOpen);

    const handleClick = repositoryEndpoint => {
        document.cookie = 'repositoryEndpoint=' + repositoryEndpoint;
        window.location.reload();
    }

    return (
        <>
            <Navbar color="light" light expand="md">
                <NavbarBrand href="/">
                    <a className="navbar-brand">Progressor</a>
                </NavbarBrand>
                <NavbarToggler onClick={toggle}/>
                <Collapse isOpen={isOpen} navbar>
                    <Nav className="mr-auto" navbar>
                        <NavItem>
                            <NavLink href="/">
                                <a className="nav-link">Count Class</a>
                            </NavLink>
                        </NavItem>
                        <NavItem>
                            <NavLink href="/count-comment">
                                <a className="nav-link">Count Comment</a>
                            </NavLink>
                        </NavItem>
                        <NavItem>
                            <NavLink href="/count-file-and-folder">
                                <a className="nav-link">Count File & Folder</a>
                            </NavLink>
                        </NavItem>
                        <NavItem>
                            <NavLink href="/count-library">
                                <a className="nav-link">Count Library</a>
                            </NavLink>
                        </NavItem>
                        <NavItem>
                            <NavLink href="/count-loc">
                                <a className="nav-link">Count LOC</a>
                            </NavLink>
                        </NavItem>
                        <NavItem>
                            <NavLink href="/count-method">
                                <a className="nav-link">Count Method</a>
                            </NavLink>
                        </NavItem>
                        <NavItem>
                            <NavLink href="/count-testing">
                                <a className="nav-link">Count Testing</a>
                            </NavLink>
                        </NavItem>
                    </Nav>
                    <Nav className="ml-auto" navbar>
                        <UncontrolledDropdown nav inNavbar>
                            <DropdownToggle nav caret>
                                Repository
                            </DropdownToggle>
                            <DropdownMenu right>
                                <DropdownItem>
                                    <strong>Java</strong>
                                </DropdownItem>
                                <DropdownItem onClick={() => handleClick('kagkarlsson/db-scheduler')}>
                                    kagkarlsson/db-scheduler
                                </DropdownItem>
                                <DropdownItem divider/>
                                <DropdownItem>
                                    <strong>Javascript</strong>
                                </DropdownItem>
                                <DropdownItem onClick={() => handleClick('axios/axios')}>
                                    axios/axios
                                </DropdownItem>
                                <DropdownItem divider/>
                                <DropdownItem>
                                    <strong>Python</strong>
                                </DropdownItem>
                                <DropdownItem onClick={() => handleClick('Pylons/deform')}>
                                    Pylons/deform
                                </DropdownItem>
                                <DropdownItem divider/>
                                <DropdownItem>
                                    <strong>PHP</strong>
                                </DropdownItem>
                                <DropdownItem onClick={() => handleClick('sebastianbergmann/php-timer')}>
                                    sebastianbergmann/php-timer
                                </DropdownItem>
                            </DropdownMenu>
                        </UncontrolledDropdown>
                    </Nav>
                </Collapse>
            </Navbar>
        </>
    );
};

export default Header;