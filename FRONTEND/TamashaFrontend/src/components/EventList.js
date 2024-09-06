import React, { useEffect, useState } from 'react';
import { MDBRow, MDBCol } from 'mdb-react-ui-kit';
import axios from 'axios';
import EventCard from './EventCard';
import Navbar from './Navbar';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

export default function EventList() {
  const [events, setEvents] = useState([]);

  // Fetch events from the backend when the component mounts
  useEffect(() => {
    const fetchEvents = async () => {
      try {
        const token = localStorage.getItem('access_token');
        const response = await axios.get('http://localhost:8000/api/events/', {
          headers: {
            'Authorization': `Bearer ${token}`,
          },
        });
        setEvents(response.data); // Set the fetched events to the state
      } catch (error) {
        toast.error('Failed to fetch events. Please to Login again.');
      }
    };

    fetchEvents();
  }, []);

  return (
    <>
      <Navbar />
      <ToastContainer />
      <MDBRow className='g-4'>
        {events.map((event) => (
          <MDBCol md='3' key={event.title}>
            <EventCard event={event} /> {/* Pass event data as a prop */}
          </MDBCol>
        ))}
      </MDBRow>
    </>
  );
}