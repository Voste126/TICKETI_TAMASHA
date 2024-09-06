import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import { validate as uuidValidate } from 'uuid';
import { MDBContainer, MDBRow, MDBCol, MDBCard, MDBCardBody, MDBCardTitle, MDBCardText, MDBCardImage, MDBBtn, MDBSpinner } from 'mdb-react-ui-kit';

function EventDetails() {
  const {event_id} = useParams();
  const id = event_id;
  const [event, setEvent] = useState(null); // State to hold the event data
  const [loading, setLoading] = useState(true); // Loading state
   
  useEffect(() => {
    console.log("Event ID:", event_id); 
    const token = localStorage.getItem('access_token'); // Get the token from localStorage
    
    if (uuidValidate(event_id)) {
      // Fetch event details based on the event ID
      //api/events/<uuid:pk>/

      axios.get(`http://localhost:8000/api/events/${event_id}/`,{
        headers: {
            'Authorization': `Bearer ${token}`,
        },
      })
      .then(response => {
        setEvent(response.data); // Set the event data to state
        setLoading(false); // Disable loading once data is fetched
      })
      .catch(error => {
        console.error("Error fetching event details:", error);
        setLoading(false); // Disable loading even if an error occurs
      });
    } else {
      console.error('Invalid UUID');
      setLoading(false); // Disable loading if the UUID is invalid
    }
  }, [event_id]);

  // Loading spinner while fetching data
  if (loading) {
    return (
      <MDBContainer className="d-flex justify-content-center align-items-center" style={{ minHeight: '100vh' }}>
        <MDBSpinner role="status">
          <span className="visually-hidden">Loading...</span>
        </MDBSpinner>
      </MDBContainer>
    );
  }

  // Check if event data is available before rendering
  if (!event) {
    return (
      <MDBContainer className="d-flex justify-content-center align-items-center" style={{ minHeight: '100vh' }}>
        <p>Error loading event details. Please try again later.</p>
      </MDBContainer>
    );
  }

  // Display the event details once fetched
  return (
    <MDBContainer style={{ padding: '50px 0' }}>
      <MDBCard className="shadow-5 mb-5" style={{ borderRadius: '15px' }}>
        <MDBRow className="g-0">
          <MDBCol md="6">
            <MDBCardImage
              src={event.image_url || 'https://mdbootstrap.com/img/new/standard/nature/111.webp'} // Default image if not available
              alt="Event"
              fluid
              className="rounded-start"
              style={{ maxHeight: '100%', objectFit: 'cover' }}
            />
          </MDBCol>
          <MDBCol md="6">
            <MDBCardBody>
              <MDBCardTitle style={{ fontSize: '2rem', color: '#1D3557' }}>{event.title}</MDBCardTitle>
              <MDBCardText style={{ fontSize: '1.2rem', color: '#555', marginBottom: '20px' }}>
                {event.description}
              </MDBCardText>
              <MDBCardText>
                <strong>Date:</strong> {new Date(event.date).toLocaleDateString()}
              </MDBCardText>
              <MDBCardText>
                <strong>Location:</strong> {event.location}
              </MDBCardText>
              <MDBBtn href='/events' style={{ backgroundColor: '#E63946', borderRadius: '50px', fontWeight: 'bold' }}>Back to Events</MDBBtn>
            </MDBCardBody>
          </MDBCol>
        </MDBRow>
      </MDBCard>
    </MDBContainer>
  );
}

export default EventDetails;


