import React, { useEffect, useState } from 'react';
import { MDBRow, MDBCol } from 'mdb-react-ui-kit';
import axios from 'axios';
import EventCard from './EventCard';
import Navbar from './Navbar';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

export default function EventList() {
  const [events, setEvents] = useState([]);
  const apiUrl = process.env.REACT_APP_API_URL;

  // Fetch events from the backend when the component mounts
  useEffect(() => {
    const fetchEvents = async () => {
      try {
        const token = localStorage.getItem('access_token');
        const response = await axios.get(`${apiUrl}api/events/`, {
          headers: {
            'Authorization': `Bearer ${token}`,
          },
        });

        // Log the response data to confirm the format
        console.log('Events response data:', response.data);

        // Ensure data is an array
        if (Array.isArray(response.data)) {
          setEvents(response.data); // Set the fetched events to the state
        } else {
          toast.error('Unexpected response format from API.');
        }
      } catch (error) {
        toast.error('Failed to fetch events. Please login again.');
        console.error('Error fetching events:', error);
      }
    };

    fetchEvents();
  }, [apiUrl]);

  return (
    <>
      <Navbar />
      <ToastContainer />
      <MDBRow className='g-4'>
        {/* Conditional rendering to ensure events is an array */}
        {Array.isArray(events) && events.length > 0 ? (
          events.map((event) => (
            <MDBCol md='3' key={event.event_id}>
              <EventCard event={event} /> {/* Pass event data as a prop */}
            </MDBCol>
          ))
        ) : (
          <p>No events available</p>
        )}
      </MDBRow>
    </>
  );
}
