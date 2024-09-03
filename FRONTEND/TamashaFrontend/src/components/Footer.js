import React from 'react';
import { MDBFooter, MDBContainer, MDBRow, MDBCol, MDBIcon } from 'mdb-react-ui-kit';

export default function Footer() {
  return (
    <MDBFooter bgColor='dark' className='text-center text-lg-start text-muted'>
      {/* Social Media Section */}
      <section className='d-flex justify-content-center justify-content-lg-between p-4 border-bottom'>
        <div className='me-5 d-none d-lg-block'>
          <span style={{ color: '#F1FAEE', fontFamily: 'Poppins, sans-serif' }}>Get connected with us on social networks:</span>
        </div>

        <div>
          <a href='#' className='me-4 text-reset'>
            <MDBIcon fab icon="facebook-f" style={{ color: '#E63946' }} />
          </a>
          <a href='#' className='me-4 text-reset'>
            <MDBIcon fab icon="twitter" style={{ color: '#E63946' }} />
          </a>
          <a href='#' className='me-4 text-reset'>
            <MDBIcon fab icon="google" style={{ color: '#E63946' }} />
          </a>
          <a href='#' className='me-4 text-reset'>
            <MDBIcon fab icon="instagram" style={{ color: '#E63946' }} />
          </a>
          <a href='#' className='me-4 text-reset'>
            <MDBIcon fab icon="linkedin" style={{ color: '#E63946' }} />
          </a>
          <a href='#' className='me-4 text-reset'>
            <MDBIcon fab icon="github" style={{ color: '#E63946' }} />
          </a>
        </div>
      </section>

      {/* Footer Content */}
      <section className=''>
        <MDBContainer className='text-center text-md-start mt-5'>
          <MDBRow className='mt-3'>
            {/* Company Name and Info */}
            <MDBCol md="3" lg="4" xl="3" className='mx-auto mb-4'>
              <h6 className='text-uppercase fw-bold mb-4' style={{ color: '#E63946', fontFamily: 'Lobster, cursive' }}>
                <MDBIcon icon="gem" className="me-3" />
                Tiketi Tamasha
              </h6>
              <p style={{ color: '#F1FAEE', fontFamily: 'Poppins, sans-serif', fontSize: '14px' }}>
                Tiketi Tamasha is your one-stop platform for seamless event ticketing and management. Join us and elevate your event experiences with our user-friendly platform and efficient tools.
              </p>
            </MDBCol>

            {/* Products */}
            <MDBCol md="2" lg="2" xl="2" className='mx-auto mb-4'>
              <h6 className='text-uppercase fw-bold mb-4' style={{ color: '#E63946', fontFamily: 'Poppins, sans-serif' }}>Products</h6>
              <p>
                <a href='#' className='text-reset' style={{ color: '#F1FAEE', fontFamily: 'Poppins, sans-serif', fontSize: '14px' }}>
                  Event Creation
                </a>
              </p>
              <p>
                <a href='#' className='text-reset' style={{ color: '#F1FAEE', fontFamily: 'Poppins, sans-serif', fontSize: '14px' }}>
                  Ticket Management
                </a>
              </p>
              <p>
                <a href='#' className='text-reset' style={{ color: '#F1FAEE', fontFamily: 'Poppins, sans-serif', fontSize: '14px' }}>
                  Payment Integration
                </a>
              </p>
              <p>
                <a href='#' className='text-reset' style={{ color: '#F1FAEE', fontFamily: 'Poppins, sans-serif', fontSize: '14px' }}>
                  Analytics
                </a>
              </p>
            </MDBCol>

            {/* Useful Links */}
            <MDBCol md="3" lg="2" xl="2" className='mx-auto mb-4'>
              <h6 className='text-uppercase fw-bold mb-4' style={{ color: '#E63946', fontFamily: 'Poppins, sans-serif' }}>Useful links</h6>
              <p>
                <a href='#' className='text-reset' style={{ color: '#F1FAEE', fontFamily: 'Poppins, sans-serif', fontSize: '14px' }}>
                  Pricing
                </a>
              </p>
              <p>
                <a href='#' className='text-reset' style={{ color: '#F1FAEE', fontFamily: 'Poppins, sans-serif', fontSize: '14px' }}>
                  Settings
                </a>
              </p>
              <p>
                <a href='#' className='text-reset' style={{ color: '#F1FAEE', fontFamily: 'Poppins, sans-serif', fontSize: '14px' }}>
                  Orders
                </a>
              </p>
              <p>
                <a href='#' className='text-reset' style={{ color: '#F1FAEE', fontFamily: 'Poppins, sans-serif', fontSize: '14px' }}>
                  Help
                </a>
              </p>
            </MDBCol>

            {/* Contact Information */}
            <MDBCol md="4" lg="3" xl="3" className='mx-auto mb-md-0 mb-4'>
              <h6 className='text-uppercase fw-bold mb-4' style={{ color: '#E63946', fontFamily: 'Poppins, sans-serif' }}>Contact</h6>
              <p style={{ color: '#F1FAEE', fontFamily: 'Poppins, sans-serif', fontSize: '14px' }}>
                <MDBIcon icon="home" className="me-2" />
                Nairobi, Kenya
              </p>
              <p style={{ color: '#F1FAEE', fontFamily: 'Poppins, sans-serif', fontSize: '14px' }}>
                <MDBIcon icon="envelope" className="me-3" />
                support@tiketitamasha.com
              </p>
              <p style={{ color: '#F1FAEE', fontFamily: 'Poppins, sans-serif', fontSize: '14px' }}>
                <MDBIcon icon="phone" className="me-3" /> +254 700 123 456
              </p>
              <p style={{ color: '#F1FAEE', fontFamily: 'Poppins, sans-serif', fontSize: '14px' }}>
                <MDBIcon icon="print" className="me-3" /> +254 700 123 457
              </p>
            </MDBCol>
          </MDBRow>
        </MDBContainer>
      </section>

      {/* Copyright Section */}
      <div className='text-center p-4' style={{ backgroundColor: '#1D3557', color: '#F1FAEE', fontFamily: 'Poppins, sans-serif' }}>
        © 2024 Copyright:
        <a className='text-reset fw-bold' href='https://tiketitamasha.com/' style={{ color: '#E63946' }}>
          Tiketi Tamasha
        </a>
      </div>
    </MDBFooter>
  );
}
