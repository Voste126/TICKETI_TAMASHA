import React from 'react';
import {
  MDBCard,
  MDBCardBody,
  MDBCardTitle,
  MDBCardText,
  MDBCardImage,
  MDBBtn,
  MDBRipple,
  MDBIcon
} from 'mdb-react-ui-kit';

export default function EventCard() {
  return (
    <MDBCard className='my-3 shadow-3' style={{ borderRadius: '20px', overflow: 'hidden', border: 'none' }}>
      <MDBRipple rippleColor='light' rippleTag='div' className='bg-image hover-overlay'>
        <MDBCardImage 
          src='https://mdbootstrap.com/img/new/standard/nature/111.webp' 
          fluid 
          alt='Event Image' 
          style={{ maxHeight: '200px', objectFit: 'cover' }} 
        />
        <a href='#'>
          <div className='mask' style={{ backgroundColor: 'rgba(0, 0, 0, 0.5)' }}>
            <p className='text-white text-center m-0 p-3' style={{ fontSize: '1.25rem', fontWeight: 'bold' }}>View Event Details</p>
          </div>
        </a>
      </MDBRipple>
      <MDBCardBody className='text-center'>
        <MDBCardTitle className='mb-3' style={{ fontSize: '1.75rem', fontWeight: '700', color: '#1D3557' }}>Event Title</MDBCardTitle>
        <MDBCardText style={{ fontSize: '1rem', color: '#555', marginBottom: '20px' }}>
          This is a brief description of the event. It gives an overview to entice users to learn more or attend.
        </MDBCardText>
        <MDBBtn href='#' style={{ backgroundColor: '#457B9D', borderRadius: '50px', padding: '12px 24px', fontWeight: 'bold', marginRight: '10px' }}>
          <MDBIcon icon='info-circle' className='me-2' />
          Learn More
        </MDBBtn>
        <MDBBtn href='/pay' style={{ backgroundColor: '#E63946', borderRadius: '50px', padding: '12px 24px', fontWeight: 'bold' }}>
          <MDBIcon icon='shopping-cart' className='me-2' />
          Buy Now
        </MDBBtn>
      </MDBCardBody>
    </MDBCard>
  );
}

