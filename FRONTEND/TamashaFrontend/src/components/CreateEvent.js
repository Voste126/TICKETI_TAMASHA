import React from 'react';
import {
  MDBBtn,
  MDBContainer,
  MDBCard,
  MDBCardBody,
  MDBCol,
  MDBRow,
  MDBInput,
  MDBTextArea
} from 'mdb-react-ui-kit';

function CreateEvent() {
  return (
    <MDBContainer fluid className="d-flex align-items-center justify-content-center" style={{ minHeight: '100vh', padding: '0' }}>
      <div className="w-100" style={{ backgroundImage: 'url(https://mdbootstrap.com/img/new/textures/full/171.jpg)', backgroundSize: 'cover', backgroundPosition: 'center', padding: '60px 0' }}>
        
        <MDBCard className='mx-auto my-5 p-5 shadow-5' style={{ maxWidth: '800px', background: 'hsla(0, 0%, 100%, 0.8)', backdropFilter: 'blur(30px)', borderRadius: '15px' }}>
          <MDBCardBody className='p-5 text-center'>

            <h2 className="fw-bold mb-5">Create an Event</h2>

            <MDBRow>
              <MDBCol md='6'>
                <MDBInput wrapperClass='mb-4' label='Event Name' id='eventName' type='text' />
              </MDBCol>

              <MDBCol md='6'>
                <MDBInput wrapperClass='mb-4' label='Organizer Name' id='organizerName' type='text' />
              </MDBCol>
            </MDBRow>

            <MDBInput wrapperClass='mb-4' label='Event Date' id='eventDate' type='date' />
            <MDBInput wrapperClass='mb-4' label='Event Location' id='eventLocation' type='text' />
            <MDBTextArea wrapperClass='mb-4' label='Event Description' id='eventDescription' rows={4} />

            <MDBBtn href='#' className='w-100 mb-4' size='md' style={{ backgroundColor: '#E63946', color: '#F1FAEE' }}>Create Event</MDBBtn>
            <MDBBtn href='/' className='w-100 mb-4' size='md' style={{ backgroundColor: 'green', color: '#F1FAEE' }}>Back To home</MDBBtn>
          </MDBCardBody>
        </MDBCard>

      </div>
    </MDBContainer>
  );
}

export default CreateEvent;
