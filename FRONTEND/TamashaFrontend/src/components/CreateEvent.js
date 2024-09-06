import React,{ useState } from 'react';
import axios from 'axios';
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

import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';


function CreateEvent() {
  const [eventData, setEventData] = useState({
    title: '',
    description: '',
    date: '',
    location: '',
    image_url: ''
  });

  const handleChange = (e) => {
    const { id, value } = e.target;
    setEventData({ ...eventData, [id]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    // Get the token from localStorage
    const token = localStorage.getItem('access_token');

    // Send POST request to the server
    axios.post('http://localhost:8000/api/events/', eventData, {
      headers: {
        'Authorization': `Bearer ${token}`  // Include the JWT token
      }
    })
      .then((response) => {
        toast.success('Event created successfully!');
        setEventData({
          title: '',
          description: '',
          date: '',
          location: '',
          image_url: ''
        });
        // Redirect to the home page after successful event creation
        setTimeout(() => {
          window.location.href = '/';
        }, 5000);
      })
      .catch((error) => {
        if (error.response && error.response.status === 403) {
          toast.error('Authorization error: Please login again.');
        } else {
          toast.error('Failed to create event. Please try again.');
        }
      });
  };

  return (
    <MDBContainer fluid className="d-flex align-items-center justify-content-center" style={{ minHeight: '100vh', padding: '0' }}>
      <div className="w-100" style={{ backgroundImage: 'url(https://mdbootstrap.com/img/new/textures/full/171.jpg)', backgroundSize: 'cover', backgroundPosition: 'center', padding: '60px 0' }}>
        
        <MDBCard className='mx-auto my-5 p-5 shadow-5' style={{ maxWidth: '800px', background: 'hsla(0, 0%, 100%, 0.8)', backdropFilter: 'blur(30px)', borderRadius: '15px' }}>
          <MDBCardBody className='p-5 text-center'>
          <ToastContainer />
            <h2 className="fw-bold mb-5">Create an Event</h2>

              <form onSubmit={handleSubmit}>
              <MDBRow>
                <MDBCol md='6'>
                  <MDBInput 
                    wrapperClass='mb-4' 
                    label='Event Name' 
                    id='title' 
                    type='text' 
                    value={eventData.title}
                    onChange={handleChange} 
                    required
                  />
                </MDBCol>

                <MDBCol md='6'>
                  <MDBInput 
                    wrapperClass='mb-4' 
                    label='Organizer Name' 
                    id='organizerName' 
                    type='text' 
                    required
                  />
                </MDBCol>
              </MDBRow>

              <MDBInput 
                wrapperClass='mb-4' 
                label='Event Date' 
                id='date' 
                type='date' 
                value={eventData.date}
                onChange={handleChange} 
                required
              />
              <MDBInput 
                wrapperClass='mb-4' 
                label='Event Location' 
                id='location' 
                type='text' 
                value={eventData.location}
                onChange={handleChange} 
                required
              />
              <MDBTextArea 
                wrapperClass='mb-4' 
                label='Event Description' 
                id='description' 
                rows={4} 
                value={eventData.description}
                onChange={handleChange} 
                required
              />
              <MDBInput 
                wrapperClass='mb-4' 
                label='Event Image URL' 
                id='image_url' 
                type='url' 
                value={eventData.image_url}
                onChange={handleChange} 
              />

              <MDBBtn type='submit' className='w-100 mb-4' size='md' style={{ backgroundColor: '#E63946', color: '#F1FAEE' }}>Create Event</MDBBtn>
            </form>
            <MDBBtn href='/' className='w-100 mb-4' size='md' style={{ backgroundColor: 'green', color: '#F1FAEE' }}>Back To home</MDBBtn>
          </MDBCardBody>
        </MDBCard>

      </div>
    </MDBContainer>
  );
}

export default CreateEvent;
