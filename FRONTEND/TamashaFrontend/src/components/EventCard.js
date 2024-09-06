import React from 'react';
import { Link } from 'react-router-dom';
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

export default function EventCard({ event }) {
  return (
    <MDBCard className='my-3 shadow-3' style={{ borderRadius: '15px', overflow: 'hidden', border: 'none', height: '350px' }}>
      <MDBRipple rippleColor='light' rippleTag='div' className='bg-image hover-overlay'>
        <MDBCardImage 
          src={event.image_url || 'https://mdbootstrap.com/img/new/standard/nature/111.webp'} 
          fluid 
          alt='Event Image' 
          style={{ maxHeight: '150px', objectFit: 'cover', width: '100%' }} 
        />
        <a href='#'>
          <div className='mask' style={{ backgroundColor: 'rgba(0, 0, 0, 0.5)' }}>
            <p className='text-white text-center m-0 p-3' style={{ fontSize: '1.25rem', fontWeight: 'bold' }}>View Event</p>
          </div>
        </a>
      </MDBRipple>
      <MDBCardBody className='text-center'>
        <MDBCardTitle className='mb-3' style={{ fontSize: '1.25rem', fontWeight: '700', color: '#1D3557' }}>{event.title}</MDBCardTitle>
        <MDBCardText style={{ fontSize: '1rem', color: '#555' }}>Event ID:{event.event_id}</MDBCardText>
        <MDBCardText style={{ fontSize: '0.9rem', color: '#555' }}>
          {event.description.substring(0, 50)}...
        </MDBCardText>
        <MDBBtn href={`/events/${event.id}`} style={{ backgroundColor: '#457B9D', borderRadius: '50px', padding: '12px 24px', fontWeight: 'bold', marginRight: '10px' }}>
          <MDBIcon icon='info-circle' className='me-2' />
          Learn More
        </MDBBtn>
        <Link to={`/events/`+ event.event_id}>learn more</Link>
        <MDBBtn href='/pay' style={{ backgroundColor: '#E63946', borderRadius: '50px', padding: '8px 16px', fontWeight: 'bold' }}>
          <MDBIcon icon='shopping-cart' className='me-2' />
          Buy Now
        </MDBBtn>
      </MDBCardBody>
    </MDBCard>
  );
}



