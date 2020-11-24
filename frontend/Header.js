import { useState } from 'react';
import Link from 'next/link';
import {
  Collapse,
  Navbar,
  NavbarToggler,
  NavbarBrand,
  Nav,
  NavItem,
  NavLink,
} from 'reactstrap';

const Header = () => {
    const [isOpen, setIsOpen] = useState(false);

    const toggle = () => setIsOpen(!isOpen);

    return (
        <>
            <Navbar color="light" light expand="md">
                <NavbarBrand href="/" tag={Link}>
                    <a className="navbar-brand">Progressor</a>
                </NavbarBrand>
                <NavbarToggler onClick={toggle}/>
                <Collapse isOpen={isOpen} navbar>
                    <Nav className="mr-auto" navbar>
                        <NavItem>
                            <NavLink href="/" tag={Link}>
                                <a className="nav-link">Count Class</a>
                            </NavLink>
                        </NavItem>
                        <NavItem>
                            <NavLink href="/count-comment" tag={Link}>
                                <a className="nav-link">Count Comment</a>
                            </NavLink>
                        </NavItem>
                        <NavItem>
                            <NavLink href="/count-file-and-folder" tag={Link}>
                                <a className="nav-link">Count File & Folder</a>
                            </NavLink>
                        </NavItem>
                        <NavItem>
                            <NavLink href="/count-library" tag={Link}>
                                <a className="nav-link">Count Library</a>
                            </NavLink>
                        </NavItem>
                        <NavItem>
                            <NavLink href="/count-loc" tag={Link}>
                                <a className="nav-link">Count LOC</a>
                            </NavLink>
                        </NavItem>
                        <NavItem>
                            <NavLink href="/count-method" tag={Link}>
                                <a className="nav-link">Count Method</a>
                            </NavLink>
                        </NavItem>
                        <NavItem>
                            <NavLink href="/count-testing" tag={Link}>
                                <a className="nav-link">Count Testing</a>
                            </NavLink>
                        </NavItem>
                    </Nav>
                </Collapse>
            </Navbar>
        </>
    );
};

export default Header;