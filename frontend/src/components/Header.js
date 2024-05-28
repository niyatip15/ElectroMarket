import React from 'react'
import { Navbar,Nav,Container,Row } from 'react-bootstrap'

function Header() {
  return (
    <header>
       <Navbar expand="lg" variant='dark' bg="dark" collapseOnSelect>
        <Container>
          <Navbar.Brand href="/">ElectroMarket</Navbar.Brand>
          <Navbar.Toggle aria-controls="basic-navbar-nav" />
          <Navbar.Collapse id="basic-navbar-nav">
            <Nav className="mr-auto">
              <Nav.Link href="/cart">Cart<i className='fas fa-shopping-cart'></i></Nav.Link>
              <Nav.Link href="/cart">Login<i className='fas fa-user'></i></Nav.Link>
            </Nav>
        </Navbar.Collapse>
        </Container>
    </Navbar>
    </header>
  )
}

export default Header
