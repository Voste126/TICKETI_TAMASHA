import React, { useState } from 'react';
import {
  MDBIcon,
  MDBContainer,
  MDBNavbar,
  MDBNavbarBrand,
  MDBNavbarToggler,
  MDBNavbarNav,
  MDBNavbarItem,
  MDBNavbarLink,
  MDBCollapse,
} from 'mdb-react-ui-kit';

export default function Navbar() {
  const [openNav, setOpenNav] = useState(false);

  return (
    <MDBNavbar expand='lg' dark style={{ backgroundColor: '#1D3557' }} sticky>
      <MDBContainer fluid>
        <MDBNavbarBrand href='#' style={{ color: '#F1FAEE', fontWeight: 'bold' }}>
          TICKETI TAMASHA
        </MDBNavbarBrand>
        <MDBNavbarToggler
          type='button'
          aria-expanded='false'
          aria-label='Toggle navigation'
          onClick={() => setOpenNav(!openNav)}
        >
          <MDBIcon icon='bars' fas style={{ color: '#F1FAEE' }} />
        </MDBNavbarToggler>
        <MDBCollapse navbar open={openNav}>
          <MDBNavbarNav className='ms-auto'>
            <MDBNavbarItem>
              <MDBNavbarLink active aria-current='page' href='/' style={{ color: '#F1FAEE' }}>
                Home
              </MDBNavbarLink>
            </MDBNavbarItem>
            <MDBNavbarItem>
              <MDBNavbarLink href='/eventlist' style={{ color: '#F1FAEE' }}>
                Events
              </MDBNavbarLink>
            </MDBNavbarItem>
            <MDBNavbarItem>
              <MDBNavbarLink href='/pay' style={{ color: '#F1FAEE' }}>
                Payment
              </MDBNavbarLink>
            </MDBNavbarItem>
            <MDBNavbarItem>
              <MDBNavbarLink href='#about-us' style={{ color: '#F1FAEE' }}>
                About Us
              </MDBNavbarLink>
            </MDBNavbarItem>
            <MDBNavbarItem>
              <MDBNavbarLink href='#contact-us' style={{ color: '#F1FAEE' }}>
                Contact
              </MDBNavbarLink>
            </MDBNavbarItem>
            <MDBNavbarItem>
              <MDBNavbarLink href='/login' style={{ color: '#F1FAEE' }}>
                Login/SignUp
              </MDBNavbarLink>
            </MDBNavbarItem>
          </MDBNavbarNav>
        </MDBCollapse>
      </MDBContainer>
    </MDBNavbar>
  );
}
