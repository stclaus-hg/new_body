import React, { Component } from "react";
import { Container, Nav, Navbar } from 'react-bootstrap'
import logo from './logo192.png'
import { MemoryRouter, Route, Routes } from "react-router-dom"
import Home from "../Pages/Home";

export default class Header extends Component {
    render() {
        return (
            <>
                <Navbar fixed="top" collapseOnSelect expand="md" bg="dark" variant="dark">
                    <Container>
                        <Navbar.Brand href="/">
                            <img
                                src={logo}
                                height="30"
                                width="30"
                                className="d-inline-block align-top"
                                alt="New body"
                            />
                        </Navbar.Brand>
                        <Navbar.Toggle aria-controls="responsive-navbar-nav" />
                        <Navbar.Collapse id="responsive-navbar-nav">
                            <Nav className="mr-auto">
                                <Nav.Link href="/">Home</Nav.Link>
                                <Nav.Link href="/about">About</Nav.Link>
                                <Nav.Link href="/contacts">Contacts</Nav.Link>
                            </Nav>
                        </Navbar.Collapse>
                    </Container>
                </Navbar>
                <MemoryRouter>
                    <Routes>
                        <Route exact path="/" element={<Home />} />
                    </Routes>
                </MemoryRouter> 

            </>
        )
    }

}