import React from 'react';
import Navbar from './Navbar';
import Back from './Background';
import AboutUs from './Aboutus';
import Contactus from './Contactus';
import Footer from './Footer';
import { MDBContainer } from 'mdb-react-ui-kit';

function Layout() {
  return (
    <>
      <Navbar />
      <MDBContainer fluid className="p-0">
        <Back />
        <section id="about-us" style={{ padding: '50px 20px', backgroundColor: '#F1FAEE' }}>
          <AboutUs />
        </section>
        <section id="contact-us" style={{ padding: '50px 20px', backgroundColor: '#F1FAEE', color: '#F1FAEE'}}>
          <Contactus />
        </section>
      </MDBContainer>
      <Footer />
    </>
  );
}

export default Layout;