import React from 'react'
import { Navbar,Nav,Container,Row } from 'react-bootstrap'
import { LinkContainer } from 'react-router-bootstrap'


function Header() {
  return (
    <header>
       <Navbar expand="lg" variant='dark' bg="dark" collapseOnSelect>
        <Container>
          <LinkContainer to='/'>
          <Navbar.Brand>ElectroMarket</Navbar.Brand>
          </LinkContainer>
          <Navbar.Toggle aria-controls="basic-navbar-nav" />
          <Navbar.Collapse id="basic-navbar-nav">
            <Nav className="mr-auto">
              <LinkContainer to='/cart'>
              <Nav.Link>Cart<i className='fas fa-shopping-cart'></i></Nav.Link>
              </LinkContainer>
              <LinkContainer to="/login">
              <Nav.Link>Login<i className='fas fa-user'></i></Nav.Link>
              </LinkContainer>
            </Nav>
        </Navbar.Collapse>
        </Container>
    </Navbar>
    </header>
  )
}

export default Header
